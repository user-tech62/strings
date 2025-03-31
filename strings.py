#strings

# .swapcase

def lower():
    name=input("enter name:")
    print(name.lower())
lower()

# .upper()

def upper():
    movie=input("enter movie:")
    print(movie.upper())
upper()

# .capitalize

def capitaliza():
    name=input("enter name:")
    print(name.capitalize())
capitaliza()

# .title

def title():
    sen=input("enter sen:")
    print(sen.title())
title()

# .swapcase

def swapcase():
    name=input("enter name:")
    print(name.swapcase())
swapcase()

# islower()

def islow():
    name=input("enter name:")
    print(name.islower())
islow()

# isupper

def isupper():
    name=input("enter name:")
    print(name.isupper())
isupper()

# istitle

def istitle():
    name=input("enter name:")
    print(name.istitle())
istitle()

# isalpha

def isalpha():
    name=input("enter name:")
    print(name.isalpha())
isalpha()

# isalnum

def isalnum():
    name=input("enter name:")
    print(name.isalnum())
isalnum()

# isdigit

def isdigit():
    name=input("enter name:")
    print(name.isdigit())
isdigit()

# isspace

def isspace():
    name=input("enter name:")
    print(name.isspace())
isspace()

# endswith()

def end():
    name=input("enter name:")
    print(name.endswith())
end()

# startswith()

def start():
    name=input("enter name:")
    print(name.startswith())
start()

# count()

def count():
    name=input("enter name:")
    print(name.count('f'))
count()

# find()

def find():
    name=input("enter name:")
    print(name.find('love'))
find()

# strip()

def strip():
    name=input("enter name:")
    print(name.strip())
strip()

# lstrip()

def lstrip():
    name=input("enter name:")
    print(name.lstrip())
lstrip()

# rstrip()

def rstrip():
    name=input("enter name:")
    print(name.rstrip())
rstrip()

# split()

def split():
    name=input("enter name:")
    print(name.split())
split()

# ljust()

def ljust():
    name=input("enter name:")
    print(name.ljust( 2,"#" ))
ljust()

# rjust()

def rjust():
    name=input("enter name:")
    print(name.rjust(2,"#"))
rjust()

# strip()

def zfill():
    name=input("enter name:")
    print(name.zfill(2))
zfill()

# replace()

def replace():
    sen=input("enter sen:")
    print(sen.replace("is","was"))
replace()

# join()

def join():
    name=["ram","sham"]
    fullname=" ".join(name)
    print(fullname)
join()