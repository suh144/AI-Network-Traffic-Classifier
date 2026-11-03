import pandas as pd
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# Load dataset
df = pd.read_csv(
    r"E:\QUT 2nd year and final units\july 2026\CAB222\projects related to networks to remember concepts better\AI Network Traffic Classifier\data\traffic.csv"
)

# Features and labels
X = df[["length", "src_port", "dst_port"]]
y = df["protocol"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = DecisionTreeClassifier(
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print(f"\nModel Accuracy: {accuracy:.2%}\n")

# Detailed metrics
print("Classification Report:\n")
print(classification_report(y_test, y_pred))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix:\n")
print(cm)

# Protocol distribution graph
protocol_counts = df["protocol"].value_counts()

plt.figure(figsize=(10, 5))

plt.bar(
    protocol_counts.index,
    protocol_counts.values
)

plt.title("Protocol Distribution")

plt.xlabel("Protocol")
plt.ylabel("Packet Count")

plt.xticks(rotation=45)

for i, value in enumerate(protocol_counts.values):
    plt.text(
        i,
        value + 2,
        str(value),
        ha="center"
    )

plt.tight_layout()

plt.show()
