import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Simple training dataset
data = {
    "length": [55, 60, 120, 130, 1500, 1400, 80, 90],
    "dst_port": [443, 443, 53, 53, 443, 443, 80, 80],
    "connection_count": [10, 12, 8, 9, 15, 14, 7, 6],
    "label": [
        "Normal",
        "Normal",
        "Normal",
        "Normal",
        "Normal",
        "Normal",
        "Suspicious",
        "Suspicious"
    ]
}

df = pd.DataFrame(data)

X = df[["length", "dst_port", "connection_count"]]
y = df["label"]

model = DecisionTreeClassifier()

model.fit(X, y)

print("\n=== Network Anomaly Detector ===\n")

length = int(input("Packet Length: "))
dst_port = int(input("Destination Port: "))
connection_count = int(input("Connection Count: "))

new_data = pd.DataFrame({
    "length": [length],
    "dst_port": [dst_port],
    "connection_count": [connection_count]
})

prediction = model.predict(new_data)

result = prediction[0]

print("\nPrediction:", result)

if result == "Normal":
    print("Traffic appears normal.")
else:
    print("Traffic may require investigation.")
