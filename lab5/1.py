import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

db = pd.read_csv('titanic.csv')
not_surv = db[db['Survived']==0]
tickets = not_surv['Pclass'].value_counts()

not_surv = not_surv.dropna(subset=['Age'])

def group_age(age):
    if age <= 12:
        return 'Child'
    elif age <= 17:
        return 'Teen'
    elif age <= 30:
        return 'Young adult'
    elif age <= 60:
        return 'Adult'
    else:
        return 'Elder'

not_surv['Age group'] = not_surv['Age'].apply(group_age)

age_group_count = not_surv['Age group'].value_counts()

age_group_count.plot(kind='bar', color='blue', edgecolor='black')
plt.title('Кількість загиблих за віковими групами')
plt.xlabel('Вікові групи')
plt.ylabel('Кількість людей')
plt.grid(axis='y', linestyle='--')

plt.tight_layout()
plt.show()

print('\n', db.info())
print('\n5: ', db.head(5))
print('\n10:', db.tail(10))
print('\n10:', not_surv)
print('\n10:', tickets)
