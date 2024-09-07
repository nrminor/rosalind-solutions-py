#!/usr/bin/env python3

import sys


def complement_per_base(base_char: str) -> str:
    """
    Match the input base with the correct complement base
    """
    # use pattern matching to return the correct complement
    # base for each the input base character, while making
    # sure that the base is uppercase as expected. Unknown
    # bases are given the complement 'N' to avoid crashing
    # at unexpected characters
    match base_char.upper():
        case "A":
            return "T"
        case "T":
            return "A"
        case "G":
            return "C"
        case "C":
            return "G"
        case _:
            return "N"


def get_reverse_complement(dna_string: str) -> str:
    """
    Find the reverse complement for a DNA string of arbitrary length.
    """
    # unpack the DNA string into a list of individual characters
    base_list = [*dna_string]

    # use a list comprehension to find the complement of each base in
    # the list and generate a new list of non-reversed complement bases
    complements = [complement_per_base(base) for base in base_list]

    # join the complement bases into a single string
    complement_str = "".join(complements)

    # return the complements in reverse order
    return complement_str[::-1]


def main() -> None:
    """
    Take the input DNA string, find its reverse complement, and check that it's
    the correct answer.
    """
    # get the input dataset from the command line
    input_file = sys.argv[1]

    # read the rosalind input
    dna_string: str
    with open(input_file, "r", encoding="utf8") as input_handle:
        dna_string = input_handle.read().splitlines()[0]

    # get the reverse complement
    my_answer = get_reverse_complement(dna_string)

    # print the answer
    print(f"My answer is:\n{my_answer}")


if __name__ == "__main__":
    main()
