# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 16:08:57 2023

@author: Cláudia
"""
################
#GRUPO 23
#Cláudia Silva al70759
###############1###############
import pandas as pd

# load do ficheiro #path relativo do csv
le = pd.read_csv('Life-Expectancy-Data-Updated.csv')


# filtra as colunas que tem a palavra south america
south_america_df = le[le['Region'].str.contains('South America')]

# da export para um csv novo #ver na diretoria do utilizador
south_america_df.to_csv('South_America.csv')


###############2###############

#data frame dos 4 paises
countries_df=south_america_df[south_america_df['Country'].str.contains('Argentina') | south_america_df['Country'].str.contains('Brazil') | south_america_df['Country'].str.contains('Chile') | south_america_df['Country'].str.contains('Uruguay')]

import matplotlib.pyplot as plt
 
pontos_df = countries_df.pivot(index='Year', columns='Country', values='Under_five_deaths')

# grafico
pontos_df.plot(kind='line')

# titulos 
plt.title('Under-five-deaths per 1000 population')
plt.xlabel('Year')
plt.ylabel('Under-five deaths per 1000 population')

# mostrar o grafico
plt.show()

###############3###############                                                                                                                            ESCREVI MAL ECUADOR , ESCREVI EM PORTUGUES EQUADOR
years=range(2000,2016)
countries2_df=south_america_df[south_america_df['Country'].str.contains('Bolivia') | south_america_df['Country'].str.contains('Colombia') | south_america_df['Country'].str.contains('Ecuador') | south_america_df['Country'].str.contains('Paraguay') & (south_america_df['Year'].isin(years))]

pontos2_df = countries2_df.pivot(index='Year', columns='Country', values='Population_mln')


#calcular media por 1000
mean_dff= pontos2_df.mean()/1000


#criar o grafico
labels = mean_dff.index
sizes = mean_dff.values
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

# titulos
plt.title('Population Distribution of Bolivia, Colombia, Ecuador, and Paraguay')

# print do grafico
plt.axis('equal')
plt.show()

###############4###############


def max_life_expectancy_by_country(country_name):
    
     
    expectancy_df = pd.read_csv('Life-Expectancy-Data-Updated.csv')

    # regiao e pais
    rexpectancy_df = expectancy_df[(expectancy_df['Region'] == 'South America') & (expectancy_df['Country'] == country_name)]

    #encontra a linha com a maior esperança de vida
    max_row = rexpectancy_df.loc[rexpectancy_df['Life_expectancy'].idxmax()]

    #anos e valor
    year = max_row['Year']
    value = max_row['Life_expectancy']

    
    return year, value

#escolha do país e print 
country_name = input('Enter a South American country, example(Brazil): ')
year, value = max_life_expectancy_by_country(country_name)
print(f'The highest life expectancy in {country_name} was in {year}, with {value}')


###############5###############


import seaborn as sns


expectancy_df = pd.read_csv('Life-Expectancy-Data-Updated.csv')

#escolha das colunas
rexpectancy_df = expectancy_df.dropna(subset=['Incidents_HIV', 'Life_expectancy'])

#criar o grafico de despersao da expectativa de vida com uma regressao linear dos incidentes de hiv
sns.lmplot(x='Incidents_HIV', y='Life_expectancy', data=rexpectancy_df, line_kws={'color': 'red'})

#grafico
plt.show()
 
#conclusao geral
print('As you can see as the number of HIV incidents grow the life expectancy lowers')


###############6###############






