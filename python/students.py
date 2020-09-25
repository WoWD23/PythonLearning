n=int(input('Enter the number of students:'))
data={}     #dictionary
Subjects=('Physics','Mathes','History')     #tuple
for i in range(0,n):
    name=input('Enter the name of the students {}:'.format(i+1)) #get the student's name
    marks=[]    #list
    for x in Subjects:
        marks.append(int(input('Enter marks of {}:'.format(x))))    #add marks
    data[name]=marks    #add dic
for x,y in data.items():
    total=sum(y)
    print("{}'s total score is {}".format(x,total))
    if total<120:
        print(x,"failed :(")
    else:
        print(x,"passed :)")
