from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
from datetime import datetime
import os
import shutil
import platform
import getpass
from dotenv import load_dotenv
from tqdm import tqdm
import re
import pytz


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
        curated_zone_glassdoor_avis_path = os.environ.get(
            'curated_zone_glassdoor_avis_path_linux').replace("//", "/"+user+"/")

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
        curated_zone_linkedin_emp_path = os.environ.get(
            'curated_zone_linkedin_emp_path_windows')
        metadate_file_name_path = logfiles_path+"/metadata-technical.csv"
        curated_zone_glassdoor_avis_path = os.environ.get(
            'curated_zone_glassdoor_avis_path_linux').replace("//", "/"+user+"/")

    return source_path, logfiles_path, landing_zone_linkedin_emp_path, landing_zone_glassdoor_soc_path, landing_zone_glassdoor_avi_path, linkedin_contains, glassdoor_soc_contains, glassdoor_avi_contains, path, endswith, contains_1, contains_2, delimiter_path, curated_zone_linkedin_emp_path, metadate_file_name_path, curated_zone_glassdoor_avis_path


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


def MoveFileToLandingZone(source_path, endswith, linkedin_contains, glassdoor_soc_contains, glassdoor_avi_contains, landing_zone_linkedin_emp_path, landing_zone_glassdoor_soc_path, landing_zone_glassdoor_avi_path, logfiles_path, delimiter_path, metadate_file_name_path):

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


def GetDataLinkedin(metadate_file_name_path, curated_zone_linkedin_emp_path):
    ''' Function to get data from html file where the file name contains a specific string (LINKEDIN) '''

    """
    Call LoadMetadataFiles function
    """
    landing_zone_path = LoadMetadataFiles(metadate_file_name_path)

    linkedin_files = landing_zone_path[landing_zone_path["File_Path_Destination"].str.contains(
        "LINKEDIN")]
    len_linkedin_files = len(linkedin_files)

    print("Number of Linkedin files: ", len_linkedin_files)

    list_of_data = []
    title_file = []
    columns_dataframe = ["file", "title", "society", "city", "description"]
    data_title = []
    data_society = []
    data_city = []
    data_country = []
    data_description = []

    print("\n")

    for i in tqdm(linkedin_files["File_Path_Destination"], desc="Loading...", ascii=False, ncols=75, bar_format="{l_bar}{bar:20}{r_bar}", colour="green"):
        title_file.append(i)

        with open(i, 'r', encoding="utf-8", errors="replace") as f:
            soup = bs(f, 'html.parser')
            data_title.append(soup.find_all(
                'h1', attrs={'class': 'topcard__title'})[0].text)
            data_society.append(soup.find_all(
                'span', attrs={'class': 'topcard__flavor'})[0].text)
            data_city.append(soup.find_all(
                'span', attrs={'class': 'topcard__flavor topcard__flavor--bullet'})[0].text)
            data_description.append(soup.find_all(
                'div', attrs={'class': 'description__text description__text--rich'})[0].text)

    print("Number of Linkedin files process: ", len_linkedin_files, "\n")
    data_linkedin = pd.DataFrame(list(zip(
        title_file, data_title, data_society, data_city, data_description)), columns=columns_dataframe)
    data_linkedin.index = np.arange(1, len(data_linkedin) + 1)
    data_linkedin.to_csv(curated_zone_linkedin_emp_path +
                         "/data_linkedin.csv", index=True, encoding="utf-8", header=True)
    print("Dataframe Linkedin saved in: ",
          curated_zone_linkedin_emp_path+"/data_linkedin.csv")
    print("\n")


def GetDataGlassdoorAvis(metadate_file_name_path, curated_zone_glassdoor_avis_path):
    ''' Function to get data from html file where the file name contains a specific string (AVIS-SOC) '''

    landing_zone_path = LoadMetadataFiles(metadate_file_name_path)
    glassdoor_avis_files = landing_zone_path[landing_zone_path["File_Path_Destination"].str.contains(
        "AVIS-SOC")]
    len_glassdoor_avis_files = len(glassdoor_avis_files)
    print("Number of Glassdoor avis files: ", len_glassdoor_avis_files)

    list_data_avis = []
    columns_dataframe_avis = ["file", "society", "date", "avis_positif",
                              "avis_negatif", "status", "poste", "localisation", "mean_rate", "general_rate"]
    title_avis = []
    avis_society = []
    date_avis_glassdoor = []
    avis_positif_list = []
    avis_negatif_list = []
    status_list = []
    poste_list = []
    localisation_list = []
    mean_rate_list = []
    rate_list = []

    print("\n")

    for i in tqdm(glassdoor_avis_files["File_Path_Destination"], desc="Loading...", ascii=False, ncols=75, bar_format="{l_bar}{bar:20}{r_bar}", colour="green"):
        title_avis.append(i)
        with open(i, 'r', encoding="utf-8", errors="replace") as f:
            soup = bs(f, 'html.parser')
            list_data_avis.append([i for i in soup.find_all(
                'p', attrs={"class": "h1 strong tightAll"})][0].text)
            date_avis_glassdoor.append([i for i in soup.find_all(
                'time', attrs={'class': 'date subtle small'})][0].text)
            avis_positif_list.append([i for i in soup.find(string='Avantages').findNext('p')][0].text if len(
                [i for i in soup.find(string='Avantages').findNext('p')]) > 0 else "None")
            avis_negatif_list.append([i for i in soup.find(string='Inconvénients').findNext(
                'p')][0].text if len([i for i in soup.find(string='Avantages').findNext('p')]) > 0 else "None")
            status_list.append([i for i in soup.find_all('span', attrs={
                               "class": "authorJobTitle middle reviewer"})][0].text.split("-")[0].strip())
            poste_list.append([i for i in soup.find_all('span', attrs={"class": "authorJobTitle middle reviewer"})][0].text.split(
                "-")[1].strip() if len([i for i in soup.find_all('span', attrs={"class": "authorJobTitle middle reviewer"})][0].text.split("-")) > 1 else "None")
            localisation_list.append([i for i in soup.find_all('span', attrs={"class": "authorLocation"})][0].text if len(
                [i for i in soup.find_all('span', attrs={"class": "authorLocation"})]) > 0 else "None")
            mean_rate_list.append([i for i in soup.find_all('div', attrs={
                                  "class": "v2__EIReviewsRatingsStylesV2__ratingNum v2__EIReviewsRatingsStylesV2__large"})][0].text)
            rate_list.append(re.sub(
                r'<span class="(.*)" title="(.*)">(.*)</span>(.*)', r'\2', str(soup.find_all('span', attrs={
                    "class": "gdStars gdRatings sm mr-sm mr-md-std stars__StarsStyles__gdStars"})[0].span.contents[0])))

    print("Number of Glassdoor avis files process: ",
          len_glassdoor_avis_files, "\n")
    data_glassdoor_avis = pd.DataFrame(list(zip(title_avis, list_data_avis, date_avis_glassdoor, avis_positif_list,
                                       avis_negatif_list, status_list, poste_list, localisation_list, mean_rate_list, rate_list)), columns=columns_dataframe_avis)
    data_glassdoor_avis.index = np.arange(1, len(data_glassdoor_avis) + 1)
    data_glassdoor_avis.to_csv(
        curated_zone_glassdoor_avis_path+"/data_glassdoor_avis.csv", index=True, encoding="utf-8", header=True)
    print("\n")

    print("Dataframe avis glassdoor saved in: ",
          curated_zone_glassdoor_avis_path+"/data_glassdoor_avis.csv")
    print("\n")
