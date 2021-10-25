# name = input("Enter name: ")
# print("Your name is", name)

# OPERASI TERHADAP TIPE DATA (STRING)
# my_string = "Hello world!"

# print(len(my_string))
# print(my_string[0:5])

# my_string = my_string.replace("world", "friend")
# print(my_string)

a = "Siap "
b = 86
c = a + str(b)
print(c)

nama = "Afi"
alamat = "Cinere"

my_profile = "Nama saya {}, sekarang saya tinggal di {}".format(nama, alamat)
print(my_profile)

#LIST
my_list = []
my_list.append (1)
my_list.append (3)
my_list.append (5)
print(my_list)

d = 5
e = 1000
if d>e:
    print("d is greater than e")
elif d==e:
    print("d and e are equel")
else:
    print("e is greater than d")