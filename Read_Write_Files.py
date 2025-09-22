example1 = "example1.txt"
file1 = open(example1, "r")
#When rading a file, if I read the first line, next time I read the file in the same file it will start in the second line. 
# It uses pointers~.



#Read file (r means read, w means write)
with open(example1, "r") as file1:

    #Read the whole file
    FileContent = file1.read()
    #print(FileContent)

    #Read 4 characters
    #print(file1.read(4))
    
    #Read one line
    #print(file1.readline())

    #To read and get all the lines
    i = 0
    for line in file1:
        print("Iteration", str(i), ": ", line)
        i = i + 1
        
    #Read the second line: (This need to be at top of the code to run)
    #If it runs here, since the pointer of the file is in the end of the file, it won't work.
    #FileasList = file1.readlines()
    #print(FileasList[1])

#Close the file
file1.close()


#Setting the open with 'w' means he will overwrite the existing data
exmp2 = 'Example2.txt'
with open(exmp2, 'w') as writefile:
    #Write a line - Only writes in the first line
    #writefile.write("This is line A2")

    #This way we can write in several line: \n
    #writefile.write("This is line A\n")
    #writefile.write("This is line B\n")

#Write several lines
    Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
    #for line in Lines:
        #writefile.write(line)


#Add text - Apend:
with open(exmp2, 'a') as testwritefile:
    testwritefile.write("This is line C\n")
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n")

with open(exmp2, 'r') as testwritefile:   
    print(testwritefile.read())

# Copy file to another
#exmp3 = 'Example3.txt'
#with open(exmp2,'r') as readfile:
    #with open(exmp3,'w') as writefile:
          #for line in readfile:
                #writefile.write(line)


#Use truncate() to end the data. Reduce THe file size
with open(exmp2, 'r+') as testwritefile:
    testwritefile.seek(0,0) #write at beginning of file
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("Line 4" + "\n")
    testwritefile.write("finished\n")
    

     #Uncomment the line below
    #testwritefile.truncate()
    testwritefile.seek(0,0)
    print(testwritefile.read())