from python_function_datalake import MoveFileToLandingZone, GetOS,GenerateOSPathProject

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


print(source_path)
print(logfiles_path)
print(landing_zone_linkedin_emp_path)
print(landing_zone_glassdoor_soc_path)
print(landing_zone_glassdoor_avi_path)
print(linkedin_contains)
print(glassdoor_soc_contains)
print(glassdoor_avi_contains)
print(path)
print(endswith)
print(contains_1)
print(contains_2)
print(delimiter_path)

MoveFileToLandingZone(source_path, endswith, linkedin_contains, glassdoor_soc_contains, glassdoor_avi_contains,
                      landing_zone_linkedin_emp_path, landing_zone_glassdoor_soc_path, landing_zone_glassdoor_avi_path, logfiles_path, delimiter_path)