from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
from datetime import datetime
import os
import shutil
import platform
import getpass
from dotenv import load_dotenv


def GetOS():
    system = platform.system()
    return system


def GetUser():
    user = getpass.getuser()
    return user


def GenerateOSPathProject(os_system):

    load_dotenv()

    if os_system != "Windows":
        user = GetUser()
        source_path = os.environ.get(
            'source_path_linux').replace("//", "/"+user+"/")
        logfiles_path = os.environ.get(
            'logfiles_path_linux').replace("//", "/"+user+"/")
        landing_zone_linkedin_emp_path = os.environ.get(
            'landing_zone_linkedin_emp_path_linux').replace("//", "/"+user+"/")
        landing_zone_glassdoor_soc_path = os.environ.get(
            'landing_zone_glassdoor_soc_path_linux').replace("//", "/"+user+"/")
        landing_zone_glassdoor_avi_path = os.environ.get(
            'landing_zone_glassdoor_avi_path_linux').replace("//", "/"+user+"/")
        linkedin_contains = os.environ.get('linkedin_contains')
        glassdoor_soc_contains = os.environ.get('glassdoor_soc_contains')
        glassdoor_avi_contains = os.environ.get('glassdoor_avi_contains')
        path = os.environ.get('path_linux').replace("//", "/"+user+"/")
        endswith = os.environ.get('endswith')
        contains_1 = os.environ.get('contains_1')
        contains_2 = os.environ.get('contains_2')
        delimiter_path = "/"
        curated_zone_linkedin_emp_path = os.environ.get(
            'curated_zone_linkedin_emp_path_linux').replace("//", "/"+user+"/")
        metadate_file_name_path = logfiles_path+"/metadata-technical.csv"

    elif os_system == "Windows":
        source_path = os.environ.get('source_path_windows')
        logfiles_path = os.environ.get('logfiles_path_windows')
        landing_zone_linkedin_emp_path = os.environ.get(
            'landing_zone_linkedin_emp_path_windows')
        landing_zone_glassdoor_soc_path = os.environ.get(
            'landing_zone_glassdoor_soc_path_windows')
        landing_zone_glassdoor_avi_path = os.environ.get(
            'landing_zone_glassdoor_avi_path_windows')
        linkedin_contains = os.environ.get('linkedin_contains')
        glassdoor_soc_contains = os.environ.get('glassdoor_soc_contains')
        glassdoor_avi_contains = os.environ.get('glassdoor_avi_contains')
        path = os.environ.get('path_windows')
        endswith = os.environ.get('endswith')
        contains_1 = os.environ.get('contains_1')
        contains_2 = os.environ.get('contains_2')
        delimiter_path = "\\"
        curated_zone_linkedin_emp_path = os.environ.get('curated_zone_linkedin_emp_path_windows')
        metadate_file_name_path = logfiles_path+"/metadata-technical.csv"
    return source_path, logfiles_path, landing_zone_linkedin_emp_path, landing_zone_glassdoor_soc_path, landing_zone_glassdoor_avi_path, linkedin_contains, glassdoor_soc_contains, glassdoor_avi_contains, path, endswith, contains_1, contains_2, delimiter_path,curated_zone_linkedin_emp_path,metadate_file_name_path


''' Function to count number of file in a directory '''


def GetFilesPath(path, endswith, delimiter_path):
    count = 0
    list_of_files = []
    # open Files
    for file in os.listdir(path):
        count += 1

    list_dir_path = [x for x in os.listdir(path) if x.endswith(endswith)]

    for Files in range(count):
        list_of_files.append(path+delimiter_path+list_dir_path[Files])

    return list_of_files


def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def file_size(file_path):
    """
    this function will return the file size
    """
    list_file_size = []
    for i in range(len(file_path)):
        if os.path.isfile(file_path[i]):
            file_info = os.stat(file_path[i])

            list_file_size.append(convert_bytes(file_info.st_size))

    return list_file_size


def MakeMetadataFile(file_path, file_size):
    columns_list = ["File_ID", "File_Path_Origin", "File_Size", "File_Date"]
    df = pd.DataFrame(columns=columns_list)
    for i in range(len(file_path)):

        df.loc[i] = [i+1, file_path[i], file_size[i], datetime.now()]

    df.index = df.index + 1

    return df


def MoveFileToLandingZone(source_path, endswith, linkedin_contains, glassdoor_soc_contains, glassdoor_avi_contains, landing_zone_linkedin_emp_path, landing_zone_glassdoor_soc_path, landing_zone_glassdoor_avi_path, logfiles_path, delimiter_path,metadate_file_name_path):

    file_path = GetFilesPath(source_path, endswith, delimiter_path)
    files_sizes = file_size(file_path)
    general_metadata = MakeMetadataFile(file_path, files_sizes)
    file_destination = []
    file_destination_size = []

    for file in general_metadata.File_Path_Origin:
        if linkedin_contains in file:

            file_destination.append(landing_zone_linkedin_emp_path +
                                    file.split(delimiter_path)[-1])

            shutil.copy(file, landing_zone_linkedin_emp_path +
                        file.split(delimiter_path)[-1])

            file_destination_size.append(file_size([landing_zone_linkedin_emp_path +
                                                    file.split(delimiter_path)[-1]]))

        elif glassdoor_soc_contains in file:

            file_destination.append(landing_zone_glassdoor_soc_path +
                                    file.split(delimiter_path)[-1])

            shutil.copy(file, landing_zone_glassdoor_soc_path +
                        file.split(delimiter_path)[-1])

            file_destination_size.append(file_size([landing_zone_glassdoor_soc_path +
                                                    file.split(delimiter_path)[-1]]))

        elif glassdoor_avi_contains in file:

            file_destination.append(landing_zone_glassdoor_avi_path +
                                    file.split(delimiter_path)[-1])

            shutil.copy(file, landing_zone_glassdoor_avi_path +
                        file.split(delimiter_path)[-1])
            file_destination_size.append(file_size([landing_zone_glassdoor_avi_path +
                                                    file.split(delimiter_path)[-1]]))

    general_metadata["File_Path_Destination"] = file_destination
    general_metadata["File_Destination_Size"] = file_destination_size

    general_metadata["File_Destination_Size"] = general_metadata["File_Destination_Size"].apply(
        lambda x: x[0])


    general_metadata.to_csv(metadate_file_name_path,
                            index=None, encoding="utf-8", header=True)

    return general_metadata,



def LoadMetadataFiles(metadate_file_name_path):
    """
    Load metadata files
    """
    metadata = pd.read_csv(metadate_file_name_path)
    return metadata



def GetData(metadate_file_name_path, delimiter_path,curated_zone_linkedin_emp_path):
    ''' Function to get data from html file where the file name contains a specific string (INFO) AND (LINKEDIN) '''

    """
    Call LoadMetadataFiles function
    """
    landing_zone_path = LoadMetadataFiles(metadate_file_name_path)
    
    linkedin_files = landing_zone_path[landing_zone_path["File_Path_Destination"].str.contains("LINKEDIN")]
    len_linkedin_files = len(linkedin_files)
    glassdoor_avis_files = landing_zone_path[landing_zone_path["File_Path_Destination"].str.contains("AVIS-SOC")]
    len_glassdoor_avis_files = len(glassdoor_avis_files)
    glassdoor_soc_files = landing_zone_path[landing_zone_path["File_Path_Destination"].str.contains("INFO-SOC")]
    len_glassdoor_soc_files = len(glassdoor_soc_files)
    
    print("Number of Linkedin files: ", len_linkedin_files)
    print("Number of Glassdoor avis files: ", len_glassdoor_avis_files)
    print("Number of Glassdoor soc files: ", len_glassdoor_soc_files)
    list_of_data = []
    title_file = []
    columns_dataframe = ["file","title","society","city","description"]
    data_title = []
    data_society = []
    data_city = []
    data_country = []
    data_description = []


    for i in linkedin_files["File_Path_Destination"]:
        title_file.append(i)

        
        with open(i, 'r', encoding="utf-8",errors="replace") as f:
            soup = bs(f, 'html.parser')
            title = [i for i in soup.find_all('h1', attrs = {'class':'topcard__title'})]
            title_text = title[0].text
            society = [i for i in soup.find_all('span', attrs = {'class':'topcard__flavor'})]
            society_text = society[0].text
            city = [i for i in soup.find_all('span', attrs = {'class':'topcard__flavor topcard__flavor--bullet'})]
            description = [i for i in soup.find_all('div', attrs = {'class':'description__text description__text--rich'})]
            
            city_text = city[0].text    
            description_text = description[0].text
            data_title.append(title_text)
            data_society.append(society_text)
            data_city.append(city_text)
            data_description.append(description_text)

    data_linkedin = pd.DataFrame(list(zip(title_file,data_title,data_society,data_city,data_description)),columns=columns_dataframe)
    data_linkedin.index = np.arange(1, len(data_linkedin) + 1)

    data_linkedin.to_csv(curated_zone_linkedin_emp_path+"/data_linkedin.csv", index=True,encoding="utf-8",header=True)
    print("Dataframe Linkedin saved in: ", curated_zone_linkedin_emp_path+"/data_linkedin.csv")
