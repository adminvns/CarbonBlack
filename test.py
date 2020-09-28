from cbapi.protection import *
from cbapi import CbEnterpriseProtectionAPI
from cbapi.protection.rest_api import CbEnterpriseProtectionAPI

#taking dynamic input of console
cons = input("Enter Specfic Console shortcut name:\n")

#this function returns back the state of the cb protection API connection with the server,also throws exact error's description(if occurs).

def c():
    try:
        cn= CbProtectionAPI(profile=""+cons)
    except Exception as e:
        print(e.__doc__+"\nError Details:\n"+e.message)
        input("Press Enter to Exit")
    return cn 

    
cn = c()

#query to select a specific computer from the server
query = cn.select(Computer)
servername = input("Connection Established Successfully"+"\n Please Enter The Host Name:\n")

#this matches the server()
query = query.where("name:"+"*"+servername+"*")

for comp in query:
        print('\n\nHost Name :',comp.name,'\n','Unique ID = ',comp.id)
        print("Policy Name : "+comp.policyName+" \nPolicy Enf Id: "+str(comp.enforcementLevel)+" \nPolicy Id: "+str(comp.policyId))
        if(comp.daysOffline==-1):
                print("Host is connected")
        else:
                print("Host is diconnected from "+ str(comp.daysOffline)+ " days") 
#checks whether the host is in local approval(then it moves into local one)
if(comp.localApproval==False):
    print('The host is not running in local approval')
    i = input("Enter \"y\" to move the host into Local approval now...\n")
    if(i=="y"):
        comp.localApproval = True
        comp.save()
        print("The Host is running in local approval now\n")
    else:
        print('not moved\n')
#checks whether the host already in Normal Enf mode or not(then it moves it back to normal enf mode)
elif(comp.localApproval==True):
    print('The host is already running in local approval Mode\n')
    i = input("Enter \"y\" to move the host back to Normal Enf. Mode...\n")
    if(i=="y"):
        comp.localApproval = False
        comp.save()
        print('The host is now running into normal Enf. mode')
    else:
        print('not moved\n')

#final exit to user(to hold the screen)
attempt= input("Exit!!")
