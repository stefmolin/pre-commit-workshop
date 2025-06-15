# Demos

Run the demos in VS Code for the combined view of the file contents and the terminal.

## Setup

1. Increase VS Code font size beforehand:

    1. Open settings.
    2. Change font size to 24 (original is 12).
    3. Search for `terminal.integrated.font-size` and change it to 24 as well (original is 12).

3. Change `workbench.color.theme` to `Light High Contrast` (default `Dark Modern`).

4. Create a fresh virtual environment:

    ```shell
    $ conda create --name pre-commit-demo python=3.12
    $ conda activate pre-commit-demo
    ```

5. Disable Copilot completions by clicking the icon in the bottom right of VS Code.

6. Save a PDF copy of the slides to distribute as needed:

   ```shell
   $ curl -OJ https://stefaniemolin.com/pre-commit-workshop/slides.pdf
   ```

## Section 1 demos

### Git hooks demo

1. Branch off of `main` (name it after the event).
2. Run `tree .git/hooks` and discuss output.
3. Run `less .git/hooks/pre-commit.sample` and discuss output.
4. Create a version of the file that will get run: `cp .git/hooks/pre-commit.sample .git/hooks/pre-commit`.
5. Edit the `.git/hooks/pre-commit` file to have `exit 1` near the top (automatic failure).
6. Attempt to commit the slides PDF to this branch. Discuss why it failed.
7. Run `rm .git/hooks/pre-commit` to get rid of the automatic failure hook.
8. Attempt the commit again. Discuss why it succeeds.
9. Push the changes up so the PDF version of the slides is available for everyone.

### Pre-commit package installation

1. With a pre-made virtual environment activated, run `python3 -m pip install pre-commit`.
2. Run `pre-commit --version` to show it worked.

### Install first set of hooks

1. Show that `pre-commit sample-config` can be used to see what an example looks like, but mention that the version is outdated, and the contents are different than what we will use.
2. Create `.pre-commit-config.yaml` file copying the contents from the slides.
3. Run `pre-commit install`.
4. Run `less .git/hooks/pre-commit` and show that the contents are now coming from `pre-commit` and referencing the `.pre-commit-config.yaml` file.
5. Commit the `.pre-commit-config.yaml` file.

### Adding `ruff`

1. Copy `ruff` section from slides into `.pre-commit-config.yaml` file.
2. Commit the changes.
3. Create `example.py` file with issues for `ruff` to find (copying from slides and saving with `cmd+K` then `S` or `cmd+shift+P` &rarr; `File: Save without Formatting`).
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

1. Rename the `custom_hook` folder to `filename_validation`.
2. Rename the `check.py` file to `validate_filename.py`.
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
