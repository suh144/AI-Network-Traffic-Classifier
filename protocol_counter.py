import pyshark
from collections import Counter

capture = pyshark.FileCapture(
    r'E:\QUT 2nd year and final units\july 2026\CAB222\projects related to networks to remember concepts better\AI Network Traffic Classifier\captures\first_capture.pcapng',
    tshark_path=r'D:\Wireshark\tshark.exe',
    keep_packets=False
)

protocols = Counter()

for i, packet in enumerate(capture):

    try:
        protocols[packet.highest_layer] += 1
    except AttributeError:
        pass

    if i >= 1000:   # only inspect first 1000 packets
        break

definitions = {
    "TCP": "Reliable transport protocol",
    "TLS": "Encryption used by HTTPS",
    "DNS": "Converts domain names to IP addresses",
    "ARP": "Maps IP addresses to MAC addresses",
    "ICMPV6": "IPv6 control and discovery protocol",
    "HTTP": "Web communication protocol",
    "DHCP": "Automatically assigns IP addresses",
    "DHCPV6": "IPv6 version of DHCP"
}

print("\n===== Protocol Counts =====\n")

for protocol, count in protocols.most_common():

    print(f"{protocol}: {count}")

    if protocol in definitions:
        print(f"  Meaning: {definitions[protocol]}")

    print()
