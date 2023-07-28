# 🐼 in 🐍
       ____   _    _   _ ____    _    ____  
      |  _ \ / \  | \ | |  _ \  / \  / ___|
      | |_) / _ \ |  \| | | | |/ _ \ \___ \
      |  __/ ___ \| |\  | |_| / ___ \ ___) |
      |_| /_/   \_\_| \_|____/_/   \_\____/

[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)

# Pandas Library Guide

This repository is dedicated to the pandas library in Python. It provides in-depth guides, tutorials, links, and resources to help you learn and use pandas effectively.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Script](#script)
- [Guides](#guides)
- [Tutorials](#tutorials)
- [Sample Data](#sample-data)
- [Contributing](#contributing)
- [Resources](#resources)

## Introduction
Pandas is a powerful open-source data manipulation and analysis library for Python. It provides easy-to-use data structures and data analysis tools, making it a popular choice for data scientists and analysts.

## Installation
To install pandas, you can use pip, the Python package installer. Open your terminal or command prompt and run the following command:

```
pip install pandas
```

## Getting Started
To start using pandas, you need to import it in your Python script:

```python
import pandas as pd
```

## Script
Use `python_script.py` to accelerate your understanding of pandas.

#### How To Use?

download script

then...
```
python python_script.py
```
#### OR

Run blocks of code individually

such as...
```
# Example: Merge two dataframes based on a common column
df1 = pd.DataFrame({'column_name': [1, 2, 3], 'another_column': ['A', 'B', 'C']})
df2 = pd.DataFrame({'column_name': [2, 3, 4], 'additional_column': ['X', 'Y', 'Z']})
merged_df = pd.merge(df1, df2, on='column_name')
print(merged_df)
```

## Guides
- [Pandas Documentation](https://pandas.pydata.org/docs/) - Official documentation for pandas.
- [10 Minutes to pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html) - A quick introduction to pandas.
- [Pandas User Guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html) - Comprehensive user guide for pandas.

## Tutorials
- [Pandas Tutorial](https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python) - A comprehensive tutorial on pandas dataframes.
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf) - A handy cheat sheet for pandas operations.
- [Rob Mulla](https://www.youtube.com/channel/UCxladMszXan-jfgzyeIMyvw) - The Best Python-Data Youtuber

## Sample Data
This repository includes a sample dataset (`df`) within `python_script.py` that you can use to practice pandas functions and tasks.

## Contributing
Contributions to this repository are welcome. If you have any guides, tutorials, or resources related to pandas, feel free to submit a pull request.

## Resources
- [Pandas GitHub Repository](https://github.com/pandas-dev/pandas) - Official GitHub repository for pandas.
- [Pandas User Discussion Group](https://groups.google.com/g/pandas-users) - A community forum for pandas users.
- [Pandas Stack Overflow](https://stackoverflow.com/questions/tagged/pandas) - Questions and answers related to pandas on Stack Overflow.

🐼 Happy coding with pandas! 🐼
