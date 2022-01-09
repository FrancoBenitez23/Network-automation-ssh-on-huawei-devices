import paramiko
import time

conn = paramiko.SSHClient()          # High-level representation of a session with an SSH server
conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # When 1st connection, ask to trust this server or not
                                                            # Change SSH key authentication as "Trust All". Add untrusted hosts
conn.connect("192.168.0.3", 22, "franco", "Huawei123_")        # Initiate SSH connection with IP, Port, Username, Password

commands = conn.invoke_shell()       # Request an interactive shell session on this channel.

commands.send("N\n")
time.sleep(.5)
output = commands.recv(65535)
output = output.decode("utf-8")
print (output)

commands.send("display device\n")    # Send command to device
time.sleep(.5)                       # Wait for 0.5seconds
output = commands.recv(65535)        # .recv() - The maximum amount of data to be received at once is specified by nbytes
output = output.decode("utf-8")      # Change file type from bytes to string
print (output)

commands.send("display memory \n")
time.sleep(.5)
output = commands.recv(65535)
output = output.decode("utf-8")
print (output)

commands.send("display alarm all \n")
time.sleep(.5)
output = commands.recv(65535)
output = output.decode("utf-8")
print (output)


commands.send("sys \n")
commands.send( "interface Loopback 1 \n")
commands.send( "ip address 1.1.1.1 255.255.255.0\n")
commands.send("commit \n")
commands.send( "display ip interface brief \n")
time.sleep(.5)
output = commands.recv(65535)
output = output.decode("utf-8")
print (output)
