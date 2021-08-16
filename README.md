# Surf's Up - Berkeley DA
Yae Jin Park\
Module 9 - Surf's Up with Advanced Data Storage and Removal

## Assignment Overview
Since setting up an SQL database for every analysis is inefficient, people use SQLite in order to perform analysis on simple sets of data. In this module, datasets of Oahu's temperature and precipitation throughout seven years is provided for analysis and analysis on June and December temperatures are requested. The process is done utilizing Jupyter Notebook, SQLite, and Python.

## Results and Summary

### Temperature Analysis Result

The following are the statistical summaries for June and December temperatures of the data set, respectively:

![June Summary](https://github.com/yaejinpark/surfs-up/blob/main/resources/june_summary.png)

![December Summary](https://github.com/yaejinpark/surfs-up/blob/main/resources/dec_summary.png)

The three key differences between June and December temperatures are:
* Lower minimum temperature in December
* Higher standard deviation of temperature in December
* Overall lower temperatures in the Q1, Q2 and Q3 for December

Though these differences are expected as temperature drops in winter are common, it can be said with higher deviation of temperature data in December, temperature is more likely to fluctuate in (slightly) bigger numbers in December than in June. The minimum temperature of 56 F in December seems like an outlier - maybe it was from an unusually cold winter day in Oahu.

### More Queries and Analysis

More analysis on other parts of provided data can further help this analysis. Two more extra queries have been done for June and December data - this time, they are done on precipitation. Here are the query results and code, respectively:

![June Precipitation Query](https://github.com/yaejinpark/surfs-up/blob/main/resources/june_prcp.png)

![December Precipitation Query](https://github.com/yaejinpark/surfs-up/blob/main/resources/dec_prcp.png)

From glance, there seems to be more differences in precipitation data than there are in temperature data. Let's see if that holds up by looking at both dataframes' statistical summary:

![June PRCP Summary](https://github.com/yaejinpark/surfs-up/blob/main/resources/june_prcp_summary.png)

![December PRCP Summary](https://github.com/yaejinpark/surfs-up/blob/main/resources/dec_prcp_summary.png)

