#!/usr/bin/env python3


def transcribe_dna(dna_string: str) -> str:
    """
    Unpack the DNA string into a list of individual characters. Then,
    iterate through them, replacing any T's with U's and leaving the rest
    of the bases unchanged. Then, join them into a single string again and
    return.
    """
    dna_bases = [*dna_string]
    rna_bases = ["U" if base == "T" else base for base in dna_bases]

    return "".join(rna_bases)


def main() -> None:
    """
    Take the input DNA string, transcribe into RNA, and check that it's
    the correct answer.
    """

    # here are the inputs: a DNA nucleotide string and the expected answer
    dna_string = "GATGGAACTTGACTACGTAAATT"
    expected_answer = "GAUGGAACUUGACUACGUAAAUU"

    # transcribe the DNA into RNA
    my_answer = transcribe_dna(dna_string)

    # is my answer correct?
    assert (
        my_answer == expected_answer
    ), f"My answer '{my_answer}' was incorrect. Try again!"

    # if so, print out the answer
    print(
        f"Successfully transcribed the DNA sequence '{dna_string}' into RNA: '{my_answer}'"
    )


if __name__ == "__main__":
    main()
