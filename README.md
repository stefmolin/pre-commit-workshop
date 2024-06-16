# Pre-Commit Workshop
[![View slides in browser](https://img.shields.io/badge/view-slides-orange?logo=reveal.js&logoColor=white)](https://stefaniemolin.com/pre-commit-workshop/) [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

## Abstract

Maintaining code quality can be challenging, no matter the size of your project or number of contributors. Different team members may have different opinions on code styling and preferences for code structure, while solo contributors might find themselves spending a considerable amount of time making sure the code conforms to accepted conventions. However, manually inspecting and fixing issues in files is both tedious and error-prone. As such, computers are much more suited to this task than humans. Pre-commit hooks are a great way to have a computer handle this for you.

Pre-commit hooks are code checks that run whenever you attempt to commit your changes with `git`. They can detect and, in some cases, automatically correct code-quality issues *before* they make it to your code base. In this tutorial, you will learn how to install and configure pre-commit hooks for your repository to ensure that only code that passes your checks makes it into your code base. We will also explore how to build custom pre-commit hooks for novel use cases.

## About the Author

[Stefanie Molin](https://stefaniemolin.com) ([@stefmolin](https://github.com/stefmolin)) is a software engineer at Bloomberg in New York City, where she tackles tough problems in information security, particularly those revolving around data wrangling/visualization, building tools for gathering data, and knowledge sharing. She is also a core developer of [numpydoc](https://github.com/numpy/numpydoc) and the author of [Hands-On Data Analysis with Pandas](https://www.amazon.com/dp/1800563450/), which is currently in its second edition and has been translated into Korean and Chinese. She holds a bachelor’s of science degree in operations research from Columbia University's Fu Foundation School of Engineering and Applied Science, as well as a master’s degree in computer science, with a specialization in machine learning, from Georgia Tech. In her free time, she enjoys traveling the world, inventing new recipes, and learning new languages spoken among both people and computers.

## License

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
