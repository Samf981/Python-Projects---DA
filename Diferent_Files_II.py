###############     Binary Files - Images   ######################
from PIL import Image 
import urllib.request
urllib.request.urlretrieve("https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg", "dog.jpg")

img = Image.open("dog.jpg") #Open the image

#img.show()     #show the image

###############     Exercise to practice CSV   ######################
import pandas as pd

url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"

df = pd.read_csv(url)

df.shape    #Dimensions: 768,9

#Search missing data - shows a boolean value
missing_data = df.isnull()
print(missing_data.head(5))

#Count the number of missing values
#for column in missing_data.columns.values.tolist():
    #print(column)
    #print (missing_data[column].value_counts())
    #print("")  

df.dtypes   #Check the typses of variables in all collumns

#Visualization
import matplotlib.pyplot as plt
import seaborn as sns

labels= 'Not Diabetic','Diabetic'
plt.pie(df['Outcome'].value_counts(),labels=labels,autopct='%0.02f%%')
plt.legend()
#plt.show()