"""CLI for validating filenames."""

import argparse
from typing import Sequence

from .validate_filename import validate_filename


def main(argv: Sequence[str] | None = None) -> int:
    """
    Run filename validation.

    Parameters
    ----------
    argv : Sequence[str] | None, optional
        Command line arguments.

    Returns
    -------
    int
        Exit code.
    """
    parser = argparse.ArgumentParser(prog='validate-filename')
    parser.add_argument(
        'filenames',
        nargs='*',
        help='Filenames to process.',
    )
    parser.add_argument(
        '--min-len',
        default=3,
        type=int,
        help='Minimum length for a filename.',
    )

    args = parser.parse_args(argv)

    results = [validate_filename(filename, args.min_len) for filename in args.filenames]
    return int(any(results))
