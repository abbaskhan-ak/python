import numpy as np
# print(np.__version__)

# arry= np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]],[[19,20,21],[22,23,24],[25,26,27]]])
# print(arry)
# print(arry.shape)
# print(arry[2,2])  #2,2 ki location par jo number hoga wo print hoga
# print(arry[0:])



# q = np.array(["tariq","noman","ahmad","abbas"])
# print(q)
# print(q.dtype)
# b=np.array(["12","22","33"])
# print(b.dtype)
# c=np.array([1,2,3,4])
# print(c.dtype)

# c=np.array([1,2,3,4] , dtype="S")  #yaha array int ha magar hm nay khud dtype change kardia
# print(c.dtype)


# g=np.array([1.2,2.4,3.5,8.9], dtype="f")
# print(g.dtype)

# g=np.array([1.2,2.4,3.5,8.9], dtype="i")
# print(g.dtype)


# g=np.array([1.2,2.4,3.5,8.9], dtype="i")    #data type in hm nay khud ki to point khatam hojai ga
# print(g)


# k= c.astype(int)      #ismay c ko k k equal kia or uski d type astype k func say change krdia
# print(k)


# l=np.array([0,1.2,2.4,0,-12.5])  #isko aglay step may bool may cnvert kardia

# r=l.astype(bool)
# print(r)

# r=l.view()   #ismay r aik variable ha jis may l ka data hm view karrhay ha
# print(r)

# r=l.view()   #ismay location daikh saktay ha
# print(l[1])

# r=l.view()
# r[0]=34
# print(r)
# print(l)

# print(l)

# d=l.copy()        #copy ka matlab d may l wala saman copy hogioa or wo alag hogia
# e= l.view()       #ismay hm e k zariyay l ko view karrhay ha or ismay jo hm changes karaingay wo l may hngi

# e[1]=43
# d[1]=42

# print(d)
# print(e)
# print(l)

# print(d.base)   #base batata ha k d,e,c ya koi kisi par dependent ha knhi  
# print(e.base)
# print(l.base)




# f=np.array([[2,3],[3,5]])
#     #or       ([[2,3],
#             #  [3,5]])
# print(f.shape)     #ismay dimension ya order batai ga




# g= np.array([1,3,5,6], ndmin=3)   #ndmin ka matlab kitnay dimension karni ha us hisab [] ya bracket lagayngay
# print(g)
# print(g.shape)
# print(g.ndim)        
# print(g[:,:,3])


# q=np.array([1,2,3,4,5,6,7,8,9])
# w=q.reshape(3,3)    #reshape say colom or row barha saktay ha ap jaisay upar 1 row tha sirf phir hmnay w k andar 3 row or 3 colom bnadia
# print(w)            #3,3 karnay k liyay upar walay matrix may 9 number honay chahiyay tab hoga isi tarah 2,2 karnay k liyay 4 hona chahiyay
# print(q)
# print(q.shape)
# print(q.ndim)






# o=np.array([2,3,4,5])
# t=o.reshape(2,2)
# print(o)
# print(t)




# o=np.array([1,2,3,4,5,6,7,8])
# t=o.reshape(2,2,2)
# print(o)
# print(t)


# o=np.array([2,3,4,5,6,7,8,9])
# t=o.reshape(2,2,2)
# w=t.reshape(-1)    #-1 say dubara single dimension may hojai ga
# print(w)
# # print(o)
# # print(t)
# print(t.shape)
# print(o.shape)
# print(w.shape)
# print(t.ndim)
# print(w.ndim)
# print(o.ndim)




# a=np.array(range(1,101))
# b=a.reshape(5,5,4)
# print(b)
# print(a)

# a=np.array([1,2,3,4,5,6])
# a=np.array([[2,3],[3,5]])
# b=a.reshape(2,2)
# for x in a:
#     print(x)


# c=np.array([1,2,3,4,5,6,7,8])
# d=c.reshape(2,2,2)
# print(d)
# for y in d:
#     print(y)

# for x in np.nditer(d):    #nditer=Ndimension iteration issay har element alag alag line may ajai ga
#     print(x)



# q=np.array([range(100)])
# print(q)
# # for x in np.nditer(q):   #ndier say alg line may agaya
# #     print(x)


# for x in np.nditer(q[:,::4]):   #isjka matlab 2 k step say
#     print(x)




# y=np.array([[2,4,5,7],[8,9,6,4]])
# print(y)

# for id, x in np.ndenumerate(y):   #is say har element ki position pata chalti ha agar bara array ha or kisi element ki position find karni hoto yay use hoga
#     print(id,x)


# o=np.array([1,2,3,4,5,6,7,8,9])
# b=o.reshape(1,3,3)
# print(b)
# for id , x in np.ndenumerate(b):
#     print(id,x)






# g=np.array([1,2,3,4])   #single dimension
# h=np.array([5,6,7,8])

# i=np.concatenate((g,h))    #issay do array ko aik kardia
# print(i)



# g=np.array([[1,2],[3,4]])
# h=np.array([[5,6],[7,8]])

# i=np.concatenate((g,h))    
# print(i)





# g=np.array([[1,2],[3,4]])
# h=np.array([[5,6],[7,8]])

# i=np.concatenate((g,h), axis=1)       #issay axis aik hojai ga ya change hojai ga
# print(i)


# g=np.array([[1,2],[3,4]])
# h=np.array([[5,6],[7,8]])

# i=np.stack((g,h))    #issay stack yanay aik k upar aik     
# print(i)




# g=np.array([[1,2],[3,4]])
# h=np.array([[5,6],[7,8]])

# i=np.hstack((g,h))    #issay horizontal stack hoga   
# print(i)


# g=np.array([[1,2],[3,4]])
# h=np.array([[5,6],[7,8]])

# i=np.vstack((g,h))    #issay vertical stack hoga    
# print(i)






k=np.array([range(8)])
print(k)


