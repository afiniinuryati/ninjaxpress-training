# import mymodule

# mymodule.greeting("Afi")
# mymodule.goodbye("Afi")

import math
import datetime

x = math.pi 
print(x)

x = math.sqrt(64)
print(x)

x = math.sin(math.degrees(30))
print(x)

print(datetime.datetime.now())
print(datetime.date.today())

#FILE HANDLING
f = open("file.txt", "w")
f.write("Added text\n")
f.close()

f = open("file.txt", "a")
f.write("Hello!\n")
f.close()

# f = open("file.txt", "r")
# print(f.read())

f = open("file.txt", "r")
print(f.read(5)) #print 5 karakter pertama

f = open("file.txt", "r")
print(f.readline()) #print 1 baris


#QUIZ
import matematika 
print("PI:", matematika.pi)
print(matematika.luas_persegi(sisi=12))