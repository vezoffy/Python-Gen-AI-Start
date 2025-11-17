import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.DataFrame({
    'RAM': [8, 16, 16, 32, 32],
    'Storage': [512, 512, 1024, 1024, 2048],
    'Speed': [2.5, 2.8, 3.0, 3.2, 3.4],
    'Price': [55, 72, 85, 110, 130] 
})

X = df[['RAM', 'Storage', 'Speed']]
y = df['Price']

model = LinearRegression()
model.fit(X, y)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

predicted_price = model.predict([[24, 1024, 3.1]])
print("Predicted Price (₹k):", predicted_price[0].round(2))