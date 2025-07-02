# -*- coding: utf-8 -*-
"""
Created on Sun Jun  8 10:30:37 2025

@author: Paulo
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Coches_Segunda_Mano.csv')


df['Puertas'].unique()

df.shape