# phbs-qps-2024

## Introduction
This is Homework 1 of the PHBS Quantitative Problem Solving 2024, undertaken by **Zhiyi_Meng**.

[Github repository link](https://github.com/MengZhiyi01/Quantitative_Problem_Sloving_2024.git)

## Quick Start
1. Python 3.10.13

2. Install dependencies.
- pandas==2.2.3
- pandas_datareader==0.10.0

3. Run scripts/calculation.py

You can run the scripts *from the project root directory in the terminal*.
```shell
conda activate -your_enviroment_name

cd /path/to/project_root #[your root to phbs-qps-2024]

python -m scripts.calculation
```

4. All the processed data will be save in <code> data</code>, and **the last 4 quarters of inflation** will be printed out.

## Dataset
The downloaded CPI data is from Federal Reserve Economic Data (FRED) through pandas datareader

- [FRED link](https://fred.stlouisfed.org/series/CPILFESL)

- [Pandas_datareader link](https://pydata.github.io/pandas-datareader/stable/index.html)