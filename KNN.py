import numpy as np
import pandas as pd

def moiley(classifier,sets,age,people_class,k,df,cls):
    diffrence=[]
    i=0
    for j in range(k,len(age),1):
        for i in range(0,len(sets),1):
            ele=sets[i]-classifier
            diffrence.append(abs(ele))
            if(len(diffrence)==k):
                m=max(diffrence)
                ind=diffrence.index(m)
                sets[ind]=age[j]
                cls[ind]=people_class[j]
                diffrence.clear()                
            else:
                pass
        print("Dataset aquired on Iteration {0} is:{1} and Clases are:{2}".format(j,sets,cls))
            
            
    print("***************************************************************************")
    print("The middle age group which based on classifier is:{0}".format(classifier))
    print("***************The K-nearest neighbour result is**************************")
    for i in range(len(sets)):
        print(sets[i],cls[i])
            
sets=[]
cls=[]
df=pd.read_csv("gender-samples.csv")
print("Data we got from folder..")
print(df)
print("**********************************************************")
age=np.array(df['Age'])
people_class=np.array(df['Class'])
k=int(len(df)**0.5)
classifier=40

for i in range(k):
    sets.append(age[i])
for j in range(k):
    cls.append(people_class[j])

moiley(classifier,sets,age,people_class,k,df,cls)







