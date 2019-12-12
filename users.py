import os

USERFILE = 'userInfo.txt'

def read_data():
    the_file = open(USERFILE,'r')
    file_data = {}
    for line in the_file:
        (key, v1, v2, v3) = line.split()
        file_data[key] = [v1, v2, v3]
    the_file.close()
    return file_data

def write_data(data):
    the_file = open(USERFILE,'w')
    for key,values in data.items():
        the_file.write(key + " ")    
        the_file.write(values[0] + " ")
        the_file.write(values[1] + " ")
        the_file.write(values[2] + "\n")    
    the_file.close()


    
def create_file(): 
    userInfoFile = open(USERFILE,'a') 
    userInfoFile.close()
    
def delete_file():
    answer =input("Deleting file, all data lost. Sure Y/N? ")
    if answer.upper() == 'Y':
        print()
        print("*****   Removing " + USERFILE)
        os.remove(USERFILE)
        create_file() 
