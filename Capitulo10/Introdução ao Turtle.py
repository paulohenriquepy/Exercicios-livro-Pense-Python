# -*- coding: utf-8 -*-
"""
Created on Sun Jun  8 10:30:37 2025

@author: Paulo
"""

import pandas as pd

df = pd.read_csv('Coches_Segunda_Mano.csv')

df.head()

df.tail()

df.shape

df.dtypes

df.describe()

df['Puertas'].unique()
