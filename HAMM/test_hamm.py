#!/usr/bin/env/python3

from .hamm import check_seqs, compute_hamming_distance


def test_with_sample_data() -> None:
    # assign the sample data provided in the challenge introduction
    test_seqs = ["GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"]
    expected_answer = 7

    # check the sample sequences
    seq1, seq2 = check_seqs(test_seqs)

    # compute an answer
    my_answer = compute_hamming_distance(seq1, seq2)

    # make sure it matches the expected answer
    assert (
        my_answer == expected_answer
    ), f"My answer to the Hamming distance, {my_answer}, does not match the expected answer, {expected_answer}."
