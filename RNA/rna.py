#!/usr/bin/env python3

import sys


def transcribe_dna(dna_string: str) -> str:
    """
    Unpack the DNA string into a list of individual characters. Then,
    iterate through them, replacing any T's with U's and leaving the rest
    of the bases unchanged. Then, join them into a single string again and
    return.
    """
    rna_bases = ["U" if base == "T" else base for base in dna_string]

    return "".join(rna_bases)


def main() -> None:
    """
    Take the input DNA string, transcribe into RNA, and check that it's
    the correct answer.
    """
    # get the input dataset from the command line
    input_file = sys.argv[1]

    # read the rosalind input
    dna_string: str
    with open(input_file, "r", encoding="utf8") as input_handle:
        dna_string = input_handle.read().splitlines()[0]

    # transcribe the DNA into RNA
    my_answer = transcribe_dna(dna_string)

    # print the answer
    print(f"My answer is:\n{my_answer}")


if __name__ == "__main__":
    main()
