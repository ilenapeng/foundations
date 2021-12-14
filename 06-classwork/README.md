# 06-classwork: pandas

[pandas-neiss.ipynb](https://github.com/ilenapeng/foundations/blob/main/06-classwork/pandas-neiss.ipynb)
* Data from [neiss2017.tsv](https://github.com/ilenapeng/foundations/blob/main/06-classwork/neiss2017.tsv)
* Working with NA values: Reading in files with na_values, using .dropna(), numpy df['column'].replace({'oldname': 'newname'})
* .value_counts(normalize=True) for percentages df.info() vs df.dtypes()
* pd.set_option()
* .str.contains() and .str.replace() with words and with regex
* .isin(['a', 'b', 'c']) to search for multiple strings
* .merge()
    * Combined csv with [neiss_products.txt](https://github.com/ilenapeng/foundations/blob/main/06-classwork/neiss_products.txt)
