from sklearn import tree
#[height,weight,shoe_size]
x=[[177,67,44],[177,70,43],[160,60,38],[166,65,40],[190,90,47],[175,65,39],[177,70,40]]
y=['male','female','male','female','female','male','male']
clf=tree.DecisionTreeClassifier()
clf=clf.fit(x,y)
#here we take input from keyboard 
a=int(input("enter the height:"))
b=int(input("enter the weight:"))
c=int(input("enter the shoe size:"))
print(a,b,c)

list_a =[]
list_a.append(a)
list_a.append(b)
list_a.append(c)
print(list_a)

prediction=clf.predict(list_a)
print (prediction)
