#!/usr/bin/env python

import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter
df = pd.read_csv('survey_results_public.csv')
idnum = df['ResponseId']
lang_responses = df['LanguageHaveWorkedWith']

language_counter = Counter()
for response in lang_responses:
    language_counter.update(str(response).split(';'))

print(language_counter)
languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

plt.title('Most Popular Languages')
plt.xlabel('Ages')
plt.ylabel('Number of People who use')
plt.tight_layout()

plt.show()
print(df['LanguageHaveWorkedWith'])

#
#Addition: the same functionality with build-in csv-Reader
#replace with lines 10-12
#immport csv
#with open('survey_results_public.csv') as csv_file:
#    csv_reader = csv.DictReader(csv_file):
#    language_counter = Counter()
#
#    for row in csv_reader:
#        language_counter.update(row['LanguagesWorkedWith'].split(';'))
