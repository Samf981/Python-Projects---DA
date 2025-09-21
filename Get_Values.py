class TextAnalzer(object):
    
    def __init__ (self, text):
        # remove punctuation
        new_text = text.replace('.','').replace('!','').replace('?','').replace(',','')
        self.text=new_text.lower()
        
    def freqAll(self):        

        split_string=self.text.split(' ')

        #Create dictionary    
        freqMap = {}
        for word in set(split_string): # use set to remove duplicates in list
            freqMap[word] = split_string.count(word)

        return freqMap    
        
    def freqOf(self,word):
         
        map1=self.freqAll()
        #print (map1)
        return map1.get(word)
        
        

x=input("insert your phrase here: ")
y=input("insert the word to detect here: ")
t=TextAnalzer(str(x))
print(t.freqOf(str(y)))