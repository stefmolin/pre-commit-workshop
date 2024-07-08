from pathlib import Path


def validate_filename(filename: str, min_len: int = 3) -> int:
    # extract the name so that `/my/repo/x.py` becomes `x`
    name = Path(filename).stem

    # check the length
    if failure := len(name) < min_len:
        print(f'Name too short ({min_len=}): {filename}')

    # convert to an exit code for later
    return int(failure)
