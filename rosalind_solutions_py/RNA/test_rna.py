#!/usr/bin/env python3

from .rna import transcribe_dna


def test_with_sample_data() -> None:
    dna_string = "GATGGAACTTGACTACGTAAATT"
    expected_answer = "GAUGGAACUUGACUACGUAAAUU"
    my_answer = transcribe_dna(dna_string)
    assert (
        my_answer == expected_answer
    ), f"My answer '{my_answer}' was incorrect. Try again!"
    print(
        f"Successfully transcribed the DNA sequence '{dna_string}' into RNA: '{my_answer}'"
    )
