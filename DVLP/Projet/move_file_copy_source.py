# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 17:17:51 2023

@authors: Kousseila / Anthony / Michel 
"""
###----- Path (chemin)
myPathLog = "C:/TD_DATALAKE/LOGFILES/"
mycible_Avi = "C:/TD_DATALAKE/DATALAKE/1_LANDING_ZONE/GLASSDOOR/AVI/"
mycible_SOC = "C:/TD_DATALAKE/DATALAKE/1_LANDING_ZONE/GLASSDOOR/SOC/"
mycible_EMP = "C:/TD_DATALAKE/DATALAKE/1_LANDING_ZONE/LINKEDIN/EMP/"
myPathHtml = "C:/TD_DATALAKE/DATALAKE/0_SOURCE_WEB/"
#==============================================================================
##-----importations de modules Python sys: Fournit l'accès à certaines 
# variables utilisées ou maintenues par l'interpréteur Python et aux 
# fonctions qui interagissent fortement avec le système d'exécution Python.
#==============================================================================
import sys, os, fnmatch,shutil

myListOfFile_Avi = []
myListOfFile_Soc = []
myListOfFile_Emp = []
myListOfFileTmp = []


#==============================================================================
#-- Ramène  (obtenir*) tous les noms des fichiers du répertoire  avec la fonction  
#-- "​os.listdir()" --- *obtenir une liste de tous les fichiers 
#==============================================================================
myListOfFileTmp = os.listdir(myPathHtml)
print(myListOfFileTmp )

#==============================================================================
#------- chargement des fichiers avis
#==============================================================================
myPattern_AVI = "*AVI*.html" 
myPattern_SOC = "*INFO-SOC*.html"
myPattern_EMP = "*INFO-EMP-LINKEDIN*"


for myEntry in myListOfFileTmp :  
    if fnmatch.fnmatch(myEntry, myPattern_AVI):
        myListOfFile_Avi.append(myEntry)
 
    elif  fnmatch.fnmatch(myEntry, myPattern_SOC):
         myListOfFile_Soc.append(myEntry)
        
    elif fnmatch.fnmatch(myEntry, myPattern_EMP):
        myListOfFile_Emp.append(myEntry)
  
    
#==============================================================================
#-------- CHARGEMENT DES FICHIERS  DANS LES  REPERTOIRES DECLARE DANS LE PATH
#==============================================================================
  #--chargement des fichiers AVI
for myFileName_AVI in myListOfFile_Avi :
      filePath = shutil.copy(myPathHtml+ str(myListOfFile_Avi), mycible_Avi)

  #--chargement des fichiers SOC
  
for myFileName_SOC in myListOfFile_Soc :
      filePath = shutil.copy(myPathHtml+ str(myFileName_SOC), mycible_SOC)

  #--chargement des fichiers EMP

for myFileName_EMP in myListOfFile_Emp :
      filePath = shutil.copy(myPathHtml+ str(myFileName_EMP), mycible_EMP)
      
#==============================================================================
# mASTER BI & A  2022/2023  ----- BY O.K 
#==============================================================================