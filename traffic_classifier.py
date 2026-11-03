import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# Load dataset exported from Wireshark
df = pd.read_csv(
    r"E:\QUT 2nd year and final units\july 2026\CAB222\projects related to networks to remember concepts better\AI Network Traffic Classifier\data\traffic.csv"
)

print("\nDataset Loaded Successfully!\n")

# Features and labels
X = df[["length", "src_port", "dst_port"]]
y = df["protocol"]

# Split dataset
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

# Evaluate model
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy:.2%}")

print("\nProtocols in Dataset:\n")
print(df["protocol"].value_counts())

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))

# Protocol descriptions
notes = {
    "TLS": "Encryption used by HTTPS",
    "DNS": "Converts domain names into IP addresses",
    "DHCP": "Automatically assigns IPv4 addresses",
    "DHCPV6": "Automatically assigns IPv6 addresses",
    "HTTP": "Web communication protocol",
    "TCP": "Reliable transport protocol using acknowledgements",
    "ARP": "Maps IP addresses to MAC addresses",
    "ICMPV6": "IPv6 control and discovery protocol",
    "IGMP": "Internet Group Management Protocol",
    "LLMNR": "Local Link Multicast Name Resolution",
    "MDNS": "Multicast DNS",
    "SSDP": "Simple Service Discovery Protocol"
}

# Layer descriptions
layers = {
    "TCP": "Transport Layer",
    "TLS": "Application Layer Security",
    "DNS": "Application Layer",
    "HTTP": "Application Layer",
    "DHCP": "Application Layer",
    "DHCPV6": "Application Layer",
    "ARP": "Link Layer",
    "ICMPV6": "Network Layer",
    "IGMP": "Network Layer",
    "LLMNR": "Application Layer",
    "MDNS": "Application Layer",
    "SSDP": "Application Layer"
}

# Networking facts
facts = {
    "DNS": "DNS usually uses port 53 and translates hostnames into IP addresses.",
    "TLS": "TLS commonly uses port 443 and provides HTTPS encryption.",
    "HTTP": "HTTP commonly uses port 80 for web communication.",
    "DHCP": "DHCP automatically assigns IP addresses, subnet masks and gateways.",
    "DHCPV6": "DHCPv6 provides IPv6 configuration information.",
    "ARP": "ARP resolves IPv4 addresses to MAC addresses on a local network.",
    "TCP": "TCP provides reliable delivery using sequence numbers and acknowledgements.",
    "ICMPV6": "ICMPv6 is used for Neighbor Discovery and IPv6 operations.",
    "IGMP": "IGMP manages multicast group memberships.",
    "LLMNR": "LLMNR resolves names on local networks when DNS is unavailable.",
    "MDNS": "mDNS allows local device discovery without a DNS server.",
    "SSDP": "SSDP is used by UPnP devices for service discovery."
}

print("\n===== Enter Packet Details =====\n")

try:

    length = int(input("Enter packet length: "))
    src_port = int(input("Enter source port: "))
    dst_port = int(input("Enter destination port: "))

    new_packet = pd.DataFrame({
        "length": [length],
        "src_port": [src_port],
        "dst_port": [dst_port]
    })

    prediction = model.predict(new_packet)

    predicted = prediction[0]

    print("\n===== AI Prediction =====\n")

    print("Predicted Protocol:", predicted)

    print(
        "Meaning:",
        notes.get(predicted, "No description available")
    )

    print(
        "Layer:",
        layers.get(predicted, "Unknown Layer")
    )

    print(
        "Fact:",
        facts.get(predicted, "No fact available.")
    )

except ValueError:

    print("\nPlease enter valid integer values.")
