# After Action Report on Interview Challenge

## Summary (tl,dr)
This was a good challenge to help me better understand where my strengths and weaknesses are as a AI/ML engineer. I some areas that I need to improve on, however, in a real-world scenario I believe it is equally important to have the ability to leverage the technologies available. I understand that this can't be a crutch as will take this lesson and improve.

## Sustainments
1. The tasks were not to easy, but not too hard.
2. The tasks allowed me to identify gaps in my knowledge
3. I was able to update sections of my personal wiki

## Improvements
1. More reps. with pandas and matplotlib
2. Challenge myself in the future to rely on AI less
3. Workstation / Environment preparation, automations, and scripts.

## Special Thanks!
I want to take a moment of thanks and appreciation for the oppertunity and experience. This was both humbling and rewarding. I look forward to growing as a result of this experience. Thank you!

## References
https://www.geeksforgeeks.org/python/python-pandas-timestamp-isoformat/
https://www.geeksforgeeks.org/python/python-pandas-to_datetime/
https://www.geeksforgeeks.org/pandas/how-to-break-up-a-comma-separated-string-in-pandas-column/
https://www.geeksforgeeks.org/python/count-the-number-of-rows-and-columns-of-a-pandas-dataframe/
https://www.geeksforgeeks.org/python/apply-a-function-to-each-row-or-column-in-dataframe-using-pandas-apply/
https://pandas.pydata.org/docs/getting_started/intro_tutorials/05_add_columns.html
https://stackoverflow.com/questions/46218652/python-pandas-unique-value-ignoring-nan
https://www.statology.org/pandas-unique-ignore-nan/
https://www.geeksforgeeks.org/python/python-pandas-index-value_counts/
https://www.analyticsvidhya.com/blog/2024/02/matplotlib-pyplot-hist-in-python/
https://www.geeksforgeeks.org/pandas/bar-plot-in-matplotlib/
https://www.geeksforgeeks.org/python/python-pandas-dataframe-mean/
https://www.w3schools.com/python/pandas/ref_df_idxmax.asp
https://www.w3schools.com/python/pandas/ref_df_max.asp

I also utilized SANS SEC 595 Lab matterial, however, I can't reference that.

---
# Challenge: Ancient Tree Inventory (ATI) Extract, Transform, & Analyze

## Instructions

This coding challenge is meant to evaluate how a software engineer specializing in data collection and processing approaches a problem and works through it. You must use Python, but can otherwise utilize any resources you would normally use to do your job (Google, Stack Overflow, documentation, etc.). The only disallowed action is looking up the exact problem and copy/pasting a solution that you did not write yourself (such as using AI/LLM-generated solutions). The challenge is intended to span ~60 minutes, and the focus is not on whether you have a complete working solution in the time period, but instead on how you worked through the problem.

### Requirements

* Python

### Data

The data for this challenge is a collection of ancient trees located in the United Kingdom, and was retrieved from the Woodland Trust Open Data Portal here [https://opendata-woodlandtrust.hub.arcgis.com/datasets/9d2d13b04d654ceb9ba6e0697c1e0c29_0/explore](https://opendata-woodlandtrust.hub.arcgis.com/datasets/9d2d13b04d654ceb9ba6e0697c1e0c29_0/explore).

The dataset is provided in `.csv`, `sqlite`, and `.geojson` formats, but all three options contain the same data, so you can use the option of your choosing for the challenge.

## Challenge

### Part I

Part I of this challenge focuses on ingestion, processing, and enrichment of the provided data using Python. 

1. Ingest the ATI data into Python objects using whichever data format you prefer.
2. Output the following key metrics about the data:
   * Count/size
   * Number of fields
3. Normalize the following data:
   * Convert any of the date/time fields to ISO 8601 format (`YYYY-MM-DDThh:mm:ss`).
   * Convert any of the fields with comma-separated values to lists of values.
   * Create a new column with a boolean value for whether the tree is accessible to the public or not.

### Part II

Part II of this challenge focuses on analysis of the provided data using Python.

1. Output a list of all *unique* ancient tree species. 
2. Create a histogram (or count by value) showing the number of ancient trees per county.
3. Output what percentage of ancient trees are both alive *and* standing.
4. Determine which species of tree has the largest average girth.

### Part III

Part III of this challenge focuses on web scraping and insight gathering using Python.

1. Scrape the Woodland Trust web page where they have an A-Z list of British trees here [https://www.woodlandtrust.org.uk/trees-woods-and-wildlife/british-trees/a-z-of-british-trees/](https://www.woodlandtrust.org.uk/trees-woods-and-wildlife/british-trees/a-z-of-british-trees/) and extract the list of tree names and the direct links to the individual page for each tree.
2. Normalize the list of tree names (remove modifiers/types specified after a comma).
3. Use the above normalized list of tree names to determine which tree species *also* show up in the ancient tree database.
