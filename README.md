# Pre-Commit Workshop
[![View slides in browser](https://img.shields.io/badge/view-slides-orange?logo=reveal.js&logoColor=white)](https://stefaniemolin.com/pre-commit-workshop/) [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

The slides are licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa]. Any code files in this repository are distributed under the Apache-2.0 license.

## Abstract

Maintaining code quality can be challenging, no matter the size of your project or number of contributors. Different team members may have different opinions on code styling and preferences for code structure, while solo contributors might find themselves spending a considerable amount of time making sure the code conforms to accepted conventions. However, manually inspecting and fixing issues in files is both tedious and error-prone. As such, computers are much more suited to this task than humans. Pre-commit hooks are a great way to have a computer handle this for you.

Pre-commit hooks are code checks that run whenever you attempt to commit your changes with `git`. They can detect and, in some cases, automatically correct code-quality issues *before* they make it to your code base. In this tutorial, you will learn how to install and configure pre-commit hooks for your repository to ensure that only code that passes your checks makes it into your code base. We will also explore how to build custom pre-commit hooks for novel use cases.

## Setup Instructions

1. Create a virtual environment using Python 3.10 or higher on your personal laptop, and install `pre-commit` in that virtual environment. You can use the tool of your choice (*e.g.*, `venv`, `conda`, `uv`). For example, you could complete this step using `venv` like so on Linux or MacOS:

    ```shell
    python -m venv venv
    source venv/bin/activate
    python -m pip install pre-commit
    ```

    See https://docs.python.org/3/library/venv.html for more information and the Windows equivalent if you decide to use `venv`.

2. Fork and clone this repository. If you don't have a GitHub account, you will need to create one to complete this step. Please be sure to check for changes (and sync them) before coming to the workshop.

3. Think about some potential ideas for the pre-commit hook you would like to create in the second half of the workshop. Some ideas to get you started: prohibit `print()` calls, enforce file naming conventions, block large files, keep files under a certain number of lines, check for missing docstrings, disallow certain imports, *etc.*


## About the Author

[Stefanie Molin](https://stefaniemolin.com) ([@stefmolin](https://github.com/stefmolin)) is a software engineer at Bloomberg in New York City, where she tackles tough problems in information security, particularly those revolving around data wrangling/visualization, building tools for gathering data, and knowledge sharing. She is also a core developer of [numpydoc](https://github.com/numpy/numpydoc) and the author of [Hands-On Data Analysis with Pandas](https://www.amazon.com/dp/1800563450/), which is currently in its second edition and has been translated into Korean and Chinese. She holds a bachelor’s of science degree in operations research from Columbia University's Fu Foundation School of Engineering and Applied Science, as well as a master’s degree in computer science, with a specialization in machine learning, from Georgia Tech. In her free time, she enjoys traveling the world, inventing new recipes, and learning new languages spoken among both people and computers.

## Licenses

### Code
Any code files in this repository are distributed under the Apache-2.0 license.

### Slides
The slides are licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
