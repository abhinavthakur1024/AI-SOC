import random
import datetime

def generate_logs(num_logs=100):
    hosts = ["server1", "server2", "server3"]
    processes = ["sshd", "nginx", "mysql", "python"]
    actions = ["login", "logout", "file_access", "privilege_escalation"]
    statuses = ["success", "failure"]

    logs = []
    for _ in range(num_logs):
        log = f"{datetime.datetime.utcnow().isoformat()} host={random.choice(hosts)} process={random.choice(processes)} pid={random.randint(100,9999)} action={random.choice(actions)} status={random.choice(statuses)} src_ip=192.168.1.{random.randint(1,255)} dest_ip=10.0.0.{random.randint(1,255)}"
        logs.append(log)
    return logs
