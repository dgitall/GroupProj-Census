import requests
import pandas as pd
import config
import matplotlib.pyplot as plt
from pprintpp import pprint as pp
from plotnine import ggplot, aes, geom_bar, coord_flip, xlab, ylab, ggtitle


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
pp(df.head(10))
pp(df.columns)

# plot a bargraph of employess by gender of company
gender = df[['EMP', 'SEX_LABEL']]
gender['EMP'] = pd.to_numeric(gender['EMP'])/100000

ax = gender.plot(title="Total Count of US Business Employment (by business predominant gender)", 
                 kind='barh', 
                 x='SEX_LABEL')
ax.set_xlabel('Employees (100,000)')
ax.set_ylabel('Business Predominant Gender')

genderEmp = df[['FIRMPDEMP', 'SEX_LABEL']]
genderEmp['FIRMPDEMP'] = pd.to_numeric(genderEmp['FIRMPDEMP'])/100000
print(genderEmp.head())
ax1 = genderEmp.plot(title="Total Count of US Businesses (by business predominant gender)",
                 kind='barh',
                 x='SEX_LABEL')
ax1.set_xlabel('Firms (100,000)')
ax1.set_ylabel('Business Predominant Gender')
''' 
g = ggplot(genderEmp ) + \
    aes(y="FIRMPDEMP", x="SEX_LABEL") + \
    geom_bar( stat="identity", fill="lightblue", color="black")
print(g)
plt.show() '''


dataToGet = '?get=NAME,GEO_ID,NAICS2017_LABEL,EMP,FIRMPDEMP,SEX,SEX_LABEL'
regionToGet = '&for=state'
surveyToGet = ':*&NAICS2017=00'
queryURL = baseURL+dataToGet+regionToGet+surveyToGet+'&key='+config.personalKey
response = requests.get(queryURL)
#print(response.text)

df2 = pd.read_json(response.text)
df2.columns = df2.iloc[0]
df2.drop(index=0, inplace=True)
pp(df2.shape)
pp(df2.head(10))
pp(df2.columns)

genderst = df2[['NAME', 'EMP', 'SEX_LABEL']]
genderst['EMP'] = pd.to_numeric(genderst['EMP'])/100000
genderst.index = genderst['NAME']
genderst.index.names=[None]
pp(genderst)
genderstpivot = genderst.pivot(index='SEX_LABEL', columns='NAME')
pp(genderstpivot.shape)
pp(genderstpivot)
pp(genderstpivot.columns)
'''genderstpivot = genderstpivot.columns.reset_index(level=0)
pp(genderstpivot.shape)
pp(genderstpivot)
pp(genderstpivot.columns)
genderstpivot.drop(index=0, inplace=True)
genderstpivot.drop(index=0, inplace=True)
genderst.index.names=[None] 
'''
genderstremelt = genderstpivot.melt()
pp(genderstremelt)
# NEed to tack on the SEX_LABEL column again from the original
''' genderstremelt.index.name = [None]
genderstremelt.reset_index(inplace=True)

pp(genderstremelt)
genderstremelt['SEX_LABEL'] = genderst['SEX_LABEL'] '''


pp(genderstremelt) 
genderstmelt = genderst.melt(id_vars='NAME')
pp(genderstmelt.shape)
pp(genderstmelt)
pp(genderstmelt.columns)

g = ggplot(genderstremelt) + \
    aes(x="NAME", y="value") + \
    geom_bar(stat="identity", fill="lightblue", color="black") + \
    xlab("") + ylab("Employees by Business (proportion by business gender type)") + \
    coord_flip() + ggtitle("Total Count of Business Employment (by business predominant gender and state)")
print(g) 
''' g = ggplot(genderstmelt) + \
    aes(y="value", x="NAME") + \
    geom_bar(stat="identity", color="black")
print(g) '''
plt.show()
