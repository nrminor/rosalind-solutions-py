#!/usr/bin/env python3

from .dna import count_bases_by_type


def test_with_sample_data():
    dna_string = (
        "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
    )
    expected_answer = "20 12 17 21"
    base_list = [*dna_string]
    final_tallies = count_bases_by_type(base_list)
    my_answer = (
        f"{final_tallies.A} {final_tallies.C} {final_tallies.G} {final_tallies.T}"
    )
    # is my answer correct?
    assert (
        my_answer == expected_answer
    ), f"My answer '{my_answer}' was incorrect. Try again!"
