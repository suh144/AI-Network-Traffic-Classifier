import pyshark
import pandas as pd

capture = pyshark.FileCapture(
    r'E:\QUT 2nd year and final units\july 2026\CAB222\projects related to networks to remember concepts better\AI Network Traffic Classifier\captures\first_capture.pcapng',
    tshark_path=r'D:\Wireshark\tshark.exe',
    keep_packets=False
)

rows = []

for i, packet in enumerate(capture):

    try:

        length = int(packet.length)
        protocol = packet.highest_layer

        src_port = 0
        dst_port = 0

        if hasattr(packet, "tcp"):

            src_port = int(packet.tcp.srcport)
            dst_port = int(packet.tcp.dstport)

        elif hasattr(packet, "udp"):

            src_port = int(packet.udp.srcport)
            dst_port = int(packet.udp.dstport)

        rows.append({
            "length": length,
            "src_port": src_port,
            "dst_port": dst_port,
            "protocol": protocol
        })

    except:
        pass

    if i >= 1000:
        break

df = pd.DataFrame(rows)

df.to_csv(
    r'E:\QUT 2nd year and final units\july 2026\CAB222\projects related to networks to remember concepts better\AI Network Traffic Classifier\data\traffic.csv',
    index=False
)

print(df.head())

print("\nDataset exported successfully!")
