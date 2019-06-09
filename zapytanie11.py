#!/usr/bin/python
# -*- coding: UTF-8 -*-
import riak

client = riak.RiakClient(port=8087)
myBucket = client.bucket("s18392")

def New(key, value):
    myBucket.new(key, data=value).store()      

def Get(key):
    print(myBucket.get(key).data)

def Update(key, newValue):
    val = myBucket.get(key)
    val.data = newValue
    val.store()

def Delete(key):
    myBucket.get(key).delete()

typ = "Opera"
nazwa = "Carmen"
rok = 1878
sztuka = {"typ": typ, "nazwa": nazwa, "rokPremiery": rok}

New("Sztuka1", sztuka)
print("Utworzono sztukę: ")
Get("Sztuka1")

rok = 2000
sztuka = {"typ": typ, "nazwa": nazwa, "rokPremiery": rok}
Update("Sztuka1", sztuka)
print("Zmodyfikowano sztukę: ")
Get("Sztuka1")

Delete("Sztuka1")
print("Usunięto sztukę")
Get("Sztuka1")

