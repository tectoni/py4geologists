#!/usr/bin/env python

import pandas as pd

mmasses = {'SiO2':60.083, 'TiO2': 79.8658, 'Al2O3':101.959, 'FeO':71.844, 'MgO':40.304, 'CaO':56.077, 'Na2O':61.979, 'K2O':94.196}
catmult = {'SiO2':1, 'Al2O3':2, 'FeO':1, 'MgO':1, 'TiO2': 1, 'CaO':1, 'Na2O':2, 'K2O':2}
li_a = [mmasses]
print(li_a)
df_a = pd.DataFrame(li_a)
df_b = pd.DataFrame([catmult])
print(df_a)
df_c = pd.concat([df_a, df_b], axis=0)
print(df_c)
df_c.reset_index()
print(df_c)

