# a="hello world"
# print(a.upper())
# print(a.lower())
# a="hello"
# b="world"
# print(a+b)
# print(a+" "+b)
# age=25
# study="ai"
# txt="my name is abbas,im{},studying{}"
# print(txt.format(study,study))
# 
# a="ak"
# b="2"
# print(a+b)
# a="ak"
# print("abbas"+a)
# print(a*" "*10)
# my_list=["oil","rice","aloo"]
# print(type(my_list))
# print(my_list)
# print(len(my_list))
# print(my_list[2])
# print(my_list[0:1])
# if"rice" in my_list:
#     print("yes")
#     my_list[1]="aata"
#     print(my_list)
#     x=[4.5,0,"sugar"]
#     print(my_list+x)
# a=[1,2,3,"mango",9]
# a.insert[2,"watermelon"]
# print(a)
# mylist=["mango","water"]
# mylist.append("orange")
# print(mylist)
# a=[1,2,3,"ball"]
# mylist.extend(a)
# print(mylist)
# mylist.remove("mango")
# print(mylist)
# mylist.pop(5)
# print(mylist)
# mylist=["ball","bat","ball"]
# mylist.remove("ball")
# print(mylist)
# del mylist
# print(mylist)
# print(my_list)
# aklist=[1,2,3,4,5,"ak"]
# aklist.clear()
# print(aklist)
# aklist=["wheat","rice","cotton","apple","1","2","3"]
# aklist.sort()
# print(aklist)
# print(aklist[0:3])
# a=["CHIcken","bat","apple","car"]
# a.sort()
# print(a)
# b=[1,9,3,7]
# b.sort()
# print(b)
# z=("six","eight","one","four")
# # new=[x for x in z if "o" in x]
# # print(new)
# new=for x in range(len(z))
# print(new)


                     #sets


# set1={"one","two","three","two"}
# set2={"orange","apple"}
# # set1.update(set2)
# # print(set1)
# # # print("one" in set1)
# list1=["ball","bat"]
# set1.update(list1)
# print(set1)
# set1.remove("three")
# print(set1)
# set1.discard("bat")
# print(set1)
# set2.clear()
# print(set2)
# set3={"lemon","orange"}
# x=set3.intersection(set1)
# print(x)
# x=set3.union(set1)
# print(x)
# x=set1.intersection(set3)
# print(x)



                     #dictionary



# dict1={"A":"ali","B":"bilal","C":"chandio"}
# print(type(dict1))
# print(dict1["A"])
# dict1={"A":"ali","B":"bilal","C":["list1","list2"]}
# print(dict1["C"])
# dict1={"A":"ali","B":"bilal","C":set1}
# print(dict1["C"])
# print(dict1["B"])
# x=dict1.keys()
# print(x)
# print(dict1["B"])
# if "B"in dict1:
#     print(dict1["B"])
# if "C" in dict1:
#     print(dict1["C"])
# a=input("enter your key")
# print(a)
# f=33.32
# print(type(f))
# dict1["D"]="dawood"
# print(dict1)
# dict1.pop("D")
# print(dict1)
# i = 0
# while i <6 :
#     i+=1
#     print(i)
# else:
#     print("i is no longer than 6")
# i = 0
# while i <6 :
#     i+=1
#     print(i)
#     if i==3:
#         break
# i = 0
# while i <6 :
#     i+=1
#     print(i)
#     if i==3:
#      print("f")
#      continue
# fruit=["apple","mango","apricot","cherry"]
# item=len(fruit)   #method=1
# i=0
# while i <item:
#     if fruit[i] == "apricot":
#         print(i)
#         fruit.remove("apricot")
#         print(fruit)
#         break
#     i+=1
# for items in fruit:       #method=2
#     if items=="apricot":
#         break
#     print(items)




# def myfunc():           #jab tak hm function ko call nhi karaingay wo run nhi hoga 3rd line may call kia
#     print("my name")
# myfunc()
    
# def myfunc(fname):
#     print("my name is " +fname)
# myfunc("abbas")

# def myfunc(value1,value2):
#     print("sum is " , value1+value2)
# myfunc(2,5)
# myfunc(4,9)
# myfunc(20,50)

# def myfunc(*value):    #  * ka matlab aik ziada ya kch bhi nhi argument may daisaktay ha
#     print("my name is "  + value[2])   #jo bhi index no daingay wohi naam aiga
# myfunc("abbas","khan","ak")

# def name(firstname,lastname):
#     print("my first name is   " + firstname)
#     print("my last name is   " + lastname)
#     print("my name is "  + firstname,lastname)
# name("abbas","khan")

# # def basket(fruits):
# #     for x in fruits:
# #         print (x)
# # item = ["apple","orange"]
# # basket(item)

# def basket(fruits):
#     for x in fruits:
#         if x=="orange":
#             break
#         print(x)
# item = ["apple","orange","cherry"]
# basket(item)



# def summation(val1,val2):
#     add=val1+val2
#     return add
# print(summation(2,3))


# def summation(val1,val2):
#     add=val1+val2
#     sub=val1-val2
#     return add,sub
# print(summation(2,3))


# def val():
#     a=int(input("enter first value :"))
#     b=int(input("enter second value :"))
#     if a > b:
#         print("a is greater than b" )
#     elif b > a:
#          print("b is greater than a" )

# val()


    
    

    
# def max_num(a,b,c):   
    
#     if a>b and a>c:
#         print("a is greater no")
#     elif b>a and b>c:
#         print("b is greater no")
#     else:
#         print("c is greatest no")

# no1=int(input("enter first no:"))
# no2=int(input("enter second no:"))
# no3=int(input("enter third no:"))
    

# max_num(no1,no2,no3)

   
# no=[1,8,3,6,5]
# def summation(no):
#     add=sum(no)
#     print("the sum is" ,add)
# summation(no)






# num=int(input("enter number"))
# def range():
#     if num>=0 and num<=10:
#         print("number is in range")
#     else:
#         print("number is not in range")    
# range()






# def rev():
#     name=input("enter any string")
#     print(name[-1::-1])
# rev()







#recursion in fuction
# def max_of_two(x,y):
#     if x>y:
#         return x
#     return y         #return y isliyay likha agar x ,y say bara na hua to wo y return kardaiga
# def max_of_three(x , y , z):
#     return max_of_two(x, max_of_two(y,z))
# print(max_of_three(3,6,-5))


                         #class


# class myclass:                      #simple method
#     x=5
#     y=9
#     z="abbas"
# p1=myclass()    #p1 object ha jo myclass say belong karta ha to jo my class may hoga wohi p1 ko assign hojai ga                   
# print(myclass.z)
# print(myclass.x)
# print(myclass.y)


# class myclass:           #initializing by constructer
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1=myclass( "abbas", 10)
# print(p1.name)
# print(p1.age)


# class myclass:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def myfun(self):
#         print("the {} is name " .format(self.name))
#                                  #or
#         print("the name is" +self.name)        
# p1=myclass("abbas",10)
# p1.myfun()


# class myclass:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def myfun(self):
        
#         print("the name is" +self.name)  
#         print("the age is " +self.age)      
# p1=myclass("abbas","10")
# p1.myfun()



# #del p1.name     delete object attribute name
# #del p1        delete whole object 

# #p1.name="ahmad"  replaces name





# class person:                  #concept of inheritance
#     def __init__(self,fname,lname):
#         self.first=fname
#         self.last=lname
#     def myfun(self):
#         print(self.first,self.last)   

# class firefighter(person):       #class firefighter is a subclass of class person , firefighter prop belong to prop of person
#     pass                         #pass ka matlab yaha kch nhi karna chahta agar khali choray gay to error aiga

# o1=firefighter("talha","tariq")
# o1.myfun()




# class person:                  
#     def __init__(self,fname,lname):
#         self.first=fname
#         self.last=lname
#     def myfun(self):
#         print(self.first,self.last)   

# class firefighter(person): 
#     pass                         
# class player(firefighter):   #player is sub class of firefighter it contain same prop as firefighter and person
#     pass

# o1=player("talha","tariq")    #o1=player,firefighter ya person kch bhi likh asktay hay q k teeno ki prop same
# o1.myfun()



# class person:                    #inheritance method 1          
#     def __init__(self,fname,lname):
#         self.first=fname
#         self.last=lname
#     def myfun(self):
#         print(self.first,self.last)   

# class firefighter(person):       #ismay subclass ka apna func bnai gay
#     def __init__(self,fname,lname):
#         self.fname1=lname
#         self.lname1=fname
#     def myfunc(self):
#         print(self.fname1,self.lname1)
# u1=person("talha","tariq")  #agar firefighter or my func kraingay to subclass ka constructer use hoga agar person or my fun karainagay to parent class ka constructer use hoga
# u1.myfun()                      





# class vehicle:         # inheritance method 2
#     def __init__(self,model,name,color):
#         self.name=name
#         self.model=model
#         self.color=color
#     def func(self):
#         print("vehicle name" ,self.name)
#         print("vehicle model" ,self.model)
#         print("vehicle color" ,self.color)

# class bike(vehicle):
#     def __init__(self,model,name,color):
#         super().__init__(model,name,color)
#     def mybike(self):
#         super().func()
    

# class cycle(vehicle):
#     def __init__(self,model,name,color):
#         super().__init__ (model,name,color)
#     def mycycle(self):
#         super().func()

# p1=vehicle(2020,"mercedes","black")
# p1.func()

# q1=bike(2020,"honda","red")
# q1.mybike()

# s1=cycle(2020,"cobra","silver")
# s1.mycycle()




                    #exceptional handling
  
  
  
  
  
   #key words= key, except ,finally
   #exceptional handling allows to excecute our own defined errors
    # it is use professionally


# try:
#     print(x)
# except:          #koi bhi type ka error handle karrhay ha
#     print("except printed")


# try:
#     print(x)
# except NameError:       #jab name error aiga tab yay except run hoga 
#     print("the variable x is not defined ")
# except :       #or nameerror k ilawa koi error ai to yay except run ho
#     print("something went wrong")

#     ###############
# try:
#     print(x*4)
# except:               #ismay x define nhi tha to error aya to something went wrong print hogaya
#     print("something went wrong")
# else:
#     print("nothing went wrong")

# x=3
# try:
#     print(x*4)
# except:              #ismay x define kardia to koi error nhi aya is liyay nothing went wrong print hua 
#     print("something went wrong")
# else:
#     print("nothing went wrong")
#  ######################



# try:
#     print(x*4)
# except:               #ismay x define nhi yanay error ha lakin tab bhi finally run hoga
#     print("something went wrong")
# finally:    #error ho ya na ho finally print hoga 
#     print("i dont know about any error")






# x=3
# try:
#     print(x*4)
# except:               #ismay x define ha yanay error nhi ha tab bhi finally run hoga
#     print("something went wrong")
# finally:    #error ho ya na ho finally print hoga 
#     print("i dont know about any error")



# x=int(input("write any number u want table of"))   #table
# i=1
# while(i<=10):
#     pro=x*i
#     print("{}*{}={}" .format(x,i,pro))
#     i+=1








# x=int(input("enter your roll #:"))#self error handling
# if x<0:                        #ismay agar roll no 0 say chota hoga to raise say self error generate hoga
#     raise Exception("enter your correct roll no")






# x=int(input("enter your roll no:"))

# if type(x) is int:
#     raise Exception("type in string format")





# x=open("myfile.txt")    #ismay koi text read karana ho to python walay folder may save kar k run kara saktay ha
# print(x.read())

                          #keys="r" read ,  "a" append, "w" write, "t" text, "b" binary




# x=open("myfile.txt")
# print(x.read(10))         #ismay shuru k 10 index print hngay




# x=open("myfile.txt")
# print(x.readline())         #readline say ,, agar file aik say ziada lines ha to yay sirf pehli line read karaiga khali read say sari lines read karaiga ,,ya agar print readline ksath ko do baar likhay gay to 2 line reakaraiga isi tarah 3 say 3


# x=open("myfile.txt")
# print(x.readline())          # ya agar print readline ksath ko do baar likhay gay to 2 line reakaraiga isi tarah 3 say 3
# #print(x.readline())
# x.close()                   #open k baad close karadia agar close k neechay print karaingay to nhi hoga



# x=open("myfile.txt","a")    # "a" say add hojai text may
# x.write("this is AI class")


# x=open("myfile.txt","r")     # "r" say bhi read hoga
# print(x.read())



# x=open("myfile1.txt","x")     # "x" issay new file crate hojai gi



# x=open("myfile2.txt","x")      #new folder bna kay kch text add kardia usmay
# x.write("this is myfile2")


# x=open("myfile2.txt","w")      #issay purana text khatam hokay naya text ajai ga
# x.write("this is myfil")



# class player:
#     def __init__(self,name,age,mode):
#         self.name = name
#         self.age = age
#         self.mode = mode
    
#     def func(self):
#         print("player is running")
#         print("player name is"+self.name)
#         print("player age is"+self.age)
#         print("player mode is"+self.mode)

# p1=player("abbas","19","legendary")
# p1.func()



# class calculator:
#     def __init__(self,value1,value2,operator):
#         self.value1=value1
#         self.value2=value2
#         self.op =operator
#     def operator(self):
#         if self.op == "+":
#             print (self.value1+self.value2)
#         elif self.op =="-":
#             print(self.value1-self.value2)
#         elif self.op == "/":
#             print(self.value1/self.value2)
#         elif self.op == "*":
#             print(self.value1*self.value2)
# q1=calculator(2,6,"-")
# q1.operator()
        
    




                #encapsulation
# class computer:
#     def __init__(self):
#         self.__maxprice=900  #__ ka matlab private attribute ha yay change nhi hosakta sirf aik special method say change hoga
#     def sell(self):
#         print("sell price: {}" .format(self.__maxprice))
#     def setmaxprice(self,price):
#         self.__maxprice=price
    
# c=computer()
# c.sell()
# #ab hmnay agar price change karni ha
# #change price
# c.__maxprice=1000
# c.sell()    #nhi hoga change

# # ussing setter function 
# c.setmaxprice(1000)   #ab hojai ga
# c.sell()

