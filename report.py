from platform import system
from pynput import keyboard
from colorama import Fore,Style,Back,init
import pyperclip
import time
import os
import pyautogui
import re
############################################################################
init()
elements=["Type","Application,","Region,"]
con=True
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
       
      # print(self.title,self.type,self.application,self.region())
    def Var(self):
      self.join_type=",".join(self.type) 
      self.join_application=",".join(self.application).replace(", Others","")
      self.join_region=",".join(self.region).replace(", Others","")
      #print(type(self.title[0]))

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
                    [f"{self.heading0}{each}{self.heading4}" for each in self.region[0].split(",")],
                  #Loop over each region[6]
                   str( self.heading6+self.title[0])# Growth factors of title[7]
                                     ]
      return finalquery    

def copy_it(d):
 for each in d:
      if  type(each) ==type(str()):
         yield each
      else:
        for eachone in each:
           yield eachone
def main():

    print(Fore.GREEN+Style.BRIGHT+"""
                     _____                       _     _    _      _                 
                    |  __ \                     | |   | |  | |    | |                
                    | |__) |___ _ __   ___  _ __| |_  | |__| | ___| |_ __   ___ _ __ 
                    |  _  // _ \ '_ \ / _ \| '__| __| |  __  |/ _ \ | '_ \ / _ \ '__|
                    | | \ \  __/ |_) | (_) | |  | |_  | |  | |  __/ | |_) |  __/ |   
                    |_|  \_\___| .__/ \___/|_|   \__| |_|  |_|\___|_| .__/ \___|_|   
                                | |                                  | |              
                                |_|                                  |_|              

                                                 Version 0.4 
                                                            BY COOLSID
""")
  
    print(Fore.RED+Style.BRIGHT+"Please enter description of  your report ")
    description=input("[#>>>]")
    print(Fore.GREEN+Style.BRIGHT+"Description Copied succesfully".center(80))
    global start_time
    start_time=time.time()
    if description=="":
       print("Wrong description")
       main()
    elif description=="exit":
          exit()
   
    n1=Report_Helper(description)
    data=n1.Var()
    return data

def paste_it():
  pyautogui.hotkey("ctrl","v")
  # control=keyboard.Controller()
  # control.press(keyboard.Key.ctrl)
  # control.press("v")ss
  # control.release("v")
  # control.release(keyboard.Key.ctrl)
def shortcut():
  try:
     word=next(data_in_interator)
     if not  "On"  in word:
        if "Other" in word:
          word=""

     pyperclip.copy(word)
     print(Fore.BLUE+Style.BRIGHT+"This has been copied ---"+Style.RESET_ALL,word)
     paste_it()

  except StopIteration:
    exit()
if __name__ == '__main__':
      while con:

        data_in_interator=copy_it(main())
        with keyboard.GlobalHotKeys({"<ctrl>+m":shortcut}) as keys:
          keys.join()
        end_time=time.time()
        time_taken=int((end_time-start_time)/60)
        print(Fore.MAGENTA+Style.BRIGHT+f"You completed it in- {time_taken} minutes".center(80))
        time.sleep(3)
## done 
##Version 0.4
