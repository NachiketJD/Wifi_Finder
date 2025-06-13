import subprocess
#subprocess is imported to run the command in the terminal.

#check_Output method, which checks the output of the command and returns True if it is successful, False otherwise. This is done by checking the return code of the command, which is 0 if the command is successful.
nw = subprocess.check_output(['netsh', 'wlan', 'show', 'network']).decode('ascii')# this object, nw, contains all the network information, including the SSID of each network, this is the name of the network this done using the netsh command in the command prompt, the wlan show network command shows all the available networks in the system, the decode function is used to convert the output to a string, and the split function is used to split the output into a list of strings, each string represents a network. This is done becoz the output of the netsh command is in bytes and we need to convert it to string to 
print(nw)
#This will print all the available networks in the system, including the SSID of each network. 
#SSID stands for Service Set Identifier. The SSID is the name of the network, it is used to identify the network.