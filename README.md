# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/edx/token-utils/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                               |    Stmts |     Miss |   Branch |   BrPart |   Cover |   Missing |
|----------------------------------- | -------: | -------: | -------: | -------: | ------: | --------: |
| token\_utils/\_\_init\_\_.py       |        2 |        0 |        0 |        0 |    100% |           |
| token\_utils/api.py                |        6 |        0 |        0 |        0 |    100% |           |
| token\_utils/apps.py               |        3 |        0 |        0 |        0 |    100% |           |
| token\_utils/models.py             |        0 |        0 |        0 |        0 |    100% |           |
| token\_utils/sign.py               |       18 |        0 |        0 |        0 |    100% |           |
| token\_utils/tests/test\_sign.py   |       39 |        0 |        0 |        0 |    100% |           |
| token\_utils/tests/test\_unpack.py |       59 |        0 |        0 |        0 |    100% |           |
| token\_utils/unpack.py             |       21 |        0 |        8 |        0 |    100% |           |
| token\_utils/urls.py               |        3 |        3 |        0 |        0 |      0% |       4-7 |
|                          **TOTAL** |  **151** |    **3** |    **8** |    **0** | **98%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/edx/token-utils/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/edx/token-utils/blob/python-coverage-comment-action-data/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/edx/token-utils/python-coverage-comment-action-data/endpoint.json)](https://htmlpreview.github.io/?https://github.com/edx/token-utils/blob/python-coverage-comment-action-data/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2Fedx%2Ftoken-utils%2Fpython-coverage-comment-action-data%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/edx/token-utils/blob/python-coverage-comment-action-data/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.