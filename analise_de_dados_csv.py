import pandas as pd

dados = pd.read_csv('C:/Ambiente/workspace/python/athlete_events.csv')

dados.head()

import matplotlib.pyplot as plt

dados.hist(column='Weight', bins=100)

plt.show()