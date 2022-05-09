import csv
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

covid_filepath="/UJEP Informatika/Dama_seminarka/MSW_semin-rn-_pr-ce/COVID-19 Coronavirus.csv"
covid_data=pd.read_csv(covid_filepath,nrows=6)

sns.relplot(data=covid_data,x="Country",y="Population",hue="Continent").set(title="počet lidí v prních 6 státech")    #takto malý počet kvůli přehlednosti v grafu
plt.show()
print("\n")

covid_data=pd.read_csv(covid_filepath,nrows=20)
sns.relplot(data=covid_data,x="Total Cases",y="Death percentage",hue="Country").set(title="Procento smrtí na celkový počet nakažených Covidem, dle prvních 20 zemí")
plt.show()
print("\n")

covid_data=pd.read_csv(covid_filepath)
sns.histplot(data=covid_data,y="Continent").set(title="Kolik zemí z každého kontinentu se průzkumu účastnilo")    #na y, kvůli přehlednosti grafu
plt.show()
print("\n")

covid_data=pd.read_csv(covid_filepath,nrows=6)
sns.lineplot(data=covid_data,x="Country",y="Death percentage").set(title="Procento úmrtí na Covid v prních 6 státech")
plt.show()
print("n")

sns.lineplot(data=covid_data,x="Country",y="Total Deaths").set(title="Počet smrtí v prních 6 státech")
plt.show()
print("\n")