# Data Science Salary Estimator: Project Overview

- Created a tool that estimates data science salaries (MAE ~ $ 14K) to help data scientists negotiate their income when they get a job

- Scraped over 700 job descriptions from glassdoor using python and selenium

- Engineered features from the text of each job description to quantify the value companies put on python, R,	excel,	sql,	spark,	tableau,	aws and	hadoop

- Used Linear, Ridge, Lasso, Support Vector and Random Forest Regressors to reach the best model.

- Built a client facing API using flask

## Code and Resources Used
Project done by viewing "Data Science Project From Scratch" by Ken Jee on Youtube

https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t

Python Version: 3.7

Packages: pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle

For Web Framework Requirements: pip install -r requirements.txt

Scraper Github: https://github.com/arapfaik/scraping-glassdoor-selenium

Scraper Article: https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905

Flask Productionization: https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2

## Web Scraping

Tweaked the web scraper github repo (above) to scrape 700 job postings from glassdoor.com. With each job, got the following:

- Job title
- Salary Estimate
- Job Description
- Rating
- Company
- Location
- Company Headquarters
- Company Size
- Company Founded Date
- Type of Ownership
- Industry
- Sector
- Revenue
- Competitors

## Data Cleaning

After scraping the data, cleaned it  up so that it was usable for model building. Made the following changes and created the following variables:

- Parsed numeric data out of salary

- Made columns for employer provided salary and hourly wages

- Removed rows without salary

- Parsed rating out of company text

- Transformed founded date into age of company

- Made columns for different skills which were listed in the job description:

   - python
   - R
   - excel
   - sql
   - spark 
   - tableau
   - aws 
   - hadoop
 
- Column for simplified job title and Seniority
 
- Column for description length

## EDA
Looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables.

![](/images/wordcloud%20of%20job%20description.png)

![](/images/salary%20by%20job%20title.png)
![](/images/job%20opportunities%20by%20state.png)
![](/images/correlation.png)

## Model Building
First, transformed the categorical variables into dummy variables. Also split the data into train and tests sets with a test size of 10%.

Tried five different models and evaluated them using Mean Absolute Error. Chose MAE because it is relatively easy to interpret and also as the outliers aren’t particularly bad in for this type of model.

Multiple Linear Regression – Baseline for the model

Ridge regression

Lasso Regression – Because of the sparse data from the many categorical variables, thought a normalized regression like lasso would be effective.

Support vector regression- Which did not give good values comaparitively

Random Forest – Again, with the sparsity associated with the data, thought that this would be a good fit.

## Model Performance

The Random Forest model outperformed the other approaches on the test and validation sets.

- Random Forest : MAE = 14.97

- Linear Regression: MAE = 17.99

## Productionization

In this step, built a flask API endpoint that was hosted on a local webserver by following along with the TDS tutorial in the reference section above. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary.
