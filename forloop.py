languages=['Java', 'Python','c++']
for item in languages:
    print(item)

#sequence of numbers
numbers=range(1,6)
sum=0
for i in numbers:
    sum+=i
    print('sum :',sum)

#multiplication table
n=int(input("Enter number"))
for i in range(1,11):
    print(n,'x',i,'=',n*i)