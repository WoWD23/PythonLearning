#learn from lanqiao

import sys
from collections import Counter 

class Person(object):
    """
    Return a Person object with a given name.
    """

    def __init__(self,name):
        self.name = name

    def get_details(self):
        """
        Return a String containing a name
        """
        return self.name
    def get_grade(self):
        return 0

class Student(Person):
    """
    Return the Student object with three parameters:name,brand,year
    """
    def __init__(self,name,branch,year,grade):
        Person.__init__(self,name)
        self.branch = branch
        self.year = year
        self.grade = grade

    def get_details(self):
        """
        Return a string containing specific information for studens
        """
        return "{} studies {} and is in {} year.".format(self.name,self.branch,self.year)

    def get_grade(self):

        common = Counter(self.grade).most_common(4)
        n1 = 0
        n2 = 0
        for item in common:
            if item[0] != 'D':
                n1 += item[1]
            else:
                n2 += item[1]
        print("Pass: {},Fail: {}".format(n1,n2))

class Teacher(Person):
    """
    Return the Teacher object and use the string list as the parameter
    """
    def __init__(self,name,papers,grade):
        Person.__init__(self,name)
        self.papers = papers
        self.grade = grade

    def get_details(self):
        return "{} teaches {}".format(self.name,','.join(self.papers))

    def get_grade(self):
        s = []
        common = Counter(self.grade).most_common(4)
        for i,j in common:
            s.append("{}: {}".format(i,j))
        print(', '.join(s))

person1=Person('Sachin')
if sys.argv[1] == 'student':
    student1 = Student('Kushal','CSE',2005,sys.argv[2])
    student1.get_grade()
else:
    teacher1 = Teacher('Prashad',['C','C++'],sys.argv[2])
    teacher1.get_grade()











