#!/usr/bin/env python3

import os

from .gc import find_max_gc_content, format_my_answer, parse_fasta_records


def test_with_sample_data() -> None:
    fasta_file = "GC/test.fa"
    expected_answer = "Rosalind_0808\n60.919540"

    # make sure that file exists
    assert os.path.exists(
        fasta_file
    ), f"Provided fasta file {fasta_file} does not exist."

    # parse out the records into a list of Biopython seqrecords
    records = parse_fasta_records(fasta_file)

    # parse out which has the most GC-content
    max_gc_record = find_max_gc_content(records)

    # format the answer
    my_formatted_answer = format_my_answer(max_gc_record)

    assert (
        my_formatted_answer == expected_answer
    ), "My answer is not the same is the expected Rosalind answer."
