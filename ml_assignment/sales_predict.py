import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.DataFrame({
    'Advertising': [5, 10, 15, 20, 25],
    'Sales': [30, 50, 70, 90, 110]
})

X = df[['Advertising']]
y = df['Sales']

model = LinearRegression()
model.fit(X, y)

print(model.predict([[18]]))