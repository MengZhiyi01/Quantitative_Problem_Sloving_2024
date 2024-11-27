# phbs-qps-2024

## Introduction
This is Homework 1 of the PHBS Quantitative Problem Solving 2024, undertaken by **xl_Hao**.

[Github repository link](https://github.com/MengZhiyi01/Quantitative_Problem_Sloving_2024.git)

## Quick Start
1. Python 3.10.13

2. Install dependencies.
- pandas==2.2.3
- pandas_datareader==0.10.0

You can configure a new virtual environment (named 'qps') by entering the following commands in the terminal:
```shell
conda create -n qps python=3.10.13
conda activate qps

pip install pandas_datareader==0.10.0
pip install pandas==2.2.3
```

3. Run scripts/calculation.py

You can run the scripts *from the project root directory in the terminal*.
```shell
conda activate qps

cd /path/to/project_root #[your root to this project]

python -m scripts.calculation 
'''
This will print out The last 4 & all quarters of inflation
(in my setting is from 2015Q2) seperately.
'''
```

4. All the processed data will be save in <code>data</code>, and **the last 4 quarters of inflation** will be printed out.

## Dataset
The downloaded CPI data is from Federal Reserve Economic Data (FRED) through pandas datareader

- [FRED link](https://fred.stlouisfed.org/series/CPILFESL)

- [Pandas_datareader link](https://pydata.github.io/pandas-datareader/stable/index.html)