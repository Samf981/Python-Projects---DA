# STEPS when working with files
#   1   Extract from sources
#   2   Transform : removing and converting to the same format
#   3   Load: Load the data inside a data warehouse

########################    CSV     ##################################
import requests
import pandas as pd
import numpy as np

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv"

# URL do ficheiro online
file_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv"
filename = "addresses.csv"   # nome local do ficheiro para gravar

# Faz o download
response = requests.get(file_url)

if response.status_code == 200:  # check success
    with open(filename, "wb") as f:
        f.write(response.content)  # save the file locally
    #print("File downloaded successfully!")
else:
    #print("Failed to download file:", response.status_code)
    None


df = pd.read_csv("addresses.csv", header=None)

#Add collumns names since df dosen't have yet
df.columns =['First Name', 'Last Name', 'Location ', 'City','State','Area Code']

df["First Name"]        #Select a collumn
df = df[['First Name', 'Last Name', 'Location ', 'City','State','Area Code']]   #Select multiple collumns

#Use loc or iloc to get the intended data
df.iloc[[0,1,2], 0]


########################    JSON     ##################################
import json
person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}

#Write to a Json file (like a dictionary)
with open('person.json', 'w') as f:  # writing JSON object to a file named'person.json'
    json.dump(person, f)


#Write to a Json file (structured)
json_object = json.dumps(person, indent = 4) 
# Writing to sample.json 
with open("sample.json", "w") as outfile: 
    outfile.write(json_object) 

#Reading file
with open('sample.json', 'r') as openfile:
    json_object2 = json.load(openfile)   

#json_object2) 
type(json_object2) 

########################    XLSX     ##################################
import pandas as pd
import urllib.request
urllib.request.urlretrieve("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx", "sample.xlsx")

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx"
filename="file_example_XLSX_10.xlsx"
response = requests.get(url)    #download the fule

#with open(filename, "wb") as f:     #Saves the file locally
        #f.write(response.content)   #Get the file in bynary

#df = pd.read_excel(filename)    #load the file

#read the file without saving it locally:
df = pd.read_excel(url)

import xml.etree.ElementTree as ET  #provides functionality for parsing and creating XML documents. ElementTree represents the XML document as a tree. ~
                                    #We can move across the document using nodes which are elements and sub-elements of the XML file.
# create the file structure
employee = ET.Element('employee')
details = ET.SubElement(employee, 'details')
first = ET.SubElement(details, 'firstname')
second = ET.SubElement(details, 'lastname')
third = ET.SubElement(details, 'age')
first.text = 'Shiv'
second.text = 'Mishra'
third.text = '23'

# create a new XML file with the results
mydata1 = ET.ElementTree(employee)

with open("new_sample.xml", "wb") as files:
    mydata1.write(files)

#Read the XLSX file
df = pd.read_excel("sample.xlsx")

###############Parse the XML file######################
import xml.etree.ElementTree as etree

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Sample-employee-XML-file.xml"

response = requests.get(url)    #download the file

filename="Sample-employee-XML-file.xml"

with open(filename, "wb") as f:     #Saves the file locally
        f.write(response.content)

tree = etree.parse("Sample-employee-XML-file.xml")

# Get the root of the XML tree
root = tree.getroot()

# Define the columns for the DataFrame
columns = ["firstname", "lastname", "title", "division", "building", "room"]

# Initialize an empty DataFrame
datatframe = pd.DataFrame(columns=columns)

#Iterate through each node in the XML root
for node in root:
    # Extract text from each element
    firstname = node.find("firstname").text
    lastname = node.find("lastname").text
    title = node.find("title").text
    division = node.find("division").text
    building = node.find("building").text
    room = node.find("room").text
    
    # Create a DataFrame for the current row
    row_df = pd.DataFrame([[firstname, lastname, title, division, building, room]], columns=columns)
    
    # Concatenate with the existing DataFrame
    datatframe = pd.concat([datatframe, row_df], ignore_index=True)

#print(datatframe)

#To save the dataframe to a csv file:
#datatframe.to_csv("employee.csv", index=False)