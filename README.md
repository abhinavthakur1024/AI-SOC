# AI-SOC: Intelligent Threat Hunting Agent

## 🎯 Objective
Build an AI-driven Security Operations Center (SOC) agent that analyzes system log files and network data to detect anomalies such as failed logins, privilege escalation, and suspicious network connections.

## ✅ Outcome
- Generate mock syslog data (failed logins, sudo misuse, lateral movement, etc.)
- Parse and send data into the ELK stack for visualization
- Train ML models (K-Means, Isolation Forest) on logs to detect anomalies
- Provide alerts on suspicious activities

## 🛠 Skills & Tools
- **Python**: Data parsing, anomaly detection
- **ELK Stack**: Log storage, search, visualization
- **Machine Learning**: K-Means, Isolation Forest
- **Docker**: Containerized environment

start code    
docker start elasticsearch docker start kibana  
This gave you: Elasticsearch API at → http://localhost:9200 Kibana at → http://localhost:5601   
2️⃣ Verify Elasticsearch is Running  curl -X GET "http://localhost:9200/"   
3️⃣ Run AI-SOC main.py for the first time python main.py 
