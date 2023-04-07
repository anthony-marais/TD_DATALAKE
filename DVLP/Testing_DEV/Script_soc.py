# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 18:54:25 2023

@author: Kousseila
"""
import os
import re

import pandas as pd

from bs4 import BeautifulSoup


mycible_SOC = "C:/TD_DATALAKE/DATALAKE/1_LANDING_ZONE/GLASSDOOR/SOC/"
myListOfFile = os.listdir(mycible_SOC)


# ==============================================================================
# -- GLASSDOOR (SOCIETE) : Fonction renvoyant le nom de l'entreprise
# ==============================================================================

def Get_nom_entreprise_SOC(Soup):
    myTest = Soup.find_all('h1', attrs={'class': "strong tightAll"})[0]

    if (myTest == []):
        Result = 'NULL'
    else:
        myTxtTmp = str(myTest)
        myTxtTmp1 = re.sub(
            r'(.*)<h1 class="strong tightAll" data-company="(.*)" title="">(.*)', r'\2', myTxtTmp)
        Result = myTxtTmp1
    return(Result)


# ==============================================================================
# -- GLASSDOOR (SOCIETE) : Fonction renvoyant la ville de l'entreprise
# ==============================================================================


def Get_ville_entreprise_SOC(Soup):
    myTest = str(Soup.find_all('div', attrs={'class': "infoEntity"})[
                 1].span.contents[0])

    if (myTest == []):
        Result = 'NULL'
    else:
        myTxtTmp = str(myTest)
        myTxtTmp1 = re.sub(
            r'(.*)<h1 class=" strong tightAll" data-company="(.*)" title="">(.*)', r'\2', myTxtTmp)
        Result = myTxtTmp1
    return(Result)


# ==============================================================================
# -- GLASSDOOR (SOCIETE) : Fonction renvoyant la taille de l'entreprise
# ==============================================================================

def Get_taille_entreprise_SOC(Soup):
    myTest = str(Soup.find_all('div', attrs={'class': "infoEntity"})[2].span.contents[0])
    if (myTest == []):
        Result = 'NULL'
    else: 
        myTxtTmp = str(myTest)
        myTxtTmp1 = re.sub(r'(.*)<h1 class=" strong tightAll" data-company="(.*)" title="">(.*)', r'\2', myTxtTmp)
        Result = myTxtTmp1
    return(Result)


# ==============================================================================
# -- GLASSDOOR (SOCIETE) : Fonction renvoyant le revenu de l'entreprise
# ==============================================================================

 #def Get_revenu_SOC(Soup):

   #  myTest = str(Soup.find_all('div', attrs={'class': "infoEntity"})[
   #              5].span.contents[0])

   #  if (myTest == []):
    #     Result = 'NULL'
   #  else:
   #      myTxtTmp = str(myTest)
   #      myTxtTmp1 = re.sub(
   #         r'(.*)<h1 class=" strong tightAll" data-company="(.*)" title="">(.*)', r'\2', myTxtTmp)
   #      Result = myTxtTmp1
   #  return(Result)


# ==============================================================================
# -- GLASSDOOR (SOCIETE) : Fonction renvoyant le secteur de l'entreprise
# ==============================================================================

def Get_secteur_SOC(Soup):

    myTest = Soup.find(text='Secteur').findNext('span').text

    if (myTest == []):
        Result = 'NULL'
    else:

        Result = myTest

    return(Result)


# ==============================================================================
# -- GLASSDOOR (SOCIETE) : Fonction renvoyant le type de l'entreprise
# ==============================================================================

#def Get_Type_SOC(Soup):

  #  myTest = Soup.find(text='Type').findNext('span').text

  #    if (myTest == []):
   #       Result = 'NULL'
   #   else:

   #       Result = myTest

  #    return(Result)


# ==============================================================================
# -- GLASSDOOR (SOCIETE) : Fonction renvoyant la fondation de l'entreprise
# ==============================================================================
def Get_fondation_SOC(Soup):
    foundation_text = Soup.find(text=['Fondé en', 'Créé en dans les années','existe depuis' ])
    if foundation_text:
        foundation_date = foundation_text.findNext('span').text
        return foundation_date
    else:
        Result = foundation_text
    return(Result)

    # return 'NULL'

#Get_fondation_SOC = pd.to_datetime(Get_fondation_SOC)


# ==============================================================================
# -- GLASSDOOR (SOCIETE) : Fonction renvoyant le site web de l'entreprise
# ==============================================================================

def Get_SiteWeb_SOC(Soup):
    myTest = str(Soup.find_all('div', attrs={'class': "infoEntity"})[0].text)

    if (myTest == []):
        Result = 'NULL'
    else:
        myTxtTmp = str(myTest)
        myTxtTmp1 = re.sub(
            r'(.*)<h1 class=" strong tightAll" data-company="(.*)" title="">(.*)', r'\2', myTxtTmp)
        Result = myTxtTmp1
    return(Result.replace('Site Web', ''))


# ==============================================================================
# -- GLASSDOOR (SOCIETE) : Fonction renvoyant la description de l'entreprise
#
# ==============================================================================

def Get_description_entreprise_SOC(Soup):
    #myTest = str(mySoup.find_all('div', attrs = {'class':"infoEntity"})[1].span.contents[0])
    myTest = str(Soup.find_all('div', attrs={'id': "EmpBasicInfo"}))
    myTest2 = myTest.find_all('div', attrs={'class': ""})
    # ..........................................
    # ..
    # ... coder eventuellement des choses ici
    # .......
    # ..........................................
    if (myTest == []):
        Result = 'NULL'
    else:
        #Soup2 = Soup(myTest, 'lxml')
        #myTxtTmp = str(Soup2.find_all('div', attrs = {'class':""})[2])
        #myTxtTmp1 = re.sub(r'(.*)data-full="(.*).<br/>(.*)', r'\2', myTxtTmp)
        #Result = myTxtTmp1
        Result = myTest2
    return(Result)






# ==============================================================================
# -- Write CSV  files
#
# ==============================================================================

key = 0

myFilePathName = "C:/TD_DATALAKE/DATALAKE/2_CURATED_ZONE/GLASSDOOR/SOC/Data_Soc.csv"
# -- Ouverture du fichier en création
csvfile = open(myFilePathName, "w", encoding="utf-8")
csvfile.write("id_Entreprise" + ";" + "Nom_Fichier" + ";" + "Nom_Entreprise" + ";" + "Site_Web" + ";" + "Siège_social" + ";" 
      + "Secteur" + ";"+ "Annee_Creation"  )

#csvfile.write("id_Entreprise" + ";" + "Nom_Fichier" + ";" + "Nom_Entreprise" + ";" + "Site_Web" + ";" + "Siège_social" + ";" +
 #             "Type_Entreprise" + ";" + "Taille_Entreprise" + ";" + "Annee_Creation" + ";" + "Secteur" + ";" + "Revenu" + ";")
csvfile.write('\n')


for i in myListOfFile:

    myFile = mycible_SOC+str(i)
    File = open(myFile, "r", encoding="utf8")
    File_read = File.read()

    mySoup = BeautifulSoup(File_read, 'lxml')

    myListeDeLigneAEcrire = []
# -- Remplissage de la liste
    key = key+1

    myListeDeLigneAEcrire.append(key)

    myListeDeLigneAEcrire.append(str(i))

    myListeDeLigneAEcrire.append(str(Get_nom_entreprise_SOC(mySoup)))

    myListeDeLigneAEcrire.append(str(Get_SiteWeb_SOC(mySoup)))

    myListeDeLigneAEcrire.append(str(Get_ville_entreprise_SOC(mySoup)))

 #     myListeDeLigneAEcrire.append(str(Get_Type_SOC(mySoup)))

 #     myListeDeLigneAEcrire.append(str(Get_taille_entreprise_SOC(mySoup)))

    myListeDeLigneAEcrire.append(str(Get_secteur_SOC(mySoup)))

 #     myListeDeLigneAEcrire.append(str(Get_revenu_SOC(mySoup)))
    myListeDeLigneAEcrire.append(str(Get_fondation_SOC(mySoup)))

    # myListeDeLigneAEcrire.append(str(Get_note(soup)))

    

    res = str(myListeDeLigneAEcrire)
    res = res.replace('[','').replace(']','')
    res = res.replace(',',';')
    res = res.replace('; ',';')
    res = res.replace("'",'')
    res = res.replace('; ', ';')
    res = res.replace(' ;', ';')
#  res = str(myListeDeLigneAEcrire)
 #    res = res.replace('[', '').replace(']', '')
 #    res = res.replace(',', ';')
 #    res = res.replace('; ', ';')
  #   res = res.replace("'", '')
  #   res = res.replace('"', '')
 #    res = res.replace(' ;', ';')
 #    res = res.replace('; ', ';')
  #   res = res.replace('; ', ';')
 #    res = res.replace('; ', ';')
    
    print(res)
    print("****************************************************************************************")
    csvfile.write(res)
    csvfile.write('\n')
csvfile.close()

# -- création  fichier CSV :
#---- Data_Soc.csv

# dans le path :C:/TD_DATALAKE/DATALAKE/2_CURATED_ZONE/GLASSDOOR/SOC/Data_Soc.csv
