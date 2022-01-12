import requests
import pandas as pd
import config
import matplotlib.pyplot as plt


baseURL = 'https://api.census.gov/data/2018/abscs'
dataToGet = '?get=NAME,GEO_ID,NAICS2017_LABEL,EMP,FIRMPDEMP,SEX,SEX_LABEL'
regionToGet = '&for=us'
surveyToGet = ':*&NAICS2017=00'
queryURL = baseURL+dataToGet+regionToGet+surveyToGet+'&key='+config.personalKey 
response = requests.get(queryURL)
#print(response.text)

df = pd.read_json(response.text)
df.columns = df.iloc[0]
df.drop(index=0, inplace=True)


# plot a bargraph
gender = df[['EMP', 'SEX_LABEL']]
gender['EMP'] = pd.to_numeric(gender['EMP'])/100000

ax = gender.plot(title="Total Count of US Business Employment (by business predominant gender)", 
                 kind='barh', 
                 x='SEX_LABEL')
ax.set_xlabel('Employees (100,000)')
ax.set_ylabel('Business Predominant Gender')

plt.show()
