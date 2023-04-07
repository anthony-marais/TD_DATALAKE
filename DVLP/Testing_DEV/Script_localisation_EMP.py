# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 18:59:35 2023

@author: kousseila
"""

import  os 

from bs4 import BeautifulSoup

mycible_EMP = "C:/TD_DATALAKE/DATALAKE/1_LANDING_ZONE/LINKEDIN/EMP/" 
myListOfFile = os.listdir(mycible_EMP)





#==============================================================================
#-- LINKEDIN (EMP) : Fonction renvoyant la ville de l'emploi proposé
#==============================================================================
def Get_ville_EMP (Soup):
    location_span = Soup.find('span', {'class': 'topcard__flavor topcard__flavor--bullet'})
    if location_span:
        location_text = location_span.text
        location_parts = location_text.split(', ')
        if len(location_parts) == 2:
            city, country = location_parts
            return city
    return 'NULL'

#print(Get_ville_EMP(mySoup))




def Get_Pays_EMP(Soup):
    location_span = Soup.find('span', {'class': 'topcard__flavor topcard__flavor--bullet'})
    if location_span:
        location_text = location_span.text
        location_parts = location_text.split(', ')
        if len(location_parts) == 2:
            city, country = location_parts
            return country
    return 'NULL'


#print(Get_Pays_EMP(mySoup))



key=500

myFilePathName = "C:/TD_DATALAKE/DATALAKE/2_CURATED_ZONE/LINKEDIN/EMP/Data_lOCAL_EMP.csv"
#-- Ouverture du fichier en création
csvfile = open(myFilePathName, "w", encoding = "utf-8")
csvfile.write("id_localisation"+ ";" + "Ville" +  ";" + "Pays" )
csvfile.write('\n')



for i in myListOfFile:
        
    myFile = mycible_EMP+str(i)
    File = open(myFile, "r", encoding="utf8")
    File_read = File.read()
    
    mySoup= BeautifulSoup(File_read,'lxml')
    

   

    myListeDeLigneAEcrire = []
#-- Remplissage de la liste
    key=key+1
    
    
    myListeDeLigneAEcrire.append(key)
    
  #  myListeDeLigneAEcrire.append(str(i))
     
    myListeDeLigneAEcrire.append(str(Get_ville_EMP(mySoup)))
    myListeDeLigneAEcrire.append(str(Get_Pays_EMP(mySoup)))
    
  #  myListeDeLigneAEcrire.append(str(Get_Desc_EMP(mySoup)))
    
  #  myListeDeLigneAEcrire.append(str(Get_ville_EMP(mySoup)))
    
   
    
    res =str(myListeDeLigneAEcrire)
    res = res.replace('[','').replace(']','')
    res = res.replace(',',';')
    res = res.replace('; ',';')
    res = res.replace("'",'')
    res = res.replace('"','')
    res = res.replace(' ;',';')
    res = res.replace('; ',';')
    
   
    print (res)
    print("****************************************************************************************")
    csvfile.write(res) 
    csvfile.write('\n')
csvfile.close()

##### -- création de deux fichier CSV :
    # ----Data_EMP.csv
# dans le path :    "C:/TD_DATALAKE/DATALAKE/2_CURATED_ZONE/LINKEDIN/EMP/Data_loca_EMP.csv"