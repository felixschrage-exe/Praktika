import tkinter

var1 = 64 # this is an integer
var2 = 3.1415 # this is a float
var3 = "this is a string"
var4 = f"this is a formatted string"
var5 = 'this is also a string'
var6 = ["this", "is", "a", "list"]
var7 = ("this", "is", "a", "tuple")
var8 = "this", "is", "also", "a", "tuple", "for", "some", "odd", "reason"
var9 = { "this" : "is", "a" : "dictionary" }
var10 = tkinter.Tk() # this is an instance of an class (an object)

#----------------------------------------------------------------------------------------#

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2 # list2 gets added to the end of list1 --> [1, 2, 3, 4, 5, 6]
print(list3)

#----------------------------------------------------------------------------------------#

tpl1 = 1, 2, 3
tpl2 = 4, 5, 6
tpl3 = tpl1 + tpl2
print(tpl3)

#----------------------------------------------------------------------------------------#

test1 = list(tpl1) + list1
test2 = tuple(list1) + tpl1
print(test1, test2)

#----------------------------------------------------------------------------------------#

dict1 = {
    "marke" : "porsche",
    "modell" : "911 GT3 RS",
    "baujahr" : 2024
}

dict2 = {
    "marke" : "porsche",
    "modell" : "911 GT3 RS",
    "baujahr" : 2020
}

# dict3 = dict1 + dict2 #!

#----------------------------------------------------------------------------------------#
