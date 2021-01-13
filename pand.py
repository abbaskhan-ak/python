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



students = {"students_name":["abbas","adil","ali","erdum","ahmad","tariq","noman","hamza","usman","ebad"],
"physics":[71,88,69,75,25,65,98,78,45,12],
"chemistry":[50,58,68,72,25,36,96,85,74,45],
"maths":[74,48,61,71,12,45,78,98,65,32],
"english":[80,38,64,74,85,25,12,32,65,48]}
clg = pd.DataFrame(students)
print(clg)
print(clg.head(3))     #shuru ki values acces hngi head say
print(clg.tail(3))      #akhri ki values acces hngi tail say print
print(clg.info())       #yay information k liyay hota ha










# df = pd.read_csv("akex.csv")    #hm nay excel file ismay show karai
# print(df)
# df = pd.read_csv("akex.csv")
# print(df.head(3))     #shuru ki values acces hngi head say
# print(df.tail(3))     #akhri ki values acces hngi tail say print

# print(df.info())      #yay information k liyay hota ha






