# Python Port Scanner

A simple Python-based port scanner script that scans a specified range of ports on a target IP address. It identifies open ports by attempting TCP connections and reports the results back to the user. This tool can be useful for network troubleshooting, testing firewall configurations, and identifying open ports on a given IP.

## Features

- Scans a range of TCP ports on a specified IP address.
- Reports which ports are open.
- Lightweight and easy to use.
- Customizable port range.

## Requirements

- Python 3.x

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/hazik-khalid/Port-Scanner
   ```
2. Navigate to the project directory:
   ```bash
   cd port-scanner
   ```

## Usage

Run the script with Python, specifying the target IP address and the range of ports you want to scan.

```bash
python3 port_scanner.py <target_ip> <start_port> <end_port>
```

### Example

To scan ports 1-1024 on IP `192.168.1.1`:

```bash
python3 port_scanner.py 192.168.1.1 1 1024
```

### Command-Line Arguments

- `target_ip`: IP address of the target machine.
- `start_port`: Starting port number for the scan.
- `end_port`: Ending port number for the scan.

## Sample Output

The script outputs a list of open ports:

```bash
Starting scan on 192.168.1.1
Port 22 is open
Port 80 is open
Port 443 is open
Scan complete.
```

## Disclaimer

**Use this tool responsibly.** Only scan IP addresses and ports you have permission to test. Unauthorized port scanning may violate the terms of service of networks and result in penalties.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
