from python_function_datalake import MoveFileToLandingZone, GetOS,GenerateOSPathProject, GetDataLinkedin, GetDataGlassdoorAvis, GetDataGlassdoorSociety
import click

os_system = GetOS()
path_project = GenerateOSPathProject(os_system)
source_path = path_project[0]
logfiles_path = path_project[1]
landing_zone_linkedin_emp_path = path_project[2]
landing_zone_glassdoor_soc_path = path_project[3]
landing_zone_glassdoor_avi_path = path_project[4]
linkedin_contains = path_project[5]
glassdoor_soc_contains = path_project[6]
glassdoor_avi_contains = path_project[7]
path = path_project[8]
endswith = path_project[9]
contains_1 = path_project[10]
contains_2 = path_project[11]
delimiter_path = path_project[12]
curated_zone_linkedin_emp_path = path_project[13]
metadate_file_name_path = path_project[14]
curated_zone_glassdoor_avis_path = path_project[15]
curated_zone_glassdoor_soc_path = path_project[16]

while True:
    print("1. Move file from source to landing zone")
    print("2. Get data from Linkedin")
    print("3. Get data from Glassdoor avis")
    print("4. Get data from Glassdoor society")

    choice = input("Enter choice(1/2/3/4): ")
    choice = choice.strip()

    if choice == '1':
        MoveFileToLandingZone(source_path, endswith, linkedin_contains, glassdoor_soc_contains, glassdoor_avi_contains,
                              landing_zone_linkedin_emp_path, landing_zone_glassdoor_soc_path, landing_zone_glassdoor_avi_path, logfiles_path, delimiter_path,metadate_file_name_path)
    elif choice == '2':
        GetDataLinkedin(metadate_file_name_path, curated_zone_linkedin_emp_path)
    elif choice == '3':
        GetDataGlassdoorAvis(metadate_file_name_path, curated_zone_glassdoor_avis_path)
    elif choice == '4':
        GetDataGlassdoorSociety(metadate_file_name_path, curated_zone_glassdoor_soc_path)
    else:
        break

