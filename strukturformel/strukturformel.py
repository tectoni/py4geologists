#!/usr/bin/env python

import csv
import pandas as pd


# Define some dicts with molar masses, ion-ratio data etc, which are later used for the calculations
mmasses = {'SiO2':60.083, 'TiO2': 79.8658, 'Al2O3':101.959, 'FeO':71.844, 'MgO':40.304, 'CaO':56.077, 'Na2O':61.979, 'K2O':94.196}
catmult = {'SiO2':1, 'Al2O3':2, 'FeO':1, 'MgO':1, 'TiO2': 1, 'CaO':1, 'Na2O':2, 'K2O':2}
oxmult = {'SiO2':2, 'Al2O3':3, 'FeO':1, 'MgO':1, 'CaO':1, 'TiO2': 2, 'Na2O':1, 'K2O':1}

#with open('augit-2405alle.txt') as csv_file:
#    csv_reader = csv.DictReader(csv_file, delimiter='\t', quoting=csv.QUOTE_NONE)
#    csv_reader = (dict((k.strip(), v.strip()) for k, v in row.items() if v) for row in csv_reader)
#    for row in csv_reader:
#        print(row.values())
#        print(row['SiO2'])

# Read the analysis as csv-text file in a pandas dataframe and remove all 
# trailing and ending white-space between the separator (tab) by using a regex
df = pd.read_csv('augit-2405alle.txt', engine='python', sep='\s*\t\s*')

#print(df.at[10, 'Comment'])
#print(df.shape, df.ndim, df.size)

#for index, row in df.iterrows():
#    print(row['SiO2'])

#print(df.iloc[4:7, 2:5])
#print(df[['Al2O3', 'SiO2', 'CaO', 'Na2O', 'FeO']].sum())

# define a tuple which hold the keys for the elements which are used for the formula
sli = ('Al2O3', 'SiO2', 'TiO2', 'CaO', 'Na2O', 'FeO', 'MgO', 'K2O')

for index, row in df.iterrows():
    mydic = dict(df.iloc[index])
    newlist = [mydic[k] for k in sli if k in df]
    sm = row['SiO2']+row['Al2O3']
    print(index, row['Na2O'], sm)
    print(newlist, sum(newlist))

#print(pdatadict)
#pdatadict = (dict((k.strip(), v.strip()) for k, v in row.items() if v) for row in pdatadict)

#print(pdatadict)

#analysis = {'SiO2':52.3, 'Al2O3':37.0, 'FeO':10.3}

#print(analysis.get('SiO2'))
#print(sum(list(analysis.values())))

wts = dict(df.iloc[2])
#molepcat={}
#molepox={}
#moleratios={}
#print(type(wts), type(sli), type(moleratios), type(molepox), type(catmult), type(oxmult))
moleratios = {k:wts[k]/mmasses[k] for k in sli if k in df}
molepcat = {k:moleratios[k]*catmult[k] for k in sli if k in df}
molepox = {k:moleratios[k]*oxmult[k] for k in sli if k in df}
n_ox = 6 
n_fac = n_ox/sum(list(molepox.values()))
formula = {k:molepcat[k]*n_fac for k in sli if k in df}
#print(moleratios, molepcat, molepox)

print(formula)

# create an empty dataframe for storage of all formluas
df_formulas = pd.DataFrame()
ox_basis = 6
# Iterate the rows and calculate the formula for each analysis
for index, row in df.iterrows():
    # get the wt-% for the analysis from the main dataframe by using the index
    weights = dict(df.iloc[index])
    # perform the formula calculations by using dicts with the key-values
    moleratios = {k:weights[k]/mmasses[k] for k in sli if k in df}
    molepercat = {k:moleratios[k]*catmult[k] for k in sli if k in df}
    moleperox = {k:moleratios[k]*oxmult[k] for k in sli if k in df} 
    normalize_fac = ox_basis/sum(list(moleperox.values()))
    # result keeps a dict with key/values of the stoichiometric coefficients
    result = {k:molepercat[k]*normalize_fac for k in sli if k in df}
    # convert it to a pandas dataframe
    df_result = pd.DataFrame([result])
    print('df_res, res', df_result, result)
    # add it to the previous
    df_formulas = pd.concat([df_formulas, df_result], axis=0)

print(df_formulas)
df_formulas.to_csv('formulas.csv', index=False)
