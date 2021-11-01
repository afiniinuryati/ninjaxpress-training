def myfunction():
    print("Hello from a function")

# myfunction()

#Python: Function Parameter (Argument)
def myfunction(name):
    print("Hello" + name)

myfunction("James") #hanya boleh 1 data

def myfunction(name=""):
    print("Hello"+name)
myfunction("James")

#kalau mau datanya bisa banyak:
def myfunction(child3, child2, child1): #kalo pake function gak urutan gpp
    print("The youngest child is" + child3)
myfunction(child1="Emil", child2="Tobias", child3="Linus")


#QUIZ
def myfunction():
    x=10
    print("Value inside function:",x)

x = 20
myfunction()
print("Value outside function:",x)
