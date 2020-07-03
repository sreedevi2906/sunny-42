Open In Colab
1.what is dictionary in python?explain with an example.

Dictionary is used for storing unorder data collection. This is also a type of data structure. {Key:value,key1:value1,key2:vakue2} Keys are unique but values are duplicated.keys are immutable but values are mutale

In [1]:
d={"h":1,"e":2,"y":3}
print(d)
{'h': 1, 'e': 2, 'y': 3}
2. Write a Python program to sum all the items in a list.

In [2]:
a=[1,2,3]
b=[4,5,6]
print(a+b)
[1, 2, 3, 4, 5, 6]
In [3]:
a=[1]
b=[2]
C=a+b
print(C)
[1, 2]
3.Write a Python program to create a list of empty dictionaries.

In [3]:
a=2
l=[{} for i in range(a)]
print(l)
[{}, {}]
4.Write a Python program to access dictionary keys element by index.

In [6]:
d={"chemistry":99,"physics":88}
print(list(d)[1])
physics
In [7]:
d={"chemistry":99,"physics":88}
print(list(d)[0])
chemistry
5. Write a Python program to iterate over dictionaries using for loops

In [11]:
d={"black":1,"blue":2,"peach":3}
for colour_key,value in d.items():
  print(colour_key,"corresponds to", d[colour_key])
black corresponds to 1
blue corresponds to 2
peach corresponds to 3
6.Write a Python program to sum all the items in a dictionary.

In [29]:
def returnSum(myDict):
  sum = 0
  for i in myDict: 
    sum = sum + myDict[i]
  return sum
dict = {'a': 100, 'b':200, 'c':300} 
print("Sum :", returnSum(dict))
Sum : 600
7.Write a Python script to concatenate following dictionaries to create a new one. Sample Dictionary:

In [35]:
dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic4={}
for d in (dic1,dic2,dic3):dic4.update(d)
print(dic4)
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}