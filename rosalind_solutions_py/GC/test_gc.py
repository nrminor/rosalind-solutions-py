#!/usr/bin/env python3

import os
import sys
from pathlib import Path

from .gc import find_max_gc_content, format_my_answer, parse_fasta_records


def find_test_fasta() -> Path:
    cwd = Path.cwd()
    test_fa_paths = list(cwd.glob("**/GC/**/test.fa"))
    if len(test_fa_paths) == 1:
        test_fa_path = test_fa_paths[0]
        print(f"Found test.fa at: {test_fa_path}")
        return test_fa_path
    elif len(test_fa_paths) == 0:
        print("No 'test.fa' file found in any 'GC' subdirectory. Aborting.")
        sys.exit(1)
    else:
        print(
            "Multiple redundant 'test.fa' file found in 'GC' subdirectories. Aborting."
        )
        sys.exit(1)


def test_with_sample_data() -> None:
    fasta_file = find_test_fasta()
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
