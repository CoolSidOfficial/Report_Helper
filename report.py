from pynput import keyboard
from colorama import Fore,Style,Back,init
import pyperclip
import pyautogui
import time
import os
import re
############################################################################
init()
elements=["Types","Application,","Region,"]

class Report_Helper():
    heading1="What is "
    heading2="On the basis of " 
    heading3=" the market is segmented into "
    heading4="Growth Factors of"
    heading5="Use of "
    heading6="Growth Factors of "

    def __init__(self,des):
       self.des=des
       self.title=re.findall("Global\s(.+)Market",self.des)
       self.type=re.findall("Type\s\((.+?)\)",self.des)
       self.application=re.findall("Application\s\((.+?)\)",self.des)
       self.region=re.findall("Region\s\((.+?)\)",self.des)
       
      # print(self.title,self.type,self.application,self.region())
    def Var(self):
      self.join_type=",".join(self.type) 
      self.join_application=",".join(self.application)#.replace(", Others","")
      self.join_region=",".join(self.region)#.replace(", Others","")
      #print(type(self.title[0]))

      finalquery=[  str(self.title[0]),  #Title name[0]
                    str(self.heading1+self.title[0]),  # What is title name[1]
                    self.heading2+elements[0]+self.heading3+self.join_type,  
                    #On the basis of types the market is segmented into types[2]
                    [(f"{self.heading1}{each}") for each in self.type[0].split(",") ],  
                    #Loop over What is each type[3]
                    self.heading2+elements[1]+self.heading3+self.join_application, 
                    # On the basis of Application, the market is segmented into .[4]
                    [f"{self.heading5}{each}" for each in self.application[0].split(",")],
                    #Loop over each application type [5]
                    self.heading2+elements[2]+self.heading4+self.join_region,
                  #On the basis of region the market is segmented into region [5]
                    [f"{each}{self.title[0]}" for each in self.region[0].split(",")],
                  #Loop over each region
                   str( self.heading6+self.title[0])# Growth factors of title
                                     ]
      return finalquery    
     
     
 
if __name__ == '__main__':
    print(Fore.GREEN+Style.BRIGHT+"""
                     _____                       _     _    _      _                 
                    |  __ \                     | |   | |  | |    | |                
                    | |__) |___ _ __   ___  _ __| |_  | |__| | ___| |_ __   ___ _ __ 
                    |  _  // _ \ '_ \ / _ \| '__| __| |  __  |/ _ \ | '_ \ / _ \ '__|
                    | | \ \  __/ |_) | (_) | |  | |_  | |  | |  __/ | |_) |  __/ |   
                    |_|  \_\___| .__/ \___/|_|   \__| |_|  |_|\___|_| .__/ \___|_|   
                                | |                                  | |              
                                |_|                                  |_|              

                                                 Version 0.1
                                                            BY COOLSID
""")
  
    print(Fore.RED+Style.BRIGHT+"Please enter description of  your report ")
    description=input("[#>>>]")
    if description=="":
       print("Wrong description")
       exit()
    elif description=="exit":
        exit()
    os.system("CLS")

    n1=Report_Helper(description)
    data=n1.Var()
    for each in data:
      # print(type(each))
      if  type(each) ==type(str()):
         pyperclip.copy(each)     
         print(Fore.BLUE+Style.BRIGHT+"This has been copied ---"+Style.RESET_ALL,each)
         input(Fore.GREEN+Style.BRIGHT+"Please press Enter key   to copy next thing ".center(80)) 
      else:
        for eachone in each:
           pyperclip.copy(eachone)
           print(Fore.RED+Style.BRIGHT+"This has been copied --- "+Style.RESET_ALL,eachone)
           input("Please press Enter   key   to copy next thing ".center(80)) 
      
 #0.1;14-10-2021    