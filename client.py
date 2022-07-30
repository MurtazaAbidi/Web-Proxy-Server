import socket
import webbrowser
FORMAT = "utf-8"

# Initialise socket stuff
TCP_IP = "127.0.0.1" # Only a local server
TCP_PORT = 1457 # Just a random choice
BUFFER_SIZE = 1024 # Standard chioce
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url= ''
def conn():
    # Connect to the server
    print ("Sending server request...")
    try:
        s.connect((TCP_IP, TCP_PORT))
        print ("Connection sucessful")
        
    except:
        print ("Connection unsucessful. Make sure the server is online.")

def sending_url():
    print()
    url= input ("Enter URL : ")
    s.send ((url).encode(FORMAT))


def getting_file():
    f_name_size= int(s.recv(1024).decode(FORMAT))
    # print(f_name_size)
    filename= s.recv(f_name_size).decode(FORMAT)
    s.send(("1").encode(FORMAT))
    file_size= int(s.recv(1024).decode(FORMAT))


    # print("file name size: ", f_name_size)
    # print ("file Name:",filename)
    print("File Size recieved : ", file_size)

    outputfilename= "output.html"
    output_file = open('Recievedfile\\'+outputfilename, "wb")
    
    bytes_recieved= 0
    while bytes_recieved < file_size:
        l = s.recv(BUFFER_SIZE)
        output_file.write(l)
        bytes_recieved += BUFFER_SIZE
    output_file.close()

def opening_website():
    webbrowser.open_new_tab("Recievedfile\\output.html")
    print ('\nThe Recieved file is opened in your default browser...')

conn()
sending_url()
getting_file()
opening_website()
