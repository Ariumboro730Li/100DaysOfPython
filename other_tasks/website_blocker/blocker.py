def block_websites(hosts_path, websites_to_block, redirect_ip):
    print("Working Hours...")
    with open(hosts_path, "r+") as file:
        content = file.read()
        for website in websites_to_block:
            if website not in content:
                file.write(f"{redirect_ip}\t{website}\n")
