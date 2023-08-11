count=0
Progress_count=0
Trailer_count=0
Retriever_count=0
Excluded_count=0
Progression_outcome=''
l=[]
f=open('w1867624_test.txt','w')
while True:
    try:
        n=int(input('Please enter your credits at pass:'))
        if n==0 or n==20 or n==40 or n==60 or n==80 or n==100 or n==120:        #check the range of pass <=120
            True
        else:
            print('Out of range. Please enter your credits at pass again.')
            continue
        v=int(input('Please enter your credits at defer:'))
        if v==0 or v==20 or v==40 or v==60 or v==80 or v==100 or v==120:     #check the range of defer <=120
            True
        else:
            print('Out of range. Please enter your credits at defer again.')
            continue
        k=int(input('Please enter your credits at fail:'))
        if k==0 or k==20 or k==40 or k==60 or k==80 or k==100 or k==120:     #check the range of fail <=120
            True
        else:
            print('Out of range. Please enter your credits at fail again.')
            continue
    except ValueError: #check the input values are integers
        print('Integer required')
        continue                                                                            

       
    if n+v+k>120:
        print('value out of range') #check the sum of value n+v+k=120
    if n+v+k<120:
        print('The total must need much more credits')
        

    if n==120:
        print('Progress') #check and  print progression outcomes
        Progression_outcome='Progress'
        Progress_count=Progress_count+1 #count how many  progress are input
    elif n==100:
        print('Progress(module trailer)') #check and  print progression outcomes
        Progression_outcome='Progress(module trailer)'
        Trailer_count=Trailer_count+1  #count how many  trailers are input
    elif k>=80:
        print('Exclude')  #check and  print progression outcomes
        Progression_outcome='Exclude'
        Excluded_count=Excluded_count+1   #count how many  excludes are input
    else:
         print('Do not progress – module retriever')  #check and  print progression outcomes
         Progression_outcome='Do not progress – module retriever'
         Retriever_count=Retriever_count+1  #count how many  retrievers are input

    tempList=[]  #open a list and append all the datas in below temporarilly
    tempList.append(Progression_outcome)
    tempList.append(n)
    tempList.append(v)
    tempList.append(k)

    l.append(tempList)

    print('Would you like to enter another set of credits?')
    data=input("Enter 'y' for yes or 'q' to quit and view results:") #yes ,no condition for again enter volume of credits or quit to see results    
    if data=='y':
        continue  #store the first time volume of credits and again loop to the beginning for enter volume of credits 
    elif data=='q':  #user needs to enter q to show below histogram,vertical histogram,volume of credits that have entered and show the volume of credits in text file 
                                 

            
        

            for j in range(len(l)): #get values from tempList and print the volume of credits user takes in the beginning
                print(l[j][0] , ' - ' , l[j][1] , ',' , l[j][2] , ',' , l[j][3])
               
            l=str(l)    
                                        #write in txt file(notepad)
            f.write(l)
            f.close()
             
            
    else:
         print('please kind to be enter the correct string')
         break
