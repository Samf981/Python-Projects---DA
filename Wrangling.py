from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page

#Example of HTML code 
html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

soup = BeautifulSoup(html, 'html.parser')   #Parse - whem we have an HTML file the code dosen't know where the <title>
                                            # or <p> tags are. When you parse, it creates a tree of objects

soup.prettify()     #Show the HTML structured

tag_object=soup.title
#print("tag object:",tag_object)

tag_object=soup.h3      #Get the first tag <h3>

tag_child =tag_object.b     #Get the element in bold
parent_tag=tag_child.parent #In this example the father is the <H3> and the <b> is the child
sibling_1=tag_object.next_sibling       #In this case sibling1 is the 'Salary'

sibling_2=sibling_1.next_sibling        

############### HTML TAGS #########################
tag_child['id']     #or tag_child.get('id')

#Using a string to navigate
tag_string=tag_child.string
type(tag_string)        #Confirm the type

unicode_string = str(tag_string)    #Convert to string

table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
table_bs = BeautifulSoup(table, 'html.parser')
table_rows=table_bs.find_all('tr')  #The find function will give all tag's descendents that match with the filter

first_row =table_rows[0]