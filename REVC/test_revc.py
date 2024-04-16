#!/usr/bin/env python3

from .revc import get_reverse_complement


def test_with_sample_data() -> None:
    dna_string = "AAAACCCGGT"
    expected_answer = "ACCGGGTTTT"
    my_answer = get_reverse_complement(dna_string)
    assert (
        my_answer == expected_answer
    ), f"My answer '{my_answer}' was incorrect. Try again!"
    print(f"Successfully got the reverse complement '{dna_string}': '{my_answer}'")
