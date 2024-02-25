
<details>
<summary>
behind the scene loops/iterations in python
</summary>


```
f = open('chai.py')

f.readline()

f.__next__()

f = open('chai.py')
for line in open('chai.py'):
    print(line)

f = open('chai.py')
for line in open('chai.py'):
    print(line, end='')

f = open('chai.py')
while True:
    line = f.readline()
    if not line: break
    print(line, end='')


test = "sidhant"
if not test:            
    print("chai")

test = ""
if not test:            
    print("chai")


myList = [1,2,3,4,5,6,7,8,9]
I = iter(myList)
I.__next__()
I.__next__()       //  value of I changes but memory allocation remains same 


f = open('chai.py')
iter(f) is f
iter(f) is f.__iter__()


myNewList = [1, 2, 3]
iter(myNewList) is myNewList       // False


D = {'a': '1', 'b': '2'}
for key in D.keys():
    print(key)

I = iter(D)
I.__next__() or next(I)
next(I)

R = range(13)
I = iter(R)
next(I)
I.__next__()


```

</details>
