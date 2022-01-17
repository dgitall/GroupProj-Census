# Census API Data – Annual Business Survey 2019

## Contributors
Darrell Gerber, Grace Seiler, Pemba Sherpa, Amy Yucus

## Motivation
This project was created as an assessment for the Python Basics module of Genesis10's Dev10 program - Data Professional track.
We are exploring the Census Bureau's Annual Business Survey Technology Characteristics of Businesses API.

Questions posed: 
* What firms already have high acceptance of AI (use is high)? 
* Does AI technology use affect the number of workers, worker skill level, and STEM skills of workers?  
* What is the motivation behind firms using AI (specifically firms who report high use)?
* What is the main factor that adversely affects the adoption or utilization of AI (besides not applicable and no factors affected)? 
 
## Data Sources
* Data provider 1: Census Bureau - https://api.census.gov/data.html
	* Specific dataset: Annual Business Survey (ABS) APIs for 2019: https://www.census.gov/data/developers/data-sets/abs.2019.html
	* Get an API key: https://www.census.gov/data/developers/guidance/api-user-guide.Help_&_Contact_Us.html
* Data provider 2: census-regions - https://github.com/cphalpert/census-regions


## Pulling and Transforming
The explained process steps for pulling and transforming the data can be found in Assessment-ETL-Report.docx
1.
2.
3. Data can be pulled and transformed to answer this question using the file: motivation-technology.ipynb
	* The output csv files from the pulling and tranforming are in the Data folder: 
		* motivation_by_industry.csv
		* motivation_by_state.csv
		* motivation_by_size.csv
4. technology_factors.ipynb is the main file that etracts, transforms and creates bar chart visualization. It also creates state_data.csv file which is read by technology_factors_state-map.ipynb to create heat map visualization.  

## Analyzing and Visualizing
1.
2.
3. The code to analyze and visualize the data to answer this question is found in the file: motivation-technology-analysis.py
	* The output png images of the visualizations produced from running this code are in the Visualizations folder:
		* motivation_delaware.png
		* motivation_information_firm.png
		* motivation_large_firm.png
4. technology_factors.ipynb and technology_factors_state-map.ipynb are two files that creates visualization for this section. 
	* The output png images of the visualizations produced from running this code are in the Visualizations folder:
		*ps1.png
		*ps2.png
		*ps3.png

## Conclusions
The final report is named Assessment-Project-Report.docx

## Required Modules
json, requests, pandas, geopandas, matplotlib, palettable