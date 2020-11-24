#================FURRO404 // s0nic26===================#
# Port_Scanner.py 
# Made with help from s0nic26, hes cool, go check him out here: https://github.com/s0nic26
import threading
import socket
from queue import Queue

#==================^ Credits and Imports ^==================#

print("Made in Collaboration with s0nic26, he's a genius!")
print("ALSO NEITHER OF US ARE LIABLE FOR YOUR ACTIONS, THIS IS SOLELY FOR EDUCATIONAL PURPOSES!")
print('\nCMD - netstat -an |find /i "listening"')


target = input("Please enter the IP or Domain Address you want to scan: ")

#--DIRECTORY (Feel free to add your own!)--#

if target== ("home"):
    target = ("Your IP here")

elif target == ("google"):
    target = ("172.217.11.164")
    
print(" ")

host_ip = socket.gethostbyname(target)

print("Scanning", host_ip, "for all open ports...")

#=================The actual scanner lol.===================#

print_lock = threading.Lock()

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target, port))
        with print_lock:
            print('port', port, 'is open!!')


        con.close

    except:
        pass

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

q = Queue()

for x in range(500):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(1,1001):
    q.put(worker)

q.join()

#================FURRO404 // s0nic26===================#
