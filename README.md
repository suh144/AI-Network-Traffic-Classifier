# AI-Network-Traffic-Classifier

AI Network Traffic Classifier
Overview

AI Network Traffic Classifier is a Python-based networking and machine learning project that analyzes real network traffic captured using Wireshark and classifies protocols using a Decision Tree machine learning model.

The project was created to strengthen understanding of networking concepts including:

TCP
TLS
DNS
DHCP
ARP
ICMPv6
Port numbers
Protocol analysis
Network traffic visualization

The project combines:

Wireshark
TShark
Python
Pandas
Scikit-learn
Matplotlib
Project Workflow
Plain Text
Wireshark Capture
↓
PCAP File
↓
export_dataset.py
↓
traffic.csv
↓
traffic_classifier.py
↓
Protocol Prediction
↓
network_model_evaluation.py
↓
Model Accuracy & Analysis
Features
Protocol Counter

protocol_counter.py

Counts protocol occurrences from a packet capture.

Example output:

Plain Text
TCP: 672
TLS: 220
DNS: 26
ARP: 11
DHCP: 5
Traffic Visualization

network_traffic_graph.py

Generates visualizations of protocol distributions using Matplotlib.

Example:

TCP traffic
TLS traffic
DNS traffic
DHCP traffic
ARP traffic
Dataset Exporter

export_dataset.py

Extracts packet information from a Wireshark capture and exports a dataset for machine learning.

Output:

CSV
length,src_port,dst_port,protocol
66,443,2480,TCP
55,1033,443,TLS
103,12445,443,TLS
AI Traffic Classifier

traffic_classifier.py

Uses a Decision Tree classifier to predict network protocols based on packet characteristics.

Input:

Plain Text
Packet Length
Source Port
Destination Port

Output:

Plain Text
Predicted Protocol: TLS
 
Meaning:
Encryption used by HTTPS
 
Layer:
Application Layer Security
 
Model Evaluation

network_model_evaluation.py

Evaluates classifier performance using:

Accuracy Score
Classification Report
Confusion Matrix

Example result:

Plain Text
Model Accuracy: 95.02%
Network Anomaly Detector

network_anomaly_detector.py

Experimental extension project focused on identifying potentially unusual or suspicious traffic patterns.

This serves as a foundation for future cybersecurity and network anomaly detection work.

Results
Protocol Distribution

Observed traffic:

Protocol	CountTCP	672
TLS	220
DNS	26
IGMP	17
ICMPv6	14
ARP	11
LLMNR	8
mDNS	8
HTTP	7
DHCP	5
Machine Learning Performance
Model: Decision Tree Classifier
Features:
Packet Length
Source Port
Destination Port
Accuracy: 95.02%
Technologies Used
Networking
Wireshark
TShark
Programming
Python 3
Libraries
pandas
scikit-learn
matplotlib
pyshark
Installation

Install required packages:

Shell
pip install pandas
pip install scikit-learn
pip install matplotlib
pip install pyshark

Ensure TShark is installed and available.

Example:

Plain Text
D:\Wireshark\tshark.exe
Running the Project
Count Protocols
Shell
python protocol_counter.py
Export Dataset
Shell
python export_dataset.py
Generate Network Graph
Shell
python network_traffic_graph.py
Run AI Classifier
Shell
python traffic_classifier.py
Evaluate Model
Shell
python network_model_evaluation.py
Run Anomaly Detector
Shell
python network_anomaly_detector.py
Future Improvements

Planned enhancements:

Random Forest Classifier
Neural Network Classifier
Real-time Packet Classification
SYN Flood Detection
Port Scan Detection
DNS Anomaly Detection
Network Intrusion Detection
IoT Traffic Analysis
AIIoT Security Analytics
Educational Purpose

This project was developed as a networking and machine learning learning project to better understand:

Network protocols
Packet analysis
Feature extraction
Data visualization
Artificial intelligence
Cybersecurity concepts
Network anomaly detection
