
# simple list creation

# example 1
list1 = [10,20,30,40]

print(list1)

print(list1[0])

print(list1[-2])  # negative index


# example 2
list2 = [[ 'nitesh', 'kumar'],[10,20,30,40]]

print(list2)

print(list2[0])

print(list2[0][1])


# example 3

data = 'The ' + list2[0][-1] + ' is a genius ' + str(list2[1][-2])
print(data)

# example 4 slicing ([:])

list3 = ['cat', 'dog', 'elephant']

print(list3[1:2])

# Note - index -> single value & slice -> list of values


#  example 5 - changing list items


spam = 'Hello'
spam = [10, 20, 30]
spam[1] = 'Hello'
print(spam)

spam[1:3] = ['CAT', 'DOG', 'MOUSE']
print(spam)

#  example 6 - slice shortcuts

spam1 = ['CAT', 'DOG', 'MOUSE', 'ELE']


print(spam1[:2])


print(spam1[1:])

# example 7 - del
spam1 = ['CAT', 'DOG', 'MOUSE', 'ELE']
del spam1[2]
print(spam1)


#print(len[1,2,3])

print([1,2,3] + [4,5,6])

'hello' * 3

[1,2,3] * 3

list('Hello')


# in or not in operators

print('howdy' in ['hello','hi','howdy'])

print('howdy' not in ['hello','hi','howdy'])


# for loop

for i in range(4):
    print(i)

range(4)

range(0,4)

list(range(0,100,2))

#for i in range(len(somelist))

supplies = ['pens','staplers','flame-throwers','binders']

for i in range(len(supplies)):
    print('Index' + str(i) +'in supplies is:'+supplies[i])


# multilpe asssignemnt trick
cat = ['fat', 'orange','loud']

size,color,desp = cat
print(size)
print(color)
print(desp)

a = 'AAA'
b = 'BBB'
a,b = b,a
print(a)
print(b)

# augmented assignment operators

spam = 42
spam = spam + 1
spam +=1

