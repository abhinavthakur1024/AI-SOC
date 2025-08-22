import re
from datetime import datetime

LOG_PATTERN = re.compile(
    r'(?P<timestamp>[\d\-T:.]+)\s+host=(?P<host>\S+)\s+process=(?P<process>\S+)\s+pid=(?P<pid>\d+)\s+action=(?P<action>\S+)\s+status=(?P<status>\S+)\s+src_ip=(?P<src_ip>\S+)\s+dest_ip=(?P<dest_ip>\S+)'
)

def parse_log(log_line: str):
    match = LOG_PATTERN.match(log_line)
    if not match:
        return None
    data = match.groupdict()
    data["timestamp"] = datetime.fromisoformat(data["timestamp"])
    data["pid"] = int(data["pid"])
    return data
