## **🔹 Common Python Modules for DevOps & Their Uses** 🚀  

Python is widely used in **DevOps** for automation, infrastructure management, monitoring, and CI/CD pipelines. Below are some of the most commonly used Python modules in DevOps with their **descriptions and use cases**.

---

### **1️⃣ os** – Operating System Interactions  
✅ **Use Case**: Running system commands, managing environment variables, working with files/directories.  
```python
import os
print(os.getcwd())  # Get current working directory
os.system("ls -la")  # Run shell command
os.environ["MY_VAR"] = "value"  # Set environment variable
```

---

### **2️⃣ subprocess** – Execute System Commands  
✅ **Use Case**: Run shell commands and capture output.  
```python
import subprocess
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)  # Print command output
```

---

### **3️⃣ shutil** – File & Directory Management  
✅ **Use Case**: Copy, move, delete files/directories.  
```python
import shutil
shutil.copy("file.txt", "/backup/")  # Copy file
shutil.rmtree("/tmp/logs/")  # Delete directory
```

---

### **4️⃣ logging** – Logging for Automation & Monitoring  
✅ **Use Case**: Debugging, logging DevOps scripts.  
```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Deployment started")
logging.error("Service crashed!")
```

---

### **5️⃣ pathlib** – File System Operations (Modern Alternative to `os.path`)  
✅ **Use Case**: File and directory manipulation.  
```python
from pathlib import Path
file = Path("config.yaml")
if file.exists():
    print(file.read_text())  # Read file content
```

---

### **6️⃣ requests** – HTTP Requests & API Calls  
✅ **Use Case**: Interacting with REST APIs for cloud services, monitoring, and CI/CD.  
```python
import requests
response = requests.get("https://api.github.com")
print(response.json())  # Print JSON response
```

---

### **7️⃣ boto3** – AWS Automation  
✅ **Use Case**: Automating AWS (EC2, S3, IAM, Lambda, RDS, etc.).  
```python
import boto3
s3 = boto3.client("s3")
buckets = s3.list_buckets()
print(buckets)
```

---

### **8️⃣ paramiko** – SSH & Remote Execution  
✅ **Use Case**: Automate server configuration via SSH.  
```python
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("remote-server", username="user", password="pass")
stdin, stdout, stderr = ssh.exec_command("ls -l")
print(stdout.read().decode())  # Print output
ssh.close()
```

---

### **9️⃣ fabric** – Remote Execution & Deployment  
✅ **Use Case**: Automate deployments, execute commands on remote servers.  
```python
from fabric import Connection
conn = Connection("user@remote-server")
conn.run("sudo systemctl restart nginx")  # Restart Nginx
```

---

### **🔟 docker** – Manage Docker Containers  
✅ **Use Case**: Automate Docker container creation, deletion, and monitoring.  
```python
import docker
client = docker.from_env()
container = client.containers.run("nginx", detach=True)
print(container.logs())  # Get container logs
```

---

### **1️⃣1️⃣ kubernetes (k8s.client)** – Manage Kubernetes Clusters  
✅ **Use Case**: Automate Kubernetes deployments & cluster monitoring.  
```python
from kubernetes import client, config
config.load_kube_config()
v1 = client.CoreV1Api()
pods = v1.list_pod_for_all_namespaces(watch=False)
for pod in pods.items:
    print(pod.metadata.name)
```

---

### **1️⃣2️⃣ ansible-runner** – Run Ansible Playbooks from Python  
✅ **Use Case**: Trigger Ansible playbooks for configuration management.  
```python
import ansible_runner
runner = ansible_runner.run(private_data_dir='/path/to/playbooks', playbook='deploy.yml')
print(runner.status)  # Print execution status
```

---

### **1️⃣3️⃣ psycopg2** – PostgreSQL Database Automation  
✅ **Use Case**: Automate database management, backups, and monitoring.  
```python
import psycopg2
conn = psycopg2.connect("dbname=mydb user=admin password=secret")
cur = conn.cursor()
cur.execute("SELECT * FROM users;")
print(cur.fetchall())  # Fetch results
conn.close()
```

---

### **1️⃣4️⃣ mysql-connector-python** – MySQL Database Automation  
✅ **Use Case**: Automate MySQL database operations.  
```python
import mysql.connector
conn = mysql.connector.connect(user='root', password='secret', host='localhost', database='testdb')
cursor = conn.cursor()
cursor.execute("SHOW DATABASES")
print(cursor.fetchall())  # List all databases
conn.close()
```

---

### **1️⃣5️⃣ yaml** – Read & Write YAML Files (for CI/CD & Configuration)  
✅ **Use Case**: Automate YAML configuration handling.  
```python
import yaml
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)
print(config)  # Print YAML content
```

---

### **1️⃣6️⃣ json** – Read & Write JSON Files (for API & Configuration)  
✅ **Use Case**: Manage configuration & API data.  
```python
import json
data = {"name": "DevOps", "version": 1}
with open("config.json", "w") as file:
    json.dump(data, file)
```

---

### **1️⃣7️⃣ schedule** – Job Scheduling & Task Automation  
✅ **Use Case**: Automate periodic DevOps tasks.  
```python
import schedule
import time

def job():
    print("Running scheduled task...")

schedule.every(10).seconds.do(job)  # Run every 10 seconds

while True:
    schedule.run_pending()
    time.sleep(1)
```

---

### **1️⃣8️⃣ socket** – Network Programming  
✅ **Use Case**: Monitor network ports, automate networking tasks.  
```python
import socket
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f"Hostname: {hostname}, IP: {ip_address}")
```

---

### **1️⃣9️⃣ smtplib** – Email Notifications  
✅ **Use Case**: Send email alerts in CI/CD pipelines.  
```python
import smtplib
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("your_email@gmail.com", "password")
server.sendmail("from@gmail.com", "to@gmail.com", "Deployment Completed!")
server.quit()
```

---

## **🚀 Summary Table**
| **Module**         | **Use Case** |
|--------------------|-------------|
| `os`, `shutil`    | File, directory, and system command handling |
| `subprocess`      | Execute shell commands |
| `requests`        | REST API calls (CI/CD, monitoring) |
| `boto3`           | AWS automation |
| `paramiko`, `fabric` | SSH & remote command execution |
| `docker`          | Docker container automation |
| `kubernetes`      | Manage Kubernetes clusters |
| `ansible-runner`  | Automate Ansible playbook execution |
| `psycopg2`, `mysql-connector-python` | Database automation |
| `yaml`, `json`    | Configuration file management |
| `schedule`        | Task scheduling |
| `socket`         | Network monitoring |
| `smtplib`        | Email notifications |

---

### **🔹 Conclusion**
Python provides **powerful modules** for **DevOps automation, infrastructure management, CI/CD pipelines, cloud automation, monitoring, and security**.  

Would you like help with a **real-world DevOps automation script** using these modules? 😊
