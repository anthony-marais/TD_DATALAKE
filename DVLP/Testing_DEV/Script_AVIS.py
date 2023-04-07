# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 18:08:44 2023

@author: Kousseila 
"""
#==============================================================================
#----------- Path of my cible (chemin de ma cible)
#==============================================================================
mycible_Avi = "C:/TD_DATALAKE/DATALAKE/1_LANDING_ZONE/GLASSDOOR/AVI/"



#==============================================================================
#---- importation des modules 
#==============================================================================
import os,re

from bs4 import BeautifulSoup


myListOfFile = os.listdir(mycible_Avi)

#==============================================================================
#-- GLASSDOOR (SOCIETE) : Fonction renvoyant le nom de l'entreprise
#==============================================================================


def Get_nom_entreprise_AVI (Soup):
    myTest = Soup.find_all('div', attrs = {"class":"header cell info"})[0].span.contents[0]
    if (myTest == []) : 
        Result = 'NULL'
    else:
        Result = myTest
    return(Result)


#==============================================================================
#-- GLASSDOOR (SOCIETE) : Fonction renvoyant date de l'entreprise
#==============================================================================
def Get_date_heure (Soup) :
    myTest = Soup.find_all('time', attrs = {'class':'date subtle small'}) #==> OK
    if (myTest == []) :
        txtclean = 'NULL'
    else:
        txtclean = myTest[0].text
    Result = txtclean.replace(',' , '')
    return(Result)


#==============================================================================
#-- GLASSDOOR (SOCIETE) : Fonction renvoyant le titre de l'avi
#==============================================================================
def Get_titre_AVI (Soup):
    myTest = Soup.find_all('a', attrs = {"class":"reviewLink"})[0].span.contents[0]
    if (myTest == []) : 
              txtclean = 'NULL'
    else:
            txtclean =str(myTest)
            Result = txtclean
            Result = Result.replace('«','')
            Result = Result.replace('»','')
    return(Result.replace('\xa0',''))  


#==============================================================================
#-- GLASSDOOR (SOCIETE) : Fonction renvoyant l'avantage de l'avi - POSITIF
#==============================================================================
def Get_avantage_AVI (Soup):
    
     myTest = Soup.find(text='Avantages').findNext('p').text
    
     if (myTest == []) : 
              Result = 'NULL'
     else:
         
             Result =myTest
             Result =Result.replace(',','.')
             Result = Result.replace('\n','')

     return(Result)


#==============================================================================
#-- GLASSDOOR (SOCIETE) : Fonction renvoyant le Inconvénients de l'avi- NEGATIF
#==============================================================================
def Get_Inconvenients_AVI (Soup):
    
     myTest = Soup.find(text='Inconvénients').findNext('p').text
    
     if (myTest == []) : 
              Result = 'NULL'
     else:
         
             Result =myTest
             Result =Result.replace(',','.')
             Result = Result.replace('\n','')
     return(Result)


#==============================================================================
#-- GLASSDOOR (SOCIETE) : Fonction renvoyant le auteur d de l'avi
#==============================================================================
def Get_auteur_AVI (Soup):
    
     myTest = Soup.find_all('div', attrs = {"class":"author minor"})[0].span.contents[0]
    
     if (myTest == []) : 
              Result = 'NULL'
     else:
         
             Result =str(myTest)
             txtclean = re.sub(r'<span (.*)">(.*)</span>(.*)', r'\2', Result)            
     return(txtclean)


#==============================================================================
#-- GLASSDOOR (SOCIETE) : Fonction renvoyant le localisation de l'avi
#==============================================================================
def Get_loc_AVI (Soup):
    
     myTest = Soup.find_all('span', attrs = {"class":"authorLocation"})
    
     if (myTest == []) : 
              Result = 'NULL'
     else:
         
             txtclean = re.sub(r'<span (.*)">(.*)</span>(.*)', r'\2', str(myTest)) 
             Result = txtclean.replace('[','')
     return(Result)
 
 #==============================================================================
 #-- GLASSDOOR (SOCIETE) : Fonction renvoyant le NOTE MOYENNE de l'avi
 #==============================================================================
def Get_noteM_AVI (Soup) :
     
      myTest = Soup.find_all('div', attrs = {"class":"v2__EIReviewsRatingsStylesV2__ratingNum v2__EIReviewsRatingsStylesV2__large"})
     
      if (myTest == []) : 
               Result = 'NULL'
      else:
          
              txtclean = re.sub(r'<div (.*)">(.*)</div>(.*)', r'\2', str(myTest)) 
              Result = txtclean.replace('[','')
      return(Result)   


#==============================================================================
#-- GLASSDOOR (SOCIETE) : Fonction renvoyant le NOTE  de l'avi
#==============================================================================
def Get_note_AVI (Soup):
     myTest = Soup.find_all('span', attrs = {"class":"gdStars gdRatings sm mr-sm mr-md-std stars__StarsStyles__gdStars"})[0].span.contents[0]

     if (myTest == []) : 
              Result = 'NULL'
     else:
         
             txtclean = re.sub(r'<span class="(.*)" title="(.*)">(.*)</span>(.*)', r'\2', str(myTest)) 
             Result = txtclean.replace('[','')
     return(Result)
      




#==============================================================================
#-- GLASSDOOR (SOCIETE) : Fonction renvoyant le detail note  de l'avi
#==============================================================================
def Get_detailnote_AVI (Soup):
     Malist = []
     MAlistf =['null','null','null','null','null']
     try:
         myTest = Soup.find_all('div', attrs = {"class":"subRatings module stars__StarsStyles__subRatings"})[0]
         myTxtTmp =myTest.find_all('span', attrs = {'class':"gdBars gdRatings med"})
         myTxtTmp2 =myTest.find_all('div', attrs = {'class':"minor"})
     except IndexError:
         
         return(MAlistf)
     if (myTest == [] or len(myTxtTmp2)<=4) : 
              return(MAlistf)
     else:
         for x in range(0, len(myTxtTmp2)) :
             
             txtclean = re.sub(r'<span class="(.*)" title="(.*)"><i>(.*)</i></span>(.*)', r'\2', str(myTxtTmp[x])) 
             #txtclean2 = re.sub(r'<div (.*)">(.*)</div>(.*)', r'\2', str(myTxtTmp2[x])) 

             Result =txtclean.replace('[','')
            
             Malist.append(str(Result))
             
     return(Malist)
      



    
    
key=0

myFilePathName = "C:/TD_DATALAKE/DATALAKE/2_CURATED_ZONE/GLASSDOOR/AVI/Data_Avi.csv"
#-- Ouverture du fichier en création
csvfile = open(myFilePathName, "w", encoding = "utf-8")
csvfile.write("id_avis"+ ";" + "Nom_Fichier" +  ";" + "Nom_Entreprise"+ ";" + "Titre_Avis" + ";" + "Date_Avis" + ";" +
              "Auteur_Avis" + ";" + "Loc_Avis" + ";"  + "Inconvenients" + ";" + "Avantages")
csvfile.write('\n')


#==============================================================================
 
#==============================================================================



myFilePathName = "C:/TD_DATALAKE/DATALAKE/2_CURATED_ZONE/GLASSDOOR/AVI/Data_Note.csv"
#-- Ouverture du fichier en création
csvfile1 = open(myFilePathName, "w", encoding = "utf-8")
csvfile1.write("id_Note"+ ";" + "Nom_Fichier" +  ";" + "Titre_Avis"+ ";"  + "Équilibre travail/vie privée" + ";" + "Culture et valeurs"+";" + "Opportunités de carrière"+ ";" + "émunération et avantages" +  ";" + "Équipe dirigeante"+ ";"  + "Note_moyenne" )
csvfile1.write('\n')




for i in myListOfFile:
        
    myFile = mycible_Avi+str(i)
    print(str(i))
    File = open(myFile, "r", encoding="utf8")
    File_read = File.read()
  
    
    
    mySoup= BeautifulSoup(File_read,'lxml')
    myResult = mySoup.find_all('li', attrs = {'class':'empReview'}) 
    
    for x in range(0, len(myResult)) :
        
        myListeDeLigneAEcrire=[]
        myListeDeLigneAEcrire1=[]
        detail_List=[]
   

        myListeDeLigneAEcrire = []
    #-- Remplissage de la liste
        key=key+1
        
        
        myListeDeLigneAEcrire.append(key)
        
        myListeDeLigneAEcrire.append(str(i))
        
        myListeDeLigneAEcrire.append(str(Get_nom_entreprise_AVI(mySoup)))
        
        myListeDeLigneAEcrire.append(str(Get_titre_AVI(mySoup)))
        
        myListeDeLigneAEcrire.append(str(Get_date_heure(mySoup)))
        
        myListeDeLigneAEcrire.append(str(Get_auteur_AVI(mySoup)))
        
        myListeDeLigneAEcrire.append(str(Get_loc_AVI(mySoup)))
        
        myListeDeLigneAEcrire.append(str(Get_Inconvenients_AVI(mySoup)))
        
        myListeDeLigneAEcrire.append(str(Get_avantage_AVI(mySoup)))
        
        
        
        
        myListeDeLigneAEcrire1.append(key)
        
        myListeDeLigneAEcrire1.append(str(i))
        
        myListeDeLigneAEcrire1.append(str(Get_nom_entreprise_AVI(mySoup)))
        
        myListeDeLigneAEcrire1.append(str(Get_titre_AVI(mySoup)))
        
        
        detail_List=Get_detailnote_AVI(mySoup)
        
        print(detail_List)
        
        myListeDeLigneAEcrire1.append(str(detail_List[0]))
        myListeDeLigneAEcrire1.append(str(detail_List[1]))
        myListeDeLigneAEcrire1.append(str(detail_List[2]))
        myListeDeLigneAEcrire1.append(str(detail_List[3]))
        myListeDeLigneAEcrire1.append(str(detail_List[4]))
       
        myListeDeLigneAEcrire1.append(str(Get_note_AVI(mySoup)))
        
        
        
        
        
        res =str(myListeDeLigneAEcrire)
        res = res.replace('[','').replace(']','')
        res = res.replace(',',';')
        res = res.replace("'",'')
        res = res.replace(' ;',';')
        res = res.replace('; ',';') 
        
        res1 =str(myListeDeLigneAEcrire1)
        res1 = res1.replace('[','').replace(']','')
        res1 = res1.replace(',',';')
        res1 = res1.replace("'",'')
        res1 = res1.replace(' ;',';')
        res1 = res1.replace('; ',';') 
        
        print (res1)
        print("****************************************************************************************")
        csvfile.write(res) 
        csvfile.write('\n')
        csvfile1.write(res1) 
        csvfile1.write('\n')
csvfile.close()
csvfile1.close()

##### -- creation de deux fichier CSV :
   #---- Data_Avi
   # --- Data_Note
# dans le path :C:\TD_DATALAKE\DATALAKE\2_CURATED_ZONE\GLASSDOOR\AVI
#==============================================================================
#---- kousseila -Master 2 BI & A 2022/2023 
#==============================================================================