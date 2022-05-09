########################################
# standard library
from datetime import  date
############################################################################################################
def create_log(descri):
  with open("reports.log","a+") as file:
      current=date.today().strftime("%d;%B;%Y") # store date in the format of 10;monthname;202
      file.write(current+"|"+ descri+"\n")
##############################################################################################################  
def extract_log(date):
  counter=dict()
  with open("reports.log","r" ) as file:
    for each in file:
        counter[each.split("|")[0]]=counter.get(each.split("|")[0],0) + 1         
    if date  in  counter:
       return counter[date]  # if found return to the show log function
    elif date not in counter:
      print("The date is not available")
      exit()
#########################################################################################################
def show_log():  
  print("Please enter the date of which you wanted to see the logs")
  log_date=input("Date;Month;year]>>")
  if log_date=="":
    show_log()
  return extract_log(log_date) # RETURN TO THE REPORT 
######################v##########################################################################################################################################################  
if __name__=="__main__":
    show_log()
##############################################
### done