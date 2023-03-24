import nmap

def scan_ports(host, ports):
    # Create a new instance of the Nmap PortScanner class
    nm = nmap.PortScanner()

    # Scan the specified host for open ports
    scan_results = nm.scan(host, ports)

    # Print the results to the console
    print("Open ports for host", host)

    print("==== TCP ==== \n")
    print(nm[host]['tcp'].keys())

    for port in nm[host]['tcp']:
        service = nm[host]['tcp'][port]['name']

        print("Port:", port, "\t",  "Service:", service, "\t", "State:", nm[host]['tcp'][port]['state'], "\t", "Product:", nm[host]['tcp'][port]['product'], "\t", "cpe: ", nm[host]['tcp'][port]['cpe'])

if __name__ == '__main__':
    # print a welcome message
    print("-----" * 20)

    print("\n BEM VINDO AO PORT SCAN!! \n")

    print("-----" * 20)
    
    # Get user input for host and port range
    host = input("Informe um Número IP para averigar: ")
    ports = input("Informa um intervalo de portas (ex.: 1-5000): ")

    # Call the scan_ports function with the user's input
    scan_ports(host, ports)
