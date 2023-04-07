# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 19:10:55 2023

@author: Kousseila
"""
mycibleIN = "/home/virus/Documents/TD_DATALAKE/DATALAKE/1_LANDING_ZONE/"
mycibleOUT = "/home/virus/Documents/TD_DATALAKE/DATALAKE/2_CURATED_ZONE/"

MylistPa=['GLASSDOOR/AVI/','GLASSDOOR/SOC/','LINKEDIN/EMP/']



import  os

def Get_size_file(Soup) :
    Size= os.path.getsize(Soup)
    return(str(Size)+' KO')


from datetime import datetime


def Get_Date_creation(Soup) :
    Date_creation=os.path.getctime(Soup)
    
    return(datetime.fromtimestamp(Date_creation).strftime('%Y-%m-%d %H:%M:%S'))




def Get_Date_modification(Soup) :
    Date_modification=os.path.getmtime(Soup)
    return(datetime.fromtimestamp(Date_modification).strftime('%Y-%m-%d %H:%M:%S'))


def Get_datetime_ingestion():
    Result = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return(Result)





    
import re,fnmatch

#creation fichier CSV

for x in range(0, len(MylistPa)) :
        
    txtclean = re.sub(r'(.*)/(.*)/', r'\2',MylistPa[x] )
            
    myFilePathName = mycibleOUT+MylistPa[x]+'Date_tech_'+txtclean+'.csv'
           
    #-- Ouverture du fichier en création
    csvfile = open(myFilePathName, "w", encoding = "utf-8")
    csvfile.write("Id"+ ";" + "Nom_Fichier"+ ";" + "Site_Web" + ";" + "Date_Creation" + ";" +
                  "Date_Modification" + ";" + "Date_ingestion" + ";"  + "Taille_Fichier")
    csvfile.write('\n')
            
    myListOfFile = os.listdir(mycibleIN+MylistPa[x])
    
            
    key= 0       
    
    for i in  range(0, len(myListOfFile)):
            
       
        
        
    
       
    
        myListeDeLigneAEcrire = []
    #-- Remplissage de la liste
        key=key+1
        
        
        myListeDeLigneAEcrire.append(key)
        myListeDeLigneAEcrire.append(str(myListOfFile[i]))
          
        if fnmatch.fnmatch(myListOfFile[i], '*GLASSDOOR*'):
            myListeDeLigneAEcrire.append("GLASSDOOR")
     
        elif fnmatch.fnmatch(myListOfFile[i], '*LINKEDIN*'):
            myListeDeLigneAEcrire.append("LINKEDIN")
        
        myListeDeLigneAEcrire.append(str(Get_Date_creation(mycibleIN+MylistPa[x]+myListOfFile[i])))
        myListeDeLigneAEcrire.append(str(Get_Date_modification(mycibleIN+MylistPa[x]+myListOfFile[i])))
        myListeDeLigneAEcrire.append(str(Get_datetime_ingestion()))
        myListeDeLigneAEcrire.append(str(Get_size_file(mycibleIN+MylistPa[x]+myListOfFile[i])))

   
    
        res =str(myListeDeLigneAEcrire)
        res = res.replace('[','').replace(']','')
        res = res.replace(',',';')
        res = res.replace('; ',';')
        res = res.replace("'",'')

        print (res)
        print("****************************************************************************************")
        csvfile.write(res) 
        csvfile.write('\n')
csvfile.close()
