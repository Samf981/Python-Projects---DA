#In this exercise I am going to use the library random User. So I installed it in my terminal
#This library can get me random info: names, email, photos, phones...

from randomuser import RandomUser
import pandas as pd

r = RandomUser()
some_list = r.generate_users(10)

#Using the Get method we can generate a dataset
#for user in some_list:
    #print (user.get_full_name()," ",user.get_email())

#for user in some_list:         
    #print(user.get_picture())

#Get a table with desirable info:
def get_users():
    users =[]
     
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
    return pd.DataFrame(users)     

df1 = pd.DataFrame(get_users())  


############    ANOTHER EXAMPLE - REQUESTS  ############################################
import requests
import json
data = requests.get("https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all")
results = json.loads(data.text)
df2=pd.DataFrame(results)       #Convert JSON fata to pandas data frame

#df2 has the collumn nutrition that contains multiple sub collumns - So we normalize
df3=pd.json_normalize(results)

#Get info from dataframe. 
cherry = df3.loc[df3["name"] == 'Cherry']   #Get line with the name Cherry
(cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])  #Get the values

#How many calories are in a banana?
banana = df3.loc[df3["name"] == 'Banana']   #Get line with the name Cherry
(banana.iloc[0]['name']) , (cherry.iloc[0]['nutritions.protein'])  #Get the values

#EXERCISE 3
import requests
import json
data = requests.get("https://official-joke-api.appspot.com/jokes/ten")
results2 = json.loads(data.text)
df4=pd.DataFrame(results2)
df5=df4.drop(columns=["type","id"],inplace=True)    #Eliminate collums Type and ID
print(df5)