"""Validate filename."""

from pathlib import Path


def validate_filename(filename: str, min_len: int = 3) -> int:
    """
    Validate the filename is long enough.

    Parameters
    ----------
    filename : str
        The filename as a string.
    min_len : int, optional
        The minimum length for a valid filename, by default 3.

    Returns
    -------
    int
        The exit status, where zero means the filename is valid.
    """
    # extract the name so that `/my/repo/x.py` becomes `x`
    name = Path(filename).stem

    # check the length
    if failure := len(name) < min_len:
        print(f'Name too short ({min_len=}): {filename}')

    # convert to an exit code for later
    return int(failure)
