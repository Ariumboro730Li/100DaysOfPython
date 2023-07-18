import time
from datetime import datetime as dt
from settimer import settimer
from blocker import block_websites
from unblocker import unblock_websites

# Path to the hosts file
hosts_path = r"/etc/hosts"

# List of websites to block
websites_to_block = ["www.youtube.com"]

# Redirect IP address
redirect_ip = "127.0.0.1"

# Define start and end times for working hours
start_time =  settimer(8) # 8:00AM
end_time = settimer(18) # 6:00PM

print(f"{start_time.hour} to {end_time.hour} is your working hours")

while True:
    # check the current time whether is within the specified working hours or not.
    if start_time < dt.now() < end_time:
        block_websites(hosts_path, websites_to_block, redirect_ip)
    else:
        unblock_websites(hosts_path, websites_to_block)
    time.sleep(5)
