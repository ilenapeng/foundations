# 07-homework:

### [Part 1: Cherry Blossoms](https://github.com/ilenapeng/foundations/tree/main/07-homework/part1-cherry-blossoms)
* [cherry-blossoms.ipynb](https://github.com/ilenapeng/foundations/blob/main/07-homework/part1-cherry-blossoms/cherry-blossoms.ipynb)
* Data from [KyotoFullFlower7.xls](https://github.com/ilenapeng/foundations/blob/main/07-homework/part1-cherry-blossoms/KyotoFullFlower7.xls)
* Using xlrd to import .xls 
* Reading in files with skiprows=n
* Using df.rolling() to calculate a rolling average - .rolling(10, on='AD', min_periods=5) will calculate a 10-year mean using the AD column. If there aren't 20 samples for it to use in calculating the mean, it'll accept a minimum of 5
* pd.to_datetime will fill in missing date information (in this case, years and hours, with other values - which we don't need and so we can ignore)
* dt.strftime - formats a datetime as a string

### [Part 2: 311](https://github.com/ilenapeng/foundations/tree/main/07-homework/part2-311)
* [311.ipynb](https://github.com/ilenapeng/foundations/blob/main/07-homework/part2-311/311.ipynb)
* [Correct answers that we went over the following week](https://github.com/ilenapeng/foundations/blob/main/07-homework/part2-311/311-in-class-review.ipynb)
* Data was a subset from NYC 311 data - not uploaded here because of file size
* in pd.to_datetime, %I is 12-hour clock and %H is 24-hour clock
* .dt.month looks at every single month - so it groups Januaries from every single year, Februaries from every single year and so on
* .resample looks at each month/year combo separately, so January 2020 and January 2019 are separate
* .resample functions as a groupby(), but for datetime values
* More pivot tables: `` df.pivot_table(
    columns='what will show up as your columns',
    index='what will show up as your rows',
    values='the column that will show up in each cell',
    aggfunc='the calculation(s) you want dont'
) ``
