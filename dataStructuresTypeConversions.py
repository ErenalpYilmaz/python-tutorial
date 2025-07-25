### DATA TYPES ###
a = 1 #-->  int
b = "1" #-->  string
c = 1.4 #--> float
d = [1,2,3] #--> list
e = (1,2,3) #--> tuple
f = {
    "name":"Erenalp",
    "surname":"YILMAZ"
} #--> Dictionary
g = True #--> Bool 0/1 True/False
h = None #-->NoneType

z = {1,1,1,1,2,2,2,3,3,3} #--> Benzersizdir.
print(z) #--> output: {1,2,3} 

### CONVERSIONS ###
a = 1
a = str(a)
print(f"a = {type(int(a))}"+f" {type(a)}")

b = "3"
b = int(b)
print(f"b = {type(str(b))}"+f" {type(b)}")