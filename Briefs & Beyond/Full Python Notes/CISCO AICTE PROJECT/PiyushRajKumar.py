'''
--> PIYUSH RAJ KUMAR
Python Problem Statement :
 
Task 1: Ask the user to input 10 ipv4 addresses.
Task 2: Check if the addresses are valid ipv4 addresses.
Task 3: Convert the ipv4 addresses which are in decimal format to Binary, Octal and Hexadecimal format.
        For conversion use functions (inbuilt or library)
Task 4: Create a list which will hold the addresses. [Decimal, Binary, Octal and Hexadecimal]
Task 5: Transfer the contents of the list to a file named conversion.txt
Task 6: Print the following output on the screen
--------------------------------------------------------------------------------------
Output : 
The first IP address in Decimal, Binary, Octal and hexadecimal format is <output from the file conversion. txt>
The second IP address in Decimal, Binary, Octal and hexadecimal format is <output from the file conversion. txt>
…
The tenth IP address in Decimal, Binary, Octal and hexadecimal format is <output from the file conversion. txt>

Input :
0.0.0.0
10.2.1.1
10.9.255.34
10.21.0.257
10.21.0.255
127.82.55.45
179.16.31.5
192.0.0.0
192.10.0.255
223.102.56.78
255.255.255.255
'''


# Validate IPv4 Address
def isValid(ip):
    # split ip from '.' to convert it to octets list
    ip = ip.split('.')
    
    # valid ip address contains 4 octets
    if len(ip) != 4 :
        return False
    
    # each octets in range between 0 to 255
    for octet in ip:
        if (int(octet) < 0) or (int(octet) > 255):
            return False
    
    # if all cases pass then ip address is valid
    return True


# take 10 ipv4 address from user
def takeInput():
    # Array to hold 10 ip address
    ip_address_list = list()
    
    # take 10 valid ip address as input from user
    count = 10
    while(count):
        ip = input(f"Enter IP Address ({10-count+1}/10) : ")
        
        # add ip to list only if ip address is valid 
        if isValid(ip):
            ip_address_list.append(ip)
            count-=1
        
        # if ip is not valid print the warning message
        else:
            print("Please enter valid ip address range from 0.0.0.0 to 255.255.255.255")
            
    # return list which contans 10 ip address
    return ip_address_list


# convert ip address  from Decimal format to Binary, Octal and Hexadecimal format
def convertFormetAndSave(ip_address_list):
    # create or open file for save converted ip address
    file = open('conversion.txt', 'w')
    
    # interate over ip_address_list 
    for ip in ip_address_list:
        # create variable for each format
        decimal     = ip
        binary      = ''
        Octal       = ''
        hexadecimal = ''
        
        # interate over each octet and update
        ip = ip.split('.')
        for i in range(0, 4):            
            # add binary in 8 bit for each octet
            bin_num = str(bin(int(ip[i])))[2:]
            binary += '0'*(8-len(bin_num)) + bin_num
            
            # add octel number            
            Octal += str(oct(int(ip[i])))[2:]
            
            # add hex number in 2 digit each octet
            hex_num = str(hex(int(ip[i])))[2:]
            hexadecimal += '0'*(2-len(hex_num)) + hex_num
            
            # add '.' between each octet
            if i < 3:
                binary      += '.'
                Octal       += '.'
                hexadecimal += '.'  
            
        # add all format to a single string    
        ip_address_str = f"{decimal}, {binary}, {Octal}, {hexadecimal}\n"
        
        # write the converted ip address elements to each line in the file
        file.write(ip_address_str)
        
    # close file object
    file.close()


# Display content from the conversion.txt file
def printfileContents():
    # open the conversion.txt file
    file = open('conversion.txt')
    
    # Ordinal number dictnary 
    numToOrdinal = {1  : 'first',
                    2  : 'second',
                    3  : 'third',
                    4  : 'fourth', 
                    5  : 'fifth',
                    6  : 'sixth',
                    7  : 'seventh',
                    8  : 'eighth', 
                    9  : 'ninth',
                    10 : 'tenth'}
    
    # iterate over each line in file and read the content
    for i in range(1, 11):
        line = file.readline()
        print(f"The {numToOrdinal[i]} IP address in Decimal, Binary, Octal and hexadecimal format is {line}", end='')


# Main method
if __name__ == "__main__":
    ip_address_list    = takeInput()
    convertFormetAndSave(ip_address_list)
    printfileContents()

