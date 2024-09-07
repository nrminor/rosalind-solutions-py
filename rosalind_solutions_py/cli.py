import argparse


def parse_command_line_args() -> argparse.Namespace:
    """
    Command line argument parser that uses subparser subcommands to call for solutions
    to individual Rosalind challenges. Most subcommands require only an input file,
    though more advanced challenges require additional controls via the command line.
    """
    parser = argparse.ArgumentParser()

    # set up some subparsers
    subparsers = parser.add_subparsers(title="Subcommands", dest="subcommands")
    dna = subparsers.add_parser("dna", help="Solve the Rosalind DNA challenge.")

    # add arguments for the dna challenge
    dna.add_argument(
        "--input",
        "-i",
        type=str,
        help="Input file provided by the Rosalind challenge.",
        required=True,
    )

    return parser.parse_args()
