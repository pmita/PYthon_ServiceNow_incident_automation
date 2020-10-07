#Need to install requests and pandas package for python
import requests
import json
import pandas as pd

 # Set the request parameters
url = 'https://yourdeveloperinstance.service-now.com/api/now/table/incident'
user = 'yourusername'
pwd = 'yourpassword'
 
 # Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

#Grab list of incidents from excel
incident_list = pd.read_excel('yourlocation/raise_tickets.xlsx')
#Save each column to a self-describing variable
short_descriptions = incident_list['SHORT_DESCRIPTION']
descriptions = incident_list['DESCRIPTION']
companies = incident_list['COMPANY']
locations = incident_list['LOCATION']

 
#Initiate an variable for our json structure
data_to_pass = {}
for excel_index in range(len(impacts)):
    data_to_pass['short_description'] = short_descriptions[excel_index]
    data_to_pass['description'] = descriptions[excel_index]
    data_to_pass['company'] = companies[excel_index]
    data_to_pass['location'] = locations[excel_index]
    json_data_to_pass = json.dumps(data_to_pass)

    print(json_data_to_pass)

    # Do the HTTP request passing the above details
    response = requests.post(url, auth=(user, pwd), headers=headers ,data=json_data_to_pass)
 
    # Check for HTTP codes other than 200
    if response.status_code != 201: 
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()
 
    # Decode the JSON response into a dictionary and use the data
    print('Status:',response.status_code,'Headers:',response.headers,'Response:',response.json())
