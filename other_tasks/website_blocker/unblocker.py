def unblock_websites(hosts_path, websites_to_block):
    print("Fun Hours")
    with open(hosts_path, "r+") as file:
        content = file.read()
        file.seek(0)
        for line in content:
            if not any(website in line for website in websites_to_block):
                file.write(line)
        file.truncate()
