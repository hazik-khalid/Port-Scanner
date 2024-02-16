import socket

def scan_ports(target_ip, num_ports):
    open_ports = []

    try:
        for port in range(1, num_ports + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            # Attempt to connect to the target IP and port
            result = sock.connect_ex((target_ip, port))

            if result == 0:
                # Port is open
                open_ports.append(port)
                print(f"Port {port} is open")

            sock.close()

    except KeyboardInterrupt:
        print("Scanning interrupted by user.")
        exit()
    
    except socket.error:
        print("Could not connect to the target.")
        exit()

    return open_ports

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    
    try:
        num_ports = int(input("Enter the number of ports to scan: "))
    except ValueError:
        print("Please enter a valid number.")
        exit()

    open_ports = scan_ports(target_ip, num_ports)

    if open_ports:
        print("Open ports: ", open_ports)
    else:
        print("No open ports found.")
