#!/usr/bin/env python3


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

    # here are the inputs: a DNA nucleotide string and the expected answer
    dna_string = "AAAACCCGGT"
    expected_answer = "ACCGGGTTTT"

    # get the reverse complement
    my_answer = get_reverse_complement(dna_string)

    # is my answer correct?
    assert (
        my_answer == expected_answer
    ), f"My answer '{my_answer}' was incorrect. Try again!"

    # if so, print out the answer
    print(f"Successfully got the reverse complement '{dna_string}': '{my_answer}'")


if __name__ == "__main__":
    main()
