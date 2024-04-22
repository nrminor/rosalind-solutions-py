#!/usr/bin/env python3

import os
import sys
from typing import List, Tuple


def check_seqs(test_seqs: List[str]) -> Tuple[str, str]:
    """
    Check that only two sequences were found in the provided file, and that both
    sequences are the same length.
    """

    assert (
        len(test_seqs) == 2
    ), f"{len(test_seqs)} sequences provided whereas 2 were expected."

    seq1 = test_seqs[0]
    seq2 = test_seqs[1]

    assert (
        len(seq1) == len(seq2)
    ), f"The {len(seq1)} characters in the first sequence not match {len(seq2)}, the number of characters in the second sequence."

    return (seq1, seq2)


def compute_hamming_distance(seq1: str, seq2: str) -> int:
    """
    Count the number of bases that don't match between the two sequences.
    """
    distance = 0
    for seq1_base, seq2_base in zip(seq1, seq2):
        if seq1_base != seq2_base:
            distance += 1
    return distance


def main() -> None:
    """
    Script entrypoint coordinating the flow of data through the above functions.
    """
    # get the input dataset from the command line
    input_file = sys.argv[1]

    # make sure the provided file exists
    assert os.path.isfile(
        input_file
    ), f"The provided filename {input_file} does not exist."

    # read the rosalind input file
    seq_list: List[str] = []
    with open(input_file, "r", encoding="utf8") as input_handle:
        seq_list = input_handle.read().splitlines()

    # check the sequences to make sure there are only two and that the length of
    # each sequence is the same (which is all Hamming distances can handle)
    seq1, seq2 = check_seqs(seq_list)

    # find the number of differences between the checked sequences
    my_distance = compute_hamming_distance(seq1, seq2)

    # print out my answer for input into Rosalind
    print(
        f"The pairwise Hamming distance between the two sequences is:\n\n{my_distance}"
    )


if __name__ == "__main__":
    main()
