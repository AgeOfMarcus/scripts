#!/usr/bin/python3

import urllib.request
import os

def clear():
        return "\n"*50

banner = '''
--------------------
        MMenu
     Version 1.2
--------------------
Developed by:
     marcus.mek
Codename:
       SlyFox
--------------------
'''
help = banner+'''
--------------------
Programs
--------------------
help - prints this
update - updates this program
clear/cls - clears screen
tools - useful tools installer
read - read a text file
write - write text to a file
python - run python3 code

ls - lists files in current directory

socket - all kinds of sockets
gmail - send an email with gmail
smtp - send an email with an smtp server
wget - wget, but in python

base64 - encode/decode base64
binary - convert to and from binary
--------------------
'''
cmdmsg = "MMENU/"
enter = '''
'''

def multi_line(message):
        print(message+"\nOn a new line, enter ':done' to finish.")
        text = ''
        editing = True
        while editing:
                newline = input()
                if newline == ":done":
                        editing = False
                else:
                        text += newline + '\n'
        return text

def error(errormsg):
        return "[Error]: "+str(errormsg)

def run(cmd):
        os.system(cmd+" > tmp.mmenu")
        with open("tmp.mmenu","r") as tmp:
                return tmp.read()

def gitClone(repo):
        print("[Downloading]...")
        print(run("cd ~; git clone https://github.com/"+repo+".git --recursive"))

def send_email(server_addr,server_port,username,password,from_addr,to_addr,subject,body):
        try:
                import smtplib
                server = smtplib.SMTP(server_addr,server_port)
                server.ehlo()
                server.starttls()
                server.login(username,password)
                message = '\r\n'.join(['To: %s' % to_addr,
                                       'From: %s' % from_addr,
                                       'Subject: %s' % subject,
                                       '',body])
                server.sendmail(from_addr,[to_addr],message)
                print("[Sent Email]")
        except Exception as e:
                print(error(e))

def tcp_listener():
        ip = input('Enter IP to listen on (blank for all): ')
        if ip == '':
                ip = " "
        port = int(input("Port to listen on: "))
        import socket
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
                s.bind((ip,port))
                s.listen(10)
        except Exception as error:
                print("[Error]: "+str(error))
                print("You are probably offline. Next time, try entering [127.0.0.1] as your address to accept only local connections.")
        print("Press [Ctrl+C] to exit")
        while True:
                try:
                        conn, addr = s.accept()
                        print("[Connected]: "+str(addr))
                        text = conn.recv(1024).decode()
                        if len(text) > 0:
                                print("[Recieved]: "+str(text))
                except KeyboardInterrupt:
                        break

def tcp_send():
        ip = input("IP to send to: ")
        port = int(input("Port to send to: "))
        import socket
        c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
                c.connect((ip,port))
                print("[Connected]")
                data = input("Text to send: ").encode()
                c.send(data)
                print("[Sent]")
        except Exception as error:
                print("[Error]: "+str(error))

def tcp_chat_server():
        ip = input("Your IP: ")
        port = int(input("Port to listen on: "))
        import socket
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((ip,port))
        s.listen(10)
        try:
                while True:
                        conn, addr = s.accept()
                        print("["+str(addr)+"] Connected")
                        data = conn.recv(1024).decode()
                        if len(data) > 0:
                                print("Client: "+str(data))
                                conn.send(input("Reply: ").encode())
        except KeyboardInterrupt:
                pass

def tcp_chat_client():
        ip = input("Server IP: ")
        port = int(input("Server port: "))
        import socket
        c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        c.connect((ip,port))
        try:
                while True:
                        c.send(input("Send: ").encode())
                        data = c.recv(1024).decode()
                        if len(data) > 0:
                                print("Server: "+str(data))
        except KeyboardInterrupt:
                pass

def o2o_chat():
        print("1. Server\n2. Client\n3. Back")
        tmpmsg = cmdmsg + "SOCKET/CHAT/"
        cmd = getcmd(tmpmsg)
        if cmd == "1":
                tcp_chat_server()
        elif cmd == "2":
                tcp_chat_client()
        elif cmd == "3":
                pass

def socketMenu():
        tmpmsg = cmdmsg + "SOCKET/"
        print("1. TCP Listener\n2. Send data over TCP\n3. One to one chat\n4. Back")
        cmd = getcmd(tmpmsg)
        if cmd == "1":
                tcp_listener()
        elif cmd == "2":
                tcp_send()
        elif cmd == "3":
                o2o_chat()
        elif cmd == "4":
                pass

def installerMenu():
                tmpmsg = cmdmsg + "TOOLS/"
                print("1. ProbeKit\n2. The Lazy Script\n3. WifiPhisher\n4. Katoolin\n5. MCONN Server\n6. MCONN Client\n7. Back")
                cmd = getcmd(tmpmsg)
                if cmd == "1":
                        gitClone("brannondorsey/ProbeKit")
                        run("~/ProbeKit/shell/install.sh")
                elif cmd == "2":
                        gitClone("arismelachroinos/lscript")
                        run("~/lscript/install.sh")
                elif cmd == "3":
                        gitClone("wifiphisher/wifiphisher")
                        run("python ~/wifiphisher/setup.py install")
                elif cmd == "4":
                        gitClone("LionSec/katoolin")
                elif cmd == "5":
                        run("cd ~; wget http://3spooky5me.tk/files/python3/mconn_server.py")
                elif cmd == "6":
                        run("cd ~; wget http://3spooky5me.tk/files/python3/mconn_client.py")
                elif cmd == "7":
                        pass

def read_file():
        filename = input("Enter file name / path to file: ")
        try:
                with open(filename,"r") as f:
                        text = f.read()
                        return text
        except Exception as e:
                print("[Error] - Are you sure that file exists and has read permissions?")
                print("[Error]: "+str(e))

def run_py():
        try:
                return(exec(multi_line("Type code below.")))
        except Exception as e:
                print(error(e))

def gmail_menu():
        sender = input("Your email address: ")
        passwd = input("Your password: ")
        print(clear())
        print("[Cleared Screen]")
        addr = "smtp.gmail.com"
        port = 587
        reciever = input("Send email to: ")
        subject = input("Subject of email: ")
        body = multi_line("Enter email body below.")
        send_email(addr,port,sender,passwd,sender,reciever,subject,body)

def smtp_mailer():
        addr = input("Enter server address: ")
        port = int(input("Enter port: "))
        user = input("Enter username: ")
        passwd = input("Enter password: ")
        print(clear()+"[Cleared Screen]")
        from_addr = input("Enter 'From' address: ")
        to_addr = input("Enter 'To' address: ")
        subject = input("Email subject: ")
        body = multi_line("Type body below.")
        send_email(addr,port,user,passwd,from_addr,to_addr,subject,body)

def base64_encode(text):
        import base64
        try:
                data = bytes(text, 'utf-8')
                result = base64.b64encode(data)
                return result.decode('utf-8')
        except Exception as e:
                print("Error: "+str(e))
def base64_decode(text):
        import base64
        try:
                data = bytes(text, 'utf-8')
                result = base64.b64decode(data)
                return result.decode('utf-8')
        except Exception as e:
                print("Error: "+str(e))
def binary_encode(num):
        try:
                return "{0:08b}".format(int(num))
        except Exception as e:
                print("Error: "+str(e))
def binary_decode(num):
        try:
                return eval("print("+"0b"+str(num)+")")
        except Exception as e:
                print("Error: "+str(e))
def looksay(thing):
        try:
                n = str(thing)
                return ''.join( str(len(list(g))) + k for k, g in groupby(n))
        except Exception as e:
                print("Error: "+str(e))

def b64_menu():
        tmpmsg = cmdmsg + "BASE64/"
        print("1. Enocde Base64\n2. Decode Base64\n3. Back")
        cmd = getcmd(tmpmsg)
        if cmd == "1":
                text = input("Text to encode: ")
                print(base64_encode(text))
        elif cmd == "2":
                text = input("Text to decode: ")
                print(base64_decode(text))
        elif cmd == "3":
                pass
def bin_menu():
        tmpmsg = cmdmsg + "BINARY/"
        print("1. Number to binary\n2. Binary to number\n3. Exit")
        cmd = getcmd(tmpmsg)
        if cmd == "1":
                try:
                        num = int(input("Number to convert: "))
                        print(str(binary_encode(num)))
                except Exception as e:
                        error(e)
        elif cmd == "2":
                try:
                        num = input("Binary to convert: ")
                        print(binary_decode(num))
                except Exception as e:
                        print(error(e))
        elif cmd == "3":
                pass

def wget(url):
        return (urllib.request.urlopen(url)).read()

def wget_menu():
        try:
                url = input("Enter url: ")
                result = wget(url).decode('utf-8')
                tmpmsg = cmdmsg + "WGET/"
                print("1. Save data to file\n2. Print data")
                cmd = getcmd(tmpmsg)
                if cmd == "1":
                        filename = input("Enter filename / path to file:\n")
                        with open(filename,"wb") as out_file:
                                out_file.write(result.encode())
                                print("[+] Wrote data to file")
                elif cmd == "2":
                        print(result)
        except Exception as e:
                print(error(e))

def write_menu():
        try:
                filename = input("Enter filename / path to file:\n")
                text = multi_line("Enter text to write below.")
                with open(filename,"wb") as out_file:
                        out_file.write(text)
                        print("[+] Wrote text to file successfully")
        except Exception as e:
                print(error(e))

def update_me():
        try:
                new = wget("http://3spooky5me.tk/files/python3/mmenu.py")
                filename = input("Enter path to mmenu.py (leave blank for [mmenu.py]):\n")
                if filename == '':
                        filename = "mmenu.py"
                with open(filename,"wb") as out_file:
                        out_file.write(new)
                        print("[+] Wrote update to mmenu.py")
                        print("[*] To apply changes, please restart program")
        except Exception as e:
                print("[Error]: "+str(e))

def webserver_menu():
        try:
                tmpmsg = cmdmsg + "WEBSERVER/"
                print("[*] Checking/Installing required packages")
                run("python3-pip install http")
                print("Enter port to host webserver on:")
                port = getcmd(tmpmsg)
                print("Enter root directory to host webserver: ")
                root_dir = getcmd(tmpmsg)
                print("[*] Starting server")
                run("cd "+root_dir+"; python3 -m http.here "+port)
        except Exception as e:
                print(error(e))
                print("[*] Trying again...")
                run("cd "+root_dir+"; python3 -m http.server "+port)

def handle(cmd):
        if cmd == "exit":
                print("See ya next time!")
                exit(0)
        elif cmd == "help":
                print(help)
        elif cmd == "clear" or cmd == "cls":
                print(clear())
        elif cmd == "socket":
                socketMenu()
        elif cmd == "tools":
                installerMenu()
        elif cmd == "read":
                print(read_file())
        elif cmd == "python":
                print(run_py())
        elif cmd == "gmail":
                gmail_menu()
        elif cmd == "smtp":
                smtp_mailer()
        elif cmd == "base64":
                b64_menu()
        elif cmd == "binary":
                bin_menu()
        elif cmd == "wget":
                wget_menu()
        elif cmd == "write":
                write_menu()
        elif cmd == "update":
                update_me()
        elif cmd == "webserver":
                webserver_menu()
        elif cmd == "ls":
                run("ls")
        else:
                print("[!] Invalid Option")

def getcmd(msg):
        cmd = input(msg+"> ").lower()
        return cmd


print(clear())
print(banner)
while True:
        handle(getcmd(cmdmsg))
