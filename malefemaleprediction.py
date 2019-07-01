from sklearn import tree
#[height,weight,shoe_size]
x=[[177,67,44],[177,70,43],[160,60,38],[166,65,40],[190,90,47],[175,65,39],[177,70,40]]
y=['male','female','male','female','female','male','male']
clf=tree.DecisionTreeClassifier()
clf=clf.fit(x,y)
prediction=clf.predict([[16,50,111]])
print (prediction)