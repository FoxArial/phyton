import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('lab 6\insurance.csv')

df = df[['age', 'region', 'bmi', 'expenses']].dropna()
df = pd.get_dummies(df, columns=['region'], drop_first=True)

X = df.drop('expenses', axis=1)
y = df['expenses']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
abs_error = np.abs(y_test - y_pred)
percentage_error = (abs_error / y_test) * 100

comparison = pd.DataFrame({'Реальні значення': y_test, 'Передбачені значення': y_pred})
comparison['Похибка (%)'] = percentage_error

plt.figure(figsize=(10, 6))
plt.hist(comparison['Похибка (%)'], bins=30, edgecolor='black', color='skyblue')

plt.title('Гістограма відсоткових похибок прогнозу')
plt.xlabel('Похибка (%)')
plt.ylabel('Кількість прогнозів')
plt.grid(True)
plt.show()