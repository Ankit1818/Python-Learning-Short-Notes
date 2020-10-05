########### Python Basics ###########
************************************* Python Basic To Advance Complite Short Notes ******************************************************************************

"""
Python in in use print() function for print any stament

python in use input() function for get input from user 

print("\U000AF")-> For print unicode + sing change in to 000

->.strip()is using for remove space lsrtip()-> left space remove rstrip()-> use for remove right side space

->find method is use for find any charahter var.find("",index)then after find position

->replace() method is use for replace charcter and String var.replace("Ankit","ankit")

->center method is use for write in center var.center('charlen',"*")
output:**Ankit**

->len function using for count length of string print(len(var))

->.upper() method convert string into upper case

->.lower() method convert in to string lower case

->.title() method is use for convert string into title method

->.count("A") for count string in char
"""
####### Desition Making Stament In Python #########
"""
-> if stament is using for making conditional stamnetnt
if statement:
    print()
else:
    print()

if s:
    pass -> use if condition pass without argument
elif s:
    print()
else:


-> loping stament for use stament reptliy use
two type of loop

for i in range():
    print()

i=0
while i < 10:
    print():
i = i+1

-> int() convert into int
-> str() convert into String
-> float() convert into float
-> char() convert into char
String Formatng .format(,) latest print(f"{var}")
raw string print(r"Smae out put with symbol")
"""
############# Function In Python ##########
"""
Define Function in Pyhton using def key word

def funcname(passing parameter1,passing parameter2..pass..n):
=>
--------------Logic Part Of Function
----Note Function Define var is local they only access in only in function they are dos not work out side of func.
=>

return logicAns
"""


"""
=========> Example Of Function <==========

def total(a,b):
    c = a+b
    return c

print(total(10,10))

Ans ==> 20
"""
############# List Iin Using Method ###########
"""
[::]-> List in Check indexing.
.append()
.extend()
.insert(index,"")
.pop(pos)
.remove("String")
del name[i]
.reverse()
.count()
.min()
.max()
.copy()
.split() string convert in to list
''.join() list convert in to string
in using serch value in list
is chek memory loction of list is same or not
== its chek list is same or not
.sorted()
"""             

"""
Tuple Is Same Work like list but tuple is use in case fix value not change creat after value

syntax:
var = ()

single value tuple('',)

tuple in use list and list in perfom all list method
"""

"""
Dictionary In Python

Syntax:
var = {'Name' : 'Ankit', 'Age' : 8}

-> Dict in dic Access Using Key[]

->.keys()-> For get key value in dic.

->.values()->for get value of value in dic

->.items()-> For get Key And Value Both.


Add Value in dic
dicname['key','key'] = ['v1', 'v2']

pop item in dic
var.pop('key value pair name')

update dic concet to dic
dicname.update(dicname)

fromkey creat dic and pass same value
dicname = dict.formkey([k1,k2], 'valuename')

.get() method using for get key value
print(dic.get('keyname',"You can give Any Message for not found key in this case using"))

.cleare useing for clear dic
dic.clear()

.copy is using for copy dic
newdic = dic.copy()


"""


"""
Set in Python

Syntax:
var = {}

->acess using with index value

->remove duplicate value using .set(value)

->.remove for using remove value .remove(value)

->.add(value) using for add value.

->.discard(value) using sam work like remove

->.copy() for copy set
|-> sing join for two set

set = s1 | s2
print(set)
"""

##############  * Opreter And * args ##############
"""
args Symbols Is * They Type Tuple * is get so many input in tuple format.
ex:
def sum(*args):       args place you can write any name not fixed bustly programmer are use args keyword.
    return args

print(args)


==>Note: * is Tuple Type.

=================  Args With Normal Perameter ====================

many value sum using args

def sum(*args):
    count = 0
    for i in args:
    count += i
    return count

print(sum(1,2,3,4))
=>10

you pass function in list in this * symbol for unpacking

=================== **Kwargs =====================================

for pass keyword agrument and  get as dicrtionary
Ex:

def name(**kwargs):
    return kwargs

print(name(Ankit,Goswami))

Output ==> Ankit:key Goswami:value
    
"""
###################### Lembda Function ###########################

"""

Lambda Function Other Name Is Anonumous Function This Is same Work As A Like Function but not requrid def keyword.
Lambda Function Can Store In variable
Lambda Mostly Use Lembda
EX:
var = lambda a,b: a+b
print(var(5,5))

"""
#################### Inbuilt Function In Python ####################
"""
==> enumerate() is Function This Function Use With Loop For Get index position.
Ex:

name = "ANK"

for i,d in enumerate(name):
    print(i,d)
    
>>>>>>>>>OUTPUT:
0 A
1 N
2 K

==> map() is Function This Function Use with def function for creat list with out in multi value.

Ex:

li = [1,2,3,4]

def squ(a):
    return a**2

ch = list(map(squ,li))
print(ch)

>>>>>>>>>>>Output:
[1, 4, 9, 16]


==> Filter () is Fuction This Function Use For Filter Value.

Ex:

def li(d):
    return d%2 == 0

it = [1,2,3,4,5,6,7,8,9]
odd = []

chh = list(filter(li,it))
print(chh)

>>>>>>>Output:
[2, 4, 6, 8]         

==> zip () is function use for zip data.

Ex:

userid = ["u1","u2","u3"]
username = ["Ankit", "Uday", "Nirav"]

zi = list(zip(userid,username))



>>>>>>>>Output:
[('u1', 'Ankit'), ('u2', 'Uday'), ('u3', 'Nirav')]

"""
################ Decoreters ###############
"""
Decoretre Are Use For Increse Function In Funcanality.
Ex

=======================================================)>)  you can pass with arguments
def fun1():-------------------------------------> You Can Passs Argument:A
    print("Ankit")


def mainn(Any_Func):
    def Vio():------------------------------->>In This Pass *args,**kwargs
        print("Python")
        Any_Finc()--------------------------------------------------------------->>In This Pass *args,**kwargs with return
    return Vio
vvr = mainn(fun1)
print(vvr)
>>>>>Output:
python
Ankit
"""
############### Genreters In Pyhton ###############

"""
Genretre is use for memory perpose          
Ex:
i = [1,2,3,4,5,6,7,8,9]               -----------------> This is Iteroter.
g = iter(i)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

>>>>>>>Output:
1
2
3
4
5
6
7
8
9
"""
############## Python OOP ##############
         (Python Object Orianted Programming)

Python OOPs Concept is very usefull in real life project.

-> How To defie class:
 class name:
	class person:
    def __init__(self,fname,mname,lname):
        # instance Variable
        self.fname = fname
        self.mname = mname
        self.lname = lname


p1 = person("Ankit", "Rajeshbhai", "Goswami")
print(p1.fname)

>>>>>>>>>>> OUTPUT >>>>>>>>>>>
Ankit

-> How To Define Class Veriable: They Use in This case use value is fix.

class name:
	lname = "Any"     ----> Class Veriable
	class person:
    def __init__(self,fname,mname):
        # instance Variable
        self.fname = fname
        self.mname = mname
        return f"{self.fname}{self.mname}{name.lname}"  ----> class veriable access using with class name
					  -----------


-> Define Class Method
 @classmethod
	def name(clas,pera)
	return cls(ret)

-> Static method
  same class method
@staticmathod




--------> Inherit Class And Multi Level Inheritens

class phone:



class child(phone): ->inherit class

def __init__(self,para):
 two way inherit
  1.phone.__init__(self,para)
  2.super()
.__init__(para)->without parameter



EX:
class  person:
    def __init__(self,name):

        self.name = name



class inherit(person):
    def __init__(self,name,nname):
        
        person.__init__(self,name)
        self.nname = nname


class in2(inherit):
	def __init__(self,name,nname,nnname):
	inherit.__init__(self,name,nname)


p1 = person("Ankit")
print(p1.name)

p2 = inherit("Ankit")
print(p2.name)


-------> Method Over Rididng  <----------------------

same method over ride in this case

Ex:

class a:
  def m(self):
	print("Class A")

class b(a):
	def m(self):
	print("Class b")

ob1 = a()
print(ob1.m())

ob1 = b()
print(ob1.m())


###### Meteod Overloding ########
EX:
def m(a,b,c):
	if a != none and b != none and c != none:
		return a+b+c
	elif a != none and b!= none:
		return a**b
	else:
		print("You Can pass Only Value C")


######### Clouser  ###########

EX:
def a(x):
 def b(y):
	return x**Y

v = a(5)
print(v(2))

###### Buit In Error And Exeption ########

#Syntax Error:

""" Misiing Any Componet in Syntax That Time Run Syntax Error """

#Raise Error

def add(a,b):
    if (type(a) is int) and (type(b) is int) :
        return a+b
    raise TypeError("Some One Roung !")


# finaly Block Always Run............

# Exeption hendling
while True:
    try:
    age = input("Enter Your Age: ")
    break
except ValueError:
    print("Invelid Input")
except:
    print("You Went to Wrong")

if age < 18:
    print("YES")
else:
    print("NO")


#python debuging

    first import pdb


    than after use can use pdb for find bug in code.
    pdb.set_trace()

    command
    n -> next line exe
    c -> continue exe
    q -> quit


###### Open Read File (File Hendling) ##########
""" Working With File Like Reaad And Write Etc... """
# EX:


f = open('hello.txt')  #-------> open('file name/path') Function Use For open File
print(f.read())  #-------------------> For Read File Using read() Function.
print(f.tell())  #-------------------> For Read COurser Position.
print(f.readline())  #------------> readline() Function Read Only one Function.
print(f.readlines())  #------------> readlines() Function use for they convert in all line in list.
print(f.name) #---------> name use for know working file name.
print(f.read())
f.close()     #----------------> close() Function Use For Close File. Always Close File After Work.
print(f.closed)



############ Other METHOD WORKING with FILE #################


with open('hello.txt', 'r+', encoding = 'utf-8') as d:
    print(d.encoding)
    d.write("You Are hacked")
    d.append("Haha")


'w' FOR WRITE FILE
'r' FOR READ FILE.
'a' APPEND WORD IN FILE
'r+' READ AND WRITE BOUTH


encoding in this senerio in use like work with uniocode file.
    




################ WORKING WITH CSV(COMM SPRETED VALUE) FILE READ,WRITE #################






from csv import reader

with open("data.csv", "r") as f:
    red = reader(f)
    for i in red:
        print(i)



        
from csv import DictReader

with open("data.csv", "r") as f:
    red = DictReader(f, delimiter='|')
    for i in red:
        print(i)





from csv import DictWriter

with open("data.csv", "w") as f:
    red = DictWriter(f, fildnames=['fname','lname'])
    red.writeheader()
    red.writerow({
    'fname' : 'Ankit'
        })



from csv import writer

with open("data.csv", "w") as f:
    red = writer(f)
    red.writerow(['name','gov'])
    red.writerows([['name','gov','data']])






################ WORKING OS(OPRETING SYSTEM) MODULE ########################

---> THIS MODULE IS VERY IMPORTENT WORKING WITH OS IN REALWORLD APPLICATION 


---> THEY WORKING AS A LIKE CMD.


import os

print(os.getcwd())-------> GET CORRENT CHANGE WORKING DIRECTRY.
os.mkdir("Ankit")  -------> MAKE FOLDER.
os.chdir()    -------> USING FOR CHANGET DIRECTRY.("IN ADD PATH")


																		Creat By: Ankit Goswami
																	     ankitgoswami1818@gmail.com
