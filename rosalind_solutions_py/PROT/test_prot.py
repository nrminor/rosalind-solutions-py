#!/usr/bin/env python3


def test_with_sample_data() -> None:
    """
    Test my solution to PROT against the sample data provided in the challenge
    description at https://rosalind.info/problems/prot/
    """

    sample_dataset = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    _expected_answer = "MAMAPRTEINSTRING"

    assert (
        len(sample_dataset) % 3 == 0
    ), f"The provided string of RNA nucleotides contains at least one incomplete codon:\n{sample_dataset}"
