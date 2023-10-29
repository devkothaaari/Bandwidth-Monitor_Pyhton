import tkinter as tk
from tkinter import ttk
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

def update_display():
    sent, recv = get_bandwidth_usage(network_interface)
    if sent is not None and recv is not None:
        label_sent.config(text=f"Sent: {convert_bytes(sent)}")
        label_recv.config(text=f"Received: {convert_bytes(recv)}")
    else:
        label_sent.config(text="Error retrieving data")
        label_recv.config(text="Error retrieving data")
    root.after(1000, update_display)  # Update every 1 second

def finish():
    root.destroy()  # Close the window

# Create the main window
root = tk.Tk()
root.title("Bandwidth Monitor")

# Create a style for ttk widgets
style = ttk.Style()
style.configure('TLabel', font=('Arial', 14), foreground='blue')  # Set label text color to blue
style.configure('TButton', font=('Arial', 12), foreground='white', background='green')  # Set button text color to white and background to green

# Create a frame to group widgets
frame = ttk.Frame(root, padding=(20, 10))
frame.pack(padx=10, pady=10)

# Create labels to display data
label_sent = ttk.Label(frame, text="Sent: ", style='TLabel')
label_sent.grid(row=0, column=0, padx=(0, 10))  # Add padding to the right

label_recv = ttk.Label(frame, text="Received: ", style='TLabel')
label_recv.grid(row=0, column=1)  # No padding

# Create a Finish button
finish_button = ttk.Button(root, text="Finish", command=finish, style='TButton')
finish_button.pack(pady=(10, 0))  # Add padding above the button

# Start the update loop
update_display()

# Run the GUI application
root.mainloop()

