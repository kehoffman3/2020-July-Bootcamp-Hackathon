import pandas as pd

df_covid = pd.read_csv('owid-covid-data.csv')

name_filter = (df_covid['location'] == 'China') | (df_covid['location'] == 'South Korea') | (df_covid['location'] == 'United States') | (df_covid['location'] == 'United Kingdom') | (df_covid['location'] == 'World')

df_covid = df_covid[name_filter]

print(df_covid.iloc[193:198,:10])

import matplotlib.pyplot as plt

xcord = df_covid.date[0:193]
print(xcord)

yChina = df_covid.total_cases_per_million[0:193]
ySthKor = df_covid.total_cases_per_million[193:386]
yUSA = df_covid.total_cases_per_million[386:579]
yUK = df_covid.total_cases_per_million[579:772]
yWorld = df_covid.total_cases_per_million[772:965]
print(yChina)
print(ySthKor)
print(yUSA)
print(yUK)
print(yWorld)

plt.plot(xcord, yChina)
plt.plot(xcord, ySthKor)
plt.plot(xcord, yUSA)
plt.plot(xcord, yUK)
plt.plot(xcord, yWorld)
