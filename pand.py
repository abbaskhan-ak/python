import pandas as pd

# dataset1 = {"car":["bmw","toyota","ford","benz"],"win":[2,1,3,4]}
# report1 = pd.DataFrame(dataset1)
# print(report1)





# sub = {"subjects":["maths","physics","chem"],"marks":[90,89,92]}
# report = pd.DataFrame(sub)
# print(report)





# a = [1,4,66,7,99]
# report2=pd.Series(a)
# print(report2)






# a = [1,4,66,7,99]
# report2=pd.Series(a, index=["math","physics","chem","bio","islamiat"])   #ismay index may number ki jagah hm nay jo sbjects diay hay wo aiga
# print(report2)





# calories = {"day1":40,"day2":100,"day3":200}
# report1 = pd.Series(calories)
# print(report1)


# dataset1={"days":["day1","day2","day3"],"caloryburn":[100,200,300]}
# rep=pd.DataFrame(dataset1)
# print(rep)




# dataset1={"days":["day1","day2","day3"],"caloryburn":[100,200,300]}
# rep=pd.DataFrame(dataset1)
# print(rep.loc[2])    #issay individual ka index pata lagay ga





# calories = [10,20,50]
# report1 = pd.Series(calories, index=["car","bike","cycle"])
# print(report1)
# print(report1.loc["car"])    #ismay ab hm nay index ka naam dal kar individual ka pata chalay ga





# dataset1={"days":["day1","day2","day3"],"caloryburn":[100,200,300]}
# rep=pd.DataFrame(dataset1,index=["a","b","c"])
# print(rep.loc["a"])    



# students = {"students_name":["abbas","adil","ali","erdum","ahmad","tariq","noman","hamza","usman","ebad"],
# "physics":[71,88,69,75,25,65,98,78,45,12],
# "chemistry":[50,58,68,72,25,36,96,85,74,45],
# "maths":[74,48,61,71,12,45,78,98,65,32],
# "english":[80,38,64,74,85,25,12,32,65,48]}
# clg = pd.DataFrame(students)
# print(clg)
# print(clg.head(3))     #shuru ki values acces hngi head say
# print(clg.tail(3))      #akhri ki values acces hngi tail say print
# print(clg.info())       #yay information k liyay hota ha










# df = pd.read_csv("akex.csv")    #hm nay excel file ismay show karai
# print(df)
# df = pd.read_csv("akex.csv")
# print(df.head(3))     #shuru ki values acces hngi head say
# print(df.tail(3))     #akhri ki values acces hngi tail say print

# print(df.info())      #yay information k liyay hota ha




# a = pd.read_csv("iris.csv")
# print(a)
# print(a.info())
# print(a.to_string())
# b=a.dropna()   #dropna say null values khatam hojai gi or data clean hojai ga but data reduce hojai ga
# print(b.info())
# print(b.to_string())



# a = pd.read_csv("iris.csv")
# print(a)
# a.dropna(inplace=True)       #ismay variable assign kiyay baghair hi a may hi dropna karadia inplace isliyay use hota hay takay main data may changes hojai
# print(a.info())
# a.fillna(120 , inplace=True)   #issay null value fill hojai gi jo value hm daingay i.e 120
# print(a.to_string())
# print(a["petal_width"])     #issay jo colom print karana ha us ka naam likhana ha
# print(a["sepal_length"].loc[5])    #ismay sepal lenght k jo index print karan ho
# # print(a["sepal_length"].loc[0:5]) 
# print(a.head(6))

# b=a.drop([149],axis=0)     #issay row khatam hojai ga
# print(b)


# c=a.drop(["petal_width"],axis=1)     #issay colom khatam hojai ga,ismay axis batana zaroori ha
# print(c)


# c=a.drop(["petal_width","sepal_length"],axis=1)     
# print(c)



# a=pd.read_csv("ak.csv")
# print(a)
# print(a.info())
# x=a.drop(columns=["Period","Group","Series_reference"])    #ismay drop karnay k liyay axis batana zaroori nhi
# print(x.info())




# a=pd.read_csv("iris.csv")
# print(a.info())
# print(a.to_string())
# # m=a["petal_width"].loc[[87,91]].mean()       #issay kisi bhi colom ki values ka mean niklay ga
# # print(m)

# a=pd.read_csv("iris.csv")
# x=a["petal_width"].mean()
# a["petal_width"].fillna(x,inplace=True)    #ismay petalwidth may jo null value hogi usmay mean value fill hojai gi
# print(x)
# print(a)





# a=pd.read_csv("iris.csv")
# x=a["petal_width"].mode()
# a["petal_width"].fillna(x,inplace=True)    #ismay petalwidth may jo null value hogi usmay mode value fill hojai gi
# print(x)
# print(a)




# a=pd.read_csv("iris.csv")
# x=a["petal_width"].mode()
# a["petal_width"].fillna(x,inplace=True)    
# a["sepal_length"] = pd.to_datetime(a["sepal_length"])    #ismay wo colom datetime format may hojai ga
# print(x)
# print(a)




# a=pd.read_csv("iris.csv")
# print(a["sepal_length"])
# a.loc[0 , "sepal_length"]=4.2      #issay kisi colom ki specific value change hosakti ha
# print(a["sepal_length"])




a=pd.read_csv("iris.csv")
for x in a.index:
    if a.loc[x,"sepal_length"] >=4.5:     #ismay jo value 4.5 ya ussay bari hngi wo 5 may convert hojai gi
        a.loc[x,"sepal_length"] =5.0
print(a)