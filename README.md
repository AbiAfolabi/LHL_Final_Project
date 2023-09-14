# Final-Project-Statistical-Modelling-with-Python

## Project/Goals

The goals of this project is to showcase and reinforce my learnings in the areas of:

1. Accessing data from website using APIs. 

2. Cleaning and transforming data retrieved via API using Python.

3. Performing EDA using visualizations.

4. Perform sentiment analysis on customer reviews to support business growth.



## Process

Step 1. Data Gathering

a) Data retrieval from Outscraper (https://app.outscraper.com/profile) 

- Retrieved a total of 10,195 rows and 32 columns of data.

- Imported data into pandas dataframe.
 

b) Data retrieval from Yelp (https://docs.developer.yelp.com/reference/v3_business_search & https://docs.developer.yelp.com/reference/v3_business_reviews)

- Retrieved a total of 40 rows and 6 columns of data.

- Imported data into pandas dataframe.

Note: There is a limit of 3 reviews excerps per business on Yelp website


Step 2. Data Cleaning 

- Cleaned data (removed duplicates, removed unnecessary columns, removed rows of data without text reviews etc)

- Renamed column headers to match in all dataframes.

- Merged the dataframes into a single one.



Step 3. Exploratory Data Analysis (EDA)

Performed EDA and visuals to see relationships between the dataset features.


Step 4. Perform Sentiment Analysis.

I used 3 methods: 
a) manual labelling of 10% of data which was used to create a model (Naive Bayes) to make predictions of sentiment on the remaining data.
b) sentiment analysis using VADER.
c) sentiment analysis using BERT model.


Step 5. Review of Results & Conclusion

## Results

- Calgary has the highest number stores.

- Edmonton has the highest number of customer reviews.

- Best and worst review ratings came from Calgary.

- VADER classified some negative and positive reviews as neutral.

- Naive Bayes and BERT models performed better in classifying text reviews.


 
## Challenges 

Time was a major constraint:

- Automating the process of retrieving data from Yelp was impossible because only 3 reviews download is permitted.

- Merging and cleaning of data from different sources and formats was demanding in terms of time, effort and quality_checks performed.

- Manual labelling of 10% of the data required reading through the reviews and assigning positve or negative sentiments.

- Download and applying BERT model to perform sentiment analysis failed in Jupyter notebook and VSCode and took a long time to figure out a workaround.


## Future Goals

- Some reviews from a single customer were long and contains both positive and negative comments, so I will separate reviews into short sentences (or meaningful phrases) and perform sentiment analysis them.

- Develop an App that will highlight negative reviews to business owners and suggest damage control options. 

- Improve review rating system to give suggestions on appropriate rating to customers based on text input.


