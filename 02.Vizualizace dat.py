import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px

covid_filepath="/UJEP Informatika/Dama_seminarka/MSW_semin-rn-_pr-ce/COVID-19 Coronavirus.csv"
covid_data=pd.read_csv(covid_filepath,nrows=6)

graf=sns.relplot(data=covid_data,x="Country",y="Population",hue="Continent").set(title="                            Velikost populace v prvních 6 státech, se zvýrazněním kontinentu")    #takto malý počet kvůli přehlednosti v grafu
graf.set(xlabel = 'Název státu')
graf.set(ylabel = 'Veilkost populace v desetimilionech')
graf._legend.set_title("Kontinent")                                   #přejmenuje hue
plt.show()
print("\n")

covid_data=pd.read_csv(covid_filepath,nrows=20)
graf=sns.relplot(data=covid_data,x="Total Cases",y="Total Deaths",hue="Country").set(title="Počet smrtí na celkový počet nakažených Covidem, v prvních 20 zemích")
graf.set(xlabel = 'Celkový počet Nakažených')
graf.set(ylabel = 'Celkový počet úmrtí')
graf._legend.set_title("Názvy států")
plt.show()
print("\n")

covid_data=pd.read_csv(covid_filepath)
sns.histplot(data=covid_data,y="Continent").set(title="Kolik zemí z každého kontinentu se průzkumu účastnilo")    #na y, kvůli přehlednosti grafu
plt.xlabel('Počet')
plt.ylabel('Kontinent')
plt.show()
print("\n")


covid_data=pd.read_csv(covid_filepath)
graf=sns.barplot(x =covid_data['Population'][:30], y =covid_data ['Country'][:30], palette = 'dark')
graf.set_xlabel(xlabel = 'Populace ve stamilionech', fontsize = 10)
graf.set_ylabel(ylabel = 'Názvy států', fontsize = 10)
graf.set_title(label = 'Velikost populace v prvních 30 státech', fontsize = 20)
plt.show()
print("\n")

graf = px.choropleth(covid_data, locations="Country", 
                    locationmode='country names', color="Death percentage", 
                    hover_name="Country", range_color=[1,5],        #dle toho, jak to chci moc barevné
                    color_continuous_scale="blues", 
                    title='Procenta úmrtí na Covid')
graf.update(layout_coloraxis_showscale=True)
graf.show()