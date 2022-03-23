# STANDARD Libraryies
from pynput import keyboard
from os import  system
from colorama import Fore,Style,Back,init
import pyperclip
import re
import pyautogui
import time

#########################################################################################################################################
#CUSTOM Libraries
import banner
import extract_file
#############################################################################################################################
#global variables
init()
elements=["Type","Application,","Region,"]
#---------------------------------------------------------------------------------------------------------------------------------------------
class Report_Helper():
    heading0="***\n##"
    heading1="What is "
    heading2="On the basis of " 
    heading3=" the market is segmented into "
    heading4="?"
    heading5="Use of "
    heading6="Growth Factors of "

    def __init__(self,des):
       self.des=des
       self.title=re.findall("Global\s(.+)Market",self.des)
       self.type=re.findall("Type\s\((.+?)\)",self.des)
       self.application=re.findall("Application\s\((.+?)\)",self.des)
       self.region=re.findall("Region\s\((.+?)\)",self.des)
       
     
    def Var(self):
      self.join_type=",".join(self.type) 
      self.join_application=",".join(self.application).replace(", Others","")
      self.join_region=",".join(self.region).replace(", Others","")
      

      finalquery=[    
                    str(self.heading0+self.heading1+self.title[0]+self.heading4),  # What is title name[0]
                    self.heading2+elements[0]+self.heading3+self.join_type,  
                    #On the basis of types the market is segmented into types[1]
                    [(f"{self.heading0}{self.heading1}{each}{self.heading4}") for each in self.type[0].split(",") ],  
                    #Loop over What is each type[2]
                    self.heading2+elements[1]+self.heading3+self.join_application, 
                    # On the basis of Application, the market is segmented into .[3]
                    [f"{self.heading0}{self.heading5} {str(self.title[0])} in {each}" for each in self.application[0].split(",")],
                    #Loop over each application type [4]
                    self.heading2+elements[2]+self.heading3+self.join_region,
                  #On the basis of region the market is segmented into region [5]
                    [f"{self.heading0}{each} {self.heading4}" for each in self.region[0].split(",")],
                  #Loop over each region[6]
                   str( self.heading6 +self.title[0])# Growth factors of title[7]
                                     ]
      return finalquery    
#---------------------------------------------------------------------------------------------------------------------------

def main():
    print(Fore.GREEN+Style.BRIGHT+banner.echo_banner)
    print(Fore.WHITE+"[1]>>Get your  own Description from excel file\n[2]>>Add the Description  manually ")
    choiced=input(">>")
    if  choiced=="":
      print("Choice cannot be an empty string")
      main()
    if choiced=="1":
      description=extract_file.extractFile()
      print("This is the description you want to copy" )
      print(Style.BRIGHT+Fore.BLUE+description)
    elif choiced=="2":
      print(Fore.RED+Style.BRIGHT+"Please enter description of  your report ")
      description=input("[#>>>]")
    if description=="":
       print("Wrong description")
       main()
    elif description=="exit":
          exit()
   
    n1=Report_Helper(description)
    data=n1.Var()
    
    return data

def paste_it(d):
   if not  "On"  in d:
        if "Other" in d:
          d=""
   pyperclip.copy(d)
   time.sleep(0.25)
   pyautogui.hotkey("ctrl","v")
  
def shortcut():
          for each in data_in_interator:
              if type(each)==type(list()):
                  for one in each:
                     paste_it(one)
              else:
                     paste_it(each)
          exit()            
def start():
  global data_in_interator
  data_in_interator=main()
  with keyboard.GlobalHotKeys({"<ctrl>+m":shortcut}) as keys:
          keys.join()        
if __name__ == '__main__':
      while True:
       starts=time.time()
       start()
       system("cls")
       ends=time.time()
       final=int(ends-starts)
       print(Fore.GREEN+Back.BLACK+f"You took {final/60} minutes   to complete it  ".center(90))
      
      


## done#
#Version 0 .6