from socket import create_connection

from datetime import datetime

TIMEOUT = 5 # seconds

target = input("Enter a target to scan: ")
print("Please enter the range of ports you would like to scan on the target")

start_port = input("Enter a start port (inclusive): ")
end_port = input("enter an end port (inclusive): ")

# generates addresses for each port in range, +1 is to make end port inclusive
addresses = [(target, i) for i in range(int(start_port), int(end_port) + 1)]

print("Scanning started at " + str(datetime.now())) # https://www.w3schools.com/python/python_datetime.asp

for address in addresses:
    try:
        # https://docs.python.org/3/library/socket.html#socket.create_connection
        sock = create_connection(address, TIMEOUT) # will throw error if port is closed
    except:
        print(f"Port {address[1]} is closed")
    else:
        print(f"Port {address[1]} is open")

print("Port scanning completed")