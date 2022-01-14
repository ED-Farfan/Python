def Euclides(r0,r1):
    q=[]
    r=[r0,r1]    
    while(r[-2]%r[-1] != 0 ):
        q.append((r[-2]-r[-2]%r[-1])//r[-1])
        r.append(r[-2]%r[-1])
    q.append((r[-2]-r[-2]%r[-1])//r[-1])
    return q,r
def Invertir(q,r):
    t=[0,1]
    for i in range(1,len(r)-1):
        t.append((t[i-1]-t[i]*q[i-1])%r[0])
    print("->"+str(r[0]))
    return t
def resutados(q,r,t):
    print("\n")
    gio=""
    for i in range(20):
        gio+="-*-*"
    print(gio)
    print("\n\tAlgoritmo de Euclides\n")
    for i in range(1,len(r)-1):
        print("r["+str(i-1)+"]: "+str(r[i-1])+" = q["+str(i)+"] :"+str(q[i-1])+" x r["+str(i)+"]: "+str(r[i])+" + r["+str(i+1)+"]: "+str(r[i+1]))
    print("r["+str(len(r)-2)+"]: "+str(r[-1])+" = q["+str(len(q))+"] :"+str(q[-1])+" x r["+str(len(r)-1)+"]: "+str(r[-1])+" + 0")
    print("\nMCD("+str(r[0])+","+str(r[1]) +") = "+str(r[-1]))
    if(q != [] and r[-1]==1):
        print("\nTiene inverso")
        print("Inverso igual a "+str(t[-1]))
        print(t)
    else:
        print("\nNo tiene inverso")
    
    print(gio)
#q,r=Euclides(11001,117387)
#t=Invertir(q,r)
#resutados(q,r,t)
#q,r=Euclides(13422,117387)
#t=Invertir(q,r)
#resutados(q,r,t)
#q,r=Euclides(15872,117387)
#t=Invertir(q,r)
#resutados(q,r,t)

#q,r=Euclides(53,20)
#t=Invertir(q,r)
#resutados(q,r,t)

q,r=Euclides(94349,17761)
t=Invertir(q,r)
resutados(q,r,t)
