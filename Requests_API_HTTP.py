import os
import requests
from PIL import Image
from IPython.display import IFrame


#Get a request
url='https://www.ibm.com/'
r=requests.get(url)

#Get a response - The status of the request (200 sucess; 404 not found)
r.status_code
r.request.headers   #View headers
header=r.headers   #Headers of request

header['Date']   #Get Date adn Time
header['Content-Type']  #Type of data

#Since the context is text we can use the text function to retrieve info 
r.text[0:100]        #Get first 100 caract.


####### GET IMAGES  ####################

url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'

r=requests.get(url)
path=os.path.join(os.getcwd(),'image.png')

#Save the image in a file in the path assigned
with open(path,'wb') as f:
    f.write(r.content)

Show_image=Image.open(path)     #Dsiplay the image
#Show_image.show()

#####################   POST    ################## - To writte in server

url_post='http://httpbin.org/post'
payload={"name":"Joseph","ID":"123"}
r_post=requests.post(url_post,data=payload)
#print("POST request body:",r_post.request.body)
#print("GET request body:",r.request.body)
print("GET request body:",r_post.request.body)