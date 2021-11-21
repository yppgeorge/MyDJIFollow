

# Link -> https://www.geeksforgeeks.org/how-to-connect-wifi-using-python/

# import module
import os


# display available netwroks
displayAvailableNetworks()

# input wifi name and password
name = input("Name of Wi-Fi: ")
password = input("Password: ")

# establish new connection
createNewConnection(name, name, password)

# connect to the wifi network
connect(name, name)
print("If you aren't connected to this network, try connecting with the correct password!")