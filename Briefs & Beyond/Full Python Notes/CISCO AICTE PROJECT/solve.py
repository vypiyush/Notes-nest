from ipaddress import ip_address, IPv6Address

def validIPAddress():
    a =1
    while(True):
        IP = input("Enter IP address: ")
        if(a == 10):
            break

        try:
            print( "IPv6" if type(ip_address(IP)) is IPv6Address else "IPv4")
        except ValueError:
            print ("Neither")
    

        

    """print("The decimal value of", IP, "is:")
    print(bin(IP), "in binary.")
    print(oct(IP), "in octal.")
    print(hex(IP), "in hexadecimal.")"""

    a= a+1


validIPAddress()
