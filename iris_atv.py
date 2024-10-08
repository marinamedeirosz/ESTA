import scipy.stats
import statistics as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math

IRIS = pd.read_csv('./dados/iris.csv')
SPECIES = pd.unique(IRIS['Species']).tolist()

def line():
    print('---------------------------------------------------------------------------------------------------------------------')

def get_species_data(your_species):
    species_data = pd.DataFrame(IRIS.loc[IRIS['Species'] == SPECIES[your_species]])
    return species_data

# Função Questão 1 - Qual espécie de iris (Setosa, Versicolor, Virginica) tem a maior média de comprimento de pétala?
def get_means():
    means = {}
    for spc in SPECIES:
        species_data = IRIS[IRIS['Species'] == spc]
        petal_length_mean = species_data['PetalLengthCm'].mean()
        means[spc] = petal_length_mean
          
    return means

# Resposta 1:
species_means = get_means()
max_species = max(species_means, key=lambda x: species_means[x])
print('Questão 1:\n')
for species, mean in species_means.items():
    print(f"A espécie {species} apresenta média de comprimento de pétala de {mean:.2f} cm.")
line()
print(f"A espécie {max_species} apresenta a maior média de comprimento de pétala. Média: {species_means[max_species]:.2f} cm.\n")

# Função Questão 2 - Há uma correlação significativa entre o comprimento da sépala e o comprimento da pétala?

# Resposta 2:

# Função Questão 3 - Qual a distribuição das espécies no banco de dados?

# Resposta 3:

# Função Questão 4 - Quais características (comprimento de sépala, largura de sépala, comprimento de pétala, largura depétala) têm a maior variabilidade dentro de cada espécie?

# Resposta 4:
