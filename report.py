# STANDARD Libraries
from pynput import keyboard
from os import  system
from colorama import Fore,Style,Back,init
import pyperclip
import pyautogui
import time

#########################################################################################################################################
#CUSTOM Libraries
import banner
import extract_file
from logic import Report_Helper
import  logger
#############################################################################################################################
#global variables
init()


def main():
    print(Fore.GREEN+Style.BRIGHT+banner.echo_banner)
    print(Fore.WHITE+"[1]>>Get your  own Description from excel file\n[2]>>Add the Description  manually\n[3]>>Check the log (admin only) ")
    choiced=input(">>")
    if  choiced=="":
      print("Choice cannot be an empty string")
      main()
    if choiced=="1":
      description=extract_file.extractFile()
      logger.create_log(description)
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
      logger.create_log(description)
    elif choiced=="3":  # this is good for creating log 
       log_count=logger.show_log()
       print(f"This is the number of report you have wrote on this day-{log_count}".center(80))    
       time.sleep(5.3)
       exit()
    n1=Report_Helper(description)
    data=n1.Var()
    
    return data
 #-------------------------------------------------------------------------------------   
def copy_it(d): # it will copy each 
 for each in d:
      if  type(each) ==type(str()):
         yield each
      else:
        for eachone in each:
           yield eachone

########################################################################################################################################################################################
def paste_it():
  pyautogui.hotkey("ctrl","v")

def shortcut():
  try:
     word=next(data_in_interator)
     if "Other" in word:
       if not "On" in word:
         word=""
       else:
        word=word.rstrip(",Other")  # this will remove Other if it is in between a string 
  
     pyperclip.copy(word)
     print(Fore.BLUE+Style.BRIGHT+"This has been copied ---"+Style.RESET_ALL,word)
     paste_it()

  except StopIteration:
    exit()
 #########################################################################################################
#reading the keyboard
def start():
  global data_in_interator
  data_in_interator=copy_it(main())
  with keyboard.GlobalHotKeys({"<ctrl>+m":shortcut}) as keys:
          keys.join()        

##########################################################################################################################################
if __name__ == '__main__':
      while True:
       starts=time.time()
       start()
       system("cls")
       ends=time.time()
       final=int(ends-starts)
       print(Fore.GREEN+Back.BLACK+f"You took {final/60} minutes   to complete it  ".center(90))
      
      


## done#
#Version 0 .7