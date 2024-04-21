#!/usr/bin/env python3

import os
import sys
from pathlib import Path
from typing import List

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from numpy import argmax
from pydantic.dataclasses import dataclass


@dataclass(frozen=True)
class RecordWithGC:
    """
    Store a FASTA record ID and GC content alongside each other as easily
    accessed, statically typed fields in an immutable dataclass.
    """

    id: str
    gc: float


def parse_fasta_records(fasta_file: str) -> List[SeqRecord]:
    """
    Eagerly parse all records in the short input FASTA into a list that can be
    sorted by GC-content downstream while making sure that records could
    actually be parsed.
    """
    fasta_path = Path(fasta_file)

    records = list(SeqIO.parse(fasta_path, "fasta"))

    assert (
        len(records) > 1
    ), f"Too few records ({len(records)}) found in the provided FASTA file."

    return records


def compute_gc_content(record: SeqRecord) -> float:
    """
    Compute GC-content by counting the number of G's and C's in a given sequence
    record, dividing by the total number of bases, multiplying by 100 to get a
    percentage, and rounding to 6 decimal points.
    """
    seq_len = len(record.seq)
    gc_count = record.seq.count("G") + record.seq.count("C")
    gc_percentage = gc_count / seq_len * 100

    return round(gc_percentage, 6)


def find_max_gc_content(records: List[SeqRecord]) -> RecordWithGC:
    """
    Iterate through each record in the provided FASTA, computing the GC-content
    for each, and find the index in the resulting list of GC-contents with the
    maximum value. Then, initialize a `RecordWithGC` instance with the
    associated record ID and GC-content.
    """
    gc_contents = [compute_gc_content(record) for record in records]
    max_index = argmax(gc_contents)
    max_id = str(records[max_index].id)
    max_gc = gc_contents[max_index]

    return RecordWithGC(id=max_id, gc=max_gc)


def format_my_answer(max_gc_record: RecordWithGC) -> str:
    """
    Rosalind retains trailing zeroes in rounded values in their sample data,
    which is not the default behavior for Python floats. Here, we format our
    answer with an f-string trick that ensures the GC-content float has as many
    digits as Rosalind expects.
    """
    return f"{max_gc_record.id}\n{max_gc_record.gc:.6f}"


def main() -> None:
    """
    Script entrypoint coordinating the flow of data through the above functions.
    """
    # grab the file from the command line
    fasta_file = sys.argv[1]

    # make sure that file exists
    assert os.path.exists(
        fasta_file
    ), f"Provided fasta file {fasta_file} does not exist."

    # parse out the records into a list of Biopython seqrecords
    records = parse_fasta_records(fasta_file)

    # parse out which has the most GC-content
    max_gc_record = find_max_gc_content(records)

    # format my answer
    my_answer = format_my_answer(max_gc_record)

    # print out the results
    print(f"The maximum GC-content record in the provided FASTA {fasta_file} was:")
    print(f"\n{my_answer}")


if __name__ == "__main__":
    main()
