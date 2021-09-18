"""
x =5
y = "mahmodul" #data declaration
print(x)
print(y)


x =4
x="mahmodul"  # declared with any particular type, and can even change type after they have been set
print(x)


x = 5
y = 4.5
z ="mahmodul"
print(type(x))  #get the data of variable type
print(type(y))
print(type(z))


a =4
A="mahmud khan"
print(a)
print(A)

#Python name are casesensitive
#python contain  alpha numeric
#its first contain with letter or underscor not number

myvar = "mahmud"
my_var ="khan"
_my_var = "askar"
myVar ="didar"
MyVar ="zaoad"

#all of variable name  different

myVariableName ="partho mam"
# this is camel case
MyVariableName ="Afridi khan"
#this variable name PascalCase


#Multivariable one line
x,y,z = "Orenge","Banana","cherry"
print(x)
print (y)
print(z)

#one variable declear in multivariable name
x=y=z = "mahmud"
print(x)
print(y)
print(z)

#output variable
x ="Awsome"
print("Mahmodul is a " + x)


#we can add two variable  with + sign

x="Bad"
y ="He is not "
z= y + x
print(z)


#Global Variable creat

x ="awsome"
def myfunc():
    print("python is a " + x)
myfunc()


#create inside function and  global variable
x = "Awsome"

def thisfunc():
    x="Good"
    print("she is " + x)  #work in inside value
thisfunc()

print("this is "+x)  #work in global value



x = "awsome"

def  myfunction():
    global x
    x="good"

myfunction()
print("Why you are "+x)
"""
