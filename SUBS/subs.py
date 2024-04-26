#!/usr/bin/env python3

import sys
from typing import List


def scan_for_motif(
    query_seq: str, motif: str, window_start: int = 0, hits: List[int] = []
) -> List[int]:
    """
    Recursively search for a motif within a given query sequence. At each
    recursion, `scan_for_motif()` checks if there are enough bases left after
    the input index to match an entire motif. If not, it early returns the list
    of hits and ceases to recurse.
    """
    # run some checks
    if len(query_seq) < len(motif) or len(motif) == 0:
        return hits

    # determine the window size based on the length of the motif
    window_size = len(motif)

    # determine the indices of the query window based on the window size
    window_end = window_start + window_size

    # if there aren't enough bases left to check another window, early return
    if window_end > len(query_seq):
        return hits

    # otherwise, proceed by slicing the window and checking if it matches the motif. If it does, append the index of the match to the list of hits
    window = query_seq[window_start:window_end]
    if window == motif:
        hits.append(window_start + 1)

    # recursively proceed to the next window if there are still enough bases
    # left in the query sequence
    return scan_for_motif(query_seq, motif, window_start + 1, hits)


def main() -> None:
    """
    Script entrypoint coordinating the flow of data through the above functions
    """
    # read the input file
    input_file = sys.argv[1]

    # read the rosalind input file
    input_list: List[str] = []
    with open(input_file, "r", encoding="utf8") as input_handle:
        input_list = input_handle.read().splitlines()

    # run some checks
    assert (
        len(input_list) == 2
    ), "The length of the input list, which comes from parsing the input file line by line, does not match 2. Please double check that it's the right file."
    assert (
        len(input_list[0]) > len(input_list[1])
    ), "The first line of the input list is expected to be the query sequence, which must be longer than the motif expected in the second line."

    # parse out the query sequence and motif
    query_seq, motif = input_list

    # scan for hits
    my_answer = scan_for_motif(query_seq, motif)

    # format my answer
    formatted_answer = " ".join([str(item) for item in my_answer])

    # print out my results
    print(f"My answer is:\n\n{formatted_answer}")


if __name__ == "__main__":
    main()
