#!/usr/bin/env python3

import sys
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class NucleotideBases:
    """
    Dataclass NucleotideBases helps keep track of the number of each base
    in a string of DNA bases. By default, the class will initialize with
    0 as the count, allowing us to increment each field upward as we
    iterate through a string.
    """

    A: int = 0
    T: int = 0
    G: int = 0
    C: int = 0
    U: int = 0


def count_bases_by_type(
    bases: List[str],
    base_counts: NucleotideBases = NucleotideBases(),
    next: Optional[int] = None,
) -> NucleotideBases:
    """
    Take a list of characters presumed to be a list of nucleotide
    bases and recursively count the occurrence of each base, saving the
    final tallies in dataclass `NucleotideBases`.
    """
    if len(bases) == 0:
        return base_counts

    # if on the first base, which is to say the base at the end
    # of the DNA base list, next will have its default value, None. To
    # get started, we shadow/overwrite next with the index of the rightmost
    # base. In Python, which is zero-indexed, the rightmost index is
    # len(bases) - 1
    if next is None:
        next = len(bases) - 1

    # next, we use structural pattern matching, introduced in 2021 with Python 3.10
    # to neatly figure out what the current base is. In doing so, we make sure that
    # the input base character is uppercase and also supply a so-called default
    # case, `case _`, so we don't get an error if a weird character is present. Using
    # pass here essentially tells Python to ignore or do nothing if it encounters an
    # unmatched character. For each matched character, it increments our NucleotideBases
    # dataclass field for that base up by one.
    match bases[next].upper():
        case "A":
            base_counts.A += 1
        case "T":
            base_counts.T += 1
        case "G":
            base_counts.G += 1
        case "C":
            base_counts.C += 1
        case "U":
            base_counts.U += 1
        case _:
            pass

    # if we're on the last base character, we're now finished and can early-return
    # our count of bases.
    if next == 0:
        return base_counts

    # otherwise, run the function again on the next base
    return count_bases_by_type(bases, base_counts, next - 1)


def print_answer_report(final_tallies: NucleotideBases) -> None:
    """
    Print a formatted report of the tallies for each base and format the
    answer.
    """
    my_answer = (
        f"{final_tallies.A} {final_tallies.C} {final_tallies.G} {final_tallies.T}"
    )

    # print out the tallies:
    print("Our final tally of bases is:")
    print("----------------------------")
    print(f"Adenines: {final_tallies.A}")
    print(f"Thymine: {final_tallies.T}")
    print(f"Guanines: {final_tallies.G}")
    print(f"Cytosines: {final_tallies.C}")

    print("\n\nAnd to format like the problem asked:")
    print(my_answer)


def main() -> None:
    """
    Take the input DNA string, tally each base, and check if the tallies
    are the correct answer.
    """
    # get the input dataset from the command line
    input_file = sys.argv[1]

    # read the rosalind input
    dna_string: str
    with open(input_file, "r", encoding="utf8") as input_handle:
        dna_string = input_handle.read().splitlines()[0]

    # convert the long string to a list of characters
    base_list = [*dna_string]

    # retrieve my final tally and format my answer
    final_tallies = count_bases_by_type(base_list)

    # print out my answer
    print_answer_report(final_tallies)


if __name__ == "__main__":
    main()
