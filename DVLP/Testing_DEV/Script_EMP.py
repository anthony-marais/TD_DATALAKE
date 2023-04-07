# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 19:06:15 2023

@author: Kousseila
"""

import  os 

from bs4 import BeautifulSoup


mycible_EMP = "/home/virus/Documents/TD_DATALAKE/DATALAKE/1_LANDING_ZONE/LINKEDIN/EMP/"
myListOfFile = os.listdir(mycible_EMP)




#==============================================================================
#-- LINKEDIN (EMPLOI) : Libellé de l'offre
#==============================================================================
def Get_libelle_emploi_EMP(Soup):
    myTest = Soup.find_all('h1', attrs = {'class':'topcard__title'}) 
    if (myTest == []) : 
        Result = 'NULL'
    else:
        myTest = str(myTest[0].text)
        if (myTest == []) : 
            Result = 'NULL'
        else:
            Result = myTest
    return(Result)

#==============================================================================
#-- LINKEDIN (EMPLOI) : Fonction renvoyant le Nom de la Société 
#==============================================================================
def Get_nom_EMP(Soup):
    myTest = Soup.find_all('span', attrs = {'class':'topcard__flavor'}) 
    if (myTest == []) : 
        Result = 'NULL'
    else:
        Result = str(myTest[0].text)
    return(Result.replace(',',''))



#==============================================================================
#-- LINKEDIN (EMP) : Fonction renvoyant la ville de l'emploi proposé
#==============================================================================

def Get_ville_EMP (Soup):
    myTest = Soup.find_all('span', attrs = {'class':'topcard__flavor topcard__flavor--bullet'}) 
    if (myTest == []) : 
        Result = 'NULL'
    else:
        Result = str(myTest[0].text)
    return(Result.replace(',','')) 
    



#==============================================================================
#-- LINKEDIN (EMP) :Fonction renvoyant la description l'offre d'emploi
#==============================================================================
def Get_Desc_EMP (Soup):
    myTest = Soup.find_all('div', attrs = {"description__text description__text--rich"})
    if (myTest == []) : 
        Result = 'NULL'
    else:
        myTest = str(myTest[0].text)
        if (myTest == []) : 
            Result = 'NULL'
        else:
            Result = myTest
    return(Result)





key=500


myFilePathName = "/home/virus/Documents/TD_DATALAKE/DATALAKE/2_CURATED_ZONE/LINKEDIN/EMP/Data_EMP.csv"
#-- Ouverture du fichier en création
csvfile = open(myFilePathName, "w", encoding = "utf-8")
csvfile.write("id_Emploi"+ ";" + "Nom_Fichier" +  ";" + "Nom_Soc" + ";"+ "Libele_Poste"+ ";" + "description_Poste" + ";" + "ville" )
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
    
    myListeDeLigneAEcrire.append(str(i))
    
    myListeDeLigneAEcrire.append(str(Get_nom_EMP(mySoup)))
    
    myListeDeLigneAEcrire.append(str(Get_libelle_emploi_EMP(mySoup)))
    
    myListeDeLigneAEcrire.append(str(Get_Desc_EMP(mySoup)))
    
    myListeDeLigneAEcrire.append(str(Get_ville_EMP(mySoup)))
    
   
    
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
# dans le path :    "C:/TD_DATALAKE/DATALAKE/2_CURATED_ZONE/LINKEDIN/EMP/Data_EMP.csv"