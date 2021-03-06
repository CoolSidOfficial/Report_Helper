import re
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
