import socket
import threading
from datetime import datetime

print("=" * 50)
print("      TCP PORT SCANNER")
print("=" * 50)

target = input("Enter Target IP or Domain: ")

try:
    start_port = int(input("Enter Start Port: "))
    end_port = int(input("Enter End Port: "))
except ValueError:
    print("Invalid port number! Please enter numbers only.")
    exit()

print(f"\nTarget: {target}")
print(f"Scanning ports {start_port} to {end_port}")
print(f"Started at: {datetime.now()}\n")

threads = []

for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

log_file.close()

print("\n" + "=" * 50)
print("Scan Completed Successfully!")
print("Results have been saved to scan_results.txt")
print("=" * 50)