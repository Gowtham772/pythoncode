import threading 
from threading import*
import time

dictionary={} #  dictionary

# |Create operation|

def create(key,value,timeout=0):
    if key in dictionary:
        print("error: this key is already exists") 
    else:
        if(key.isalpha()):
            if len(dictionary)<(1024*1020*1024) and value<=(16*1024*1024): #file size less than 1GB and Jason object value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #It is for input key_name capped at 32chars
                    dictionary[key]=l
            else:
                print("error: Memory limit exceeded!! ")
        else:
            print("error: Invalind key_name it should contain only alphabets")

# |Read operation|
            
def read(key):
    if key not in dictionary:
        print("error: given key doesn't exist in database. Please enter a valid key") 
    else:
        b=dictionary[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                stri=str(key)+":"+str(b[0]) 
                return stri
            else:
                print("error: time-to-live of",key,"has expired")
        else:
            stri=str(key)+":"+str(b[0])
            return stri

# |delete operation|

def delete(key):
    if key not in dictionary:
        print("error: given key doesn't exist in database. Please enter a valid key")
    else:
        b=dictionary[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                del dictionary[key]
                print("key is successfully deleted")
            else:
                print("error: Time-To-Live of",key,"has expired") 
        else:
            del dictionary[key]
            print("key is successfully deleted")

def modify(key,value):
    b=dictionary[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in dictionary:
                print("error: given key does not exist in database. Please enter a valid key") 
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                dictionary[key]=l
        else:
            print("error: time-to-live of",key,"has expired") 
    else:
        if key not in dictionary:
            print("error: given key does not exist in database. Please enter a valid key")
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            dictionary[key]=l
#|CRD operations|

create("Python",25)
create("IDLE",70,3600) 
read("Python")
read("IDLE")
create("Python3",50)
modify("Python",55) 
delete("Python")

