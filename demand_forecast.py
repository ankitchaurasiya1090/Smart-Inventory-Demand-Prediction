import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Sample dataset (replace with real sales data)
data = {
    "day": [1, 2, 3, 4, 5, 6, 7],
    "sales": [50, 55, 53, 60, 62, 65, 70]
}
df = pd.DataFrame(data)

X = df[["day"]]
y = df["sales"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

# Predict for next 7 days
future_days = pd.DataFrame({"day": range(8, 15)})
pred = model.predict(future_days)

print("Next 7 days demand forecast:", pred)
