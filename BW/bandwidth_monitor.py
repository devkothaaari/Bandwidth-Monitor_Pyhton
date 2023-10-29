import psutil
import time

# Define the network interface you want to monitor
network_interface = "enp0s3"  # Replace with your specific interface

def get_bandwidth_usage(interface):
    try:
        stats = psutil.net_io_counters(pernic=True).get(interface)
        if stats:
            return stats.bytes_sent, stats.bytes_recv
    except Exception as e:
        print(f"Error occurred while retrieving network statistics: {e}")
    return None, None

def convert_bytes(bytes):
    if bytes is not None:
        if bytes < 1024:
            return f"{bytes} B"
        elif bytes < 1024**2:
            return f"{bytes/1024:.2f} KB"
        elif bytes < 1024**3:
            return f"{bytes/1024**2:.2f} MB"
        else:
            return f"{bytes/1024**3:.2f} GB"
    return "N/A"

def main():
    try:
        while True:
            # Get bandwidth usage
            sent, recv = get_bandwidth_usage(network_interface)
            
            if sent is not None and recv is not None:
                # Print the results
                print(f"Sent: {convert_bytes(sent)} | Received: {convert_bytes(recv)}")
            else:
                print("Error retrieving bandwidth usage.")
            
            # Wait for a short period of time
            time.sleep(1)
    
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()

