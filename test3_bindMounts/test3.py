try:
    with open('server.txt', 'r') as file:
        servers = file.read().splitlines()  # Automatically strips newlines
except FileNotFoundError:
    print("No server data found.")
else:
    for server in servers:
        if server:  
            print(server)














            