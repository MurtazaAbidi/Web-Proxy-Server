import socket
import requests
import os
FORMAT = "utf-8"
def check(filename):
    datafile = open('cache\CacheFileNames.txt')
    found = False
    for line in datafile:
        if filename in line:
            found = True
            break
    return found



print ("\nWelcome to the Proxy server.\n\nTo get started, connect a client.")


# Initialise socket stuff
TCP_IP = "127.0.0.1" # Only a local server
TCP_PORT = 1457 # Just a random choice
BUFFER_SIZE = 1024 # Standard size
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()
print ("\nConnected to by address: {}".format(addr))
url = conn.recv(1024).decode(FORMAT)
cachee= url
cachee= cachee.replace('https://','')
cachee= cachee.replace('http://','')
cachee= cachee.replace('www.','')
cachee= cachee.replace('.com','')
cachee= cachee.replace('.edu.pk','')
cachee= cachee.replace('.nu.edu.pk','')
cachee= cachee + ".html"

cf = open('cache\CacheFileNames.txt', 'a')
if os.stat("cache\CacheFileNames.txt").st_size == 0 or check(cachee)==False:
    r= requests.get(url)
    f = open('cache\\'+cachee, 'w')
    htmll = r.text
    f.write(htmll)
    f.close()
    cf.write(cachee+'\n')
    cf.close()

filename = cachee
fnsize=len(filename)
conn.send(str(fnsize).encode(FORMAT))
res=bytes(filename,FORMAT)
conn.send(res)
conn.recv(BUFFER_SIZE).decode(FORMAT)
fsize=os.stat('cache\\'+filename)
conn.send(str(fsize.st_size).encode(FORMAT))

content = open('cache\\'+filename, "rb")
l = content.read(BUFFER_SIZE)
print ("\nSending...")
while l:
    conn.send(l)
    l = content.read(BUFFER_SIZE)
content.close()



