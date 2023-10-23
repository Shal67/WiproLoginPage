import os
import django
import psutil
import random
from django.http import HttpResponse
os.environ.setdefault("DJANGO_SETTINGS_MODULE", r"C:\Users\shaly\OneDrive\Desktop\Wipro\backend\backend\settings.py")
django.setup()

# Define dummy IP addresses of backend servers
backend_servers = [
    {"ip": "192.168.1.101", "cpu_threshold": 80},
    {"ip": "192.168.1.102", "cpu_threshold": 80},
    # Add more backend servers as needed
]


def get_available_server():
    # Get CPU utilization for each server
    available_servers = []
    for server in backend_servers:
        cpu_percent = psutil.cpu_percent(interval=1, percpu=False)
        if cpu_percent < server["cpu_threshold"]:
            available_servers.append(server)
    
    # If all servers are busy, return a random one
    if not available_servers:
        return random.choice(backend_servers)
    
    return random.choice(available_servers)

def route_request(request):
    server = get_available_server()
    # Here, you would make an HTTP GET request to the selected server using server["ip"]
    # For simplicity, we'll just return the selected server's IP in the response.
    return HttpResponse(f"Request routed to server: {server['ip']}")

# Test the load balancing behavior
for _ in range(10):
    response = route_request(None)
    print(response.content)