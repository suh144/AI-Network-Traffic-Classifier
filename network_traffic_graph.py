import matplotlib.pyplot as plt

protocols = {
    "TCP": 672,
    "TLS": 220,
    "DNS": 26,
    "IGMP": 17,
    "ICMPV6": 14,
    "ARP": 11,
    "LLMNR": 8,
    "MDNS": 8,
    "HTTP": 7,
    "DHCP": 5,
    "DHCPV6": 4,
    "SSDP": 3
}

plt.figure(figsize=(10,5))
plt.bar(protocols.keys(), protocols.values())

plt.title("Network Protocol Counts")
plt.xlabel("Protocol")
plt.ylabel("Number of Packets")

plt.xticks(rotation=45)

for i, value in enumerate(protocols.values()):
    plt.text(i, value + 2, str(value), ha="center")

plt.tight_layout()
plt.show()
