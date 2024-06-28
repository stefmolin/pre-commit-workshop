# Demos

Run the demos in VS Code for the combined view of the file contents and the terminal.

## Setup

Increase VS Code font size beforehand:

1. Open settings.
2. Change font size to 24 (original is 12).
3. Search for `terminal.integrated.font-size` and change it to 24 as well (original is 12).

Create a fresh virtual environment:

```shell
$ conda create --name pre-commit-demo python=3.12
$ conda activate pre-commit-demo
```

## Section 1 demos

### Pre-commit package installation

1. Branch off of `main` (name it after the event).
2. With a pre-made virtual environment activated, run `python3 -m pip install pre-commit`.

### Install first set of hooks

1. Create `.pre-commit-config.yaml` file copying the contents from the slides.
2. Run `pre-commit install`.
3. Commit the `.pre-commit-config.yaml` file.

### Adding `ruff`

1. Copy `ruff` section from slides into `.pre-commit-config.yaml` file.
2. Commit the changes.
3. Create `example.py` file with issues for `ruff` to find (copying from slides).
4. Try to commit the file.
5. Run `git diff` to see the changes `ruff` makes.
6. Stage the changes and commit again.

### Exercise 1.2 solution

1. Copy and paste `numpydoc-validation` section into `.pre-commit-config.yaml` file.
2. Commit the changes.

### Validating docstrings

1. Run `pre-commit run numpydoc-validation --files example.py`.
2. Copy exercise 1.3 solution into `pyproject.toml` and `example.py`, accordingly.
3. Commit the changes.

### Keeping hooks up-to-date

1. Run `pre-commit autoupdate`.
2. Run `pre-commit run --all-files`.
3. Commit the changes.

## Section 2 demos

### Exercise 2.1 solution

1. Rename the `your_pkg` folder to `filename_validation`.
2. Add a new file to that package called `validate_filename.py`.
3. Copy and paste the contents for later.

### Exercise 2.2 solution

Copy and paste the solution into `cli.py` and import the function from the previous exercise.

### Exercise 2.3 solution

1. Replace the placeholder contents in `pyproject.toml` with the example solution.
2. Run `pip install .`.
3. Confirm that the script is available by running `validate-filename --help`.
4. Run `validate-filename x.py` to show how it will be used.

### Exercise 2.4 solution

1. Create `.pre-commit-hooks.yaml`.
2. Copy and paste the solution there.

### Test the hook

1. Commit the changes if not already done so.
2. Create a new file that has a name that is too short: `touch x.py`.
3. `pre-commit try-repo .  --files x.py`
