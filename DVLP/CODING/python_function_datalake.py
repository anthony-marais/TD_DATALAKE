from bs4 import BeautifulSoup as bs
import pandas as pd
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

    return source_path, logfiles_path, landing_zone_linkedin_emp_path, landing_zone_glassdoor_soc_path, landing_zone_glassdoor_avi_path, linkedin_contains, glassdoor_soc_contains, glassdoor_avi_contains, path, endswith, contains_1, contains_2, delimiter_path


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


def MoveFileToLandingZone(source_path, endswith, linkedin_contains, glassdoor_soc_contains, glassdoor_avi_contains, landing_zone_linkedin_emp_path, landing_zone_glassdoor_soc_path, landing_zone_glassdoor_avi_path, logfiles_path, delimiter_path):

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

    general_metadata.to_csv(logfiles_path+"/metadata-technical.csv",
                            index=None, encoding="utf-8", header=True)

    return general_metadata
