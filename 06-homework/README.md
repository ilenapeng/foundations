# 06-homework: pandas

[Part 1: Beer](https://github.com/ilenapeng/foundations/tree/main/06-homework/part1-beer)
  * [pandas-beer-cans.ipynb](https://github.com/ilenapeng/foundations/blob/main/06-homework/part1-beer/pandas-beer-cans.ipynb)
  * More work with strings - .replace for entire cells vs .str.replace for PARTS of cells
  * And alo more work with NA values - .isnull() or .notnull() followed by .value_counts() to see number of missing values
  * Data from [craftcans.csv](https://github.com/ilenapeng/foundations/blob/main/06-homework/part1-beer/craftcans.csv)

[Part 2: Dogs](https://github.com/ilenapeng/foundations/tree/main/06-homework/part2-dogs)
  * [pandas-dogs.ipynb](https://github.com/ilenapeng/foundations/blob/main/06-homework/part2-dogs/pandas-dogs.ipynb)
  * [NYC pet licensing data via Muckrock](https://github.com/ilenapeng/foundations/blob/main/06-homework/part2-dogs/NYC_Dog_Licenses_Current_as_of_4-28-2016.xlsx)
  * Merging data with [zipcodes-neighborhoods.csv](https://github.com/ilenapeng/foundations/blob/main/06-homework/part2-dogs/zipcodes-neighborhoods.csv) and on [boro_population.csv](https://github.com/ilenapeng/foundations/blob/main/06-homework/part2-dogs/boro_population.csv)
  * .value_counts().groupby(level=0).head(1) or .value_counts().groupby(level=0, group_keys=False).nlargest(1) to get the largest in each group
  * .crosstab(column1, column2) OR .pivot_table(index='column1',columns='column2',aggfunc='size') returns the total number of each column 2 value in each group of column 1. 
      * For .crosstab: Adding normalize='index' will give you percent of each group, normalize='true' will give you percent of the total
  * Making a new column based on values of three other columns
