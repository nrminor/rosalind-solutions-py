#!/usr/bin/env python3

from .subs import scan_for_motif


def test_with_sample_data() -> None:
    test_seq = "GATATATGCATATACTT"
    motif = "ATAT"
    expected_answer = [2, 4, 10]

    my_answer = scan_for_motif(test_seq, motif)

    assert (
        my_answer == expected_answer
    ), f"My answer {my_answer} doesn't match the expected answer, {expected_answer}"
