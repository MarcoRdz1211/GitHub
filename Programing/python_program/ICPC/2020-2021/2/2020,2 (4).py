S=input()
L,R=0,0 #Declaro puntos Left y Right
l,r = 0,0 #Juegos ganados
wl,wr = "",""

for i in range(0,len(S)):
    if S[i]=="S":
        L += 1
        if ((L==5 and abs(L-R)>=2) or L==10):
            L,R,l = 0,0,l+1
            wl,wr = "winner",""

    elif S[i]=="R":
        R += 1
        R,L,r,l = L,R,l,r
        if ((R==5 and abs(R-L)>=2) or R==10):
            R,L,r = 0,0,r+1
            wr,wl = "winner",""

    else:
        if (L==0 and R==0):
            if wl == "winner":
                print(r,"-",1,"(winner)")
            else:
                print(r,"(winner)","-",l)
        else:
            print(r,"(",R,")","-",l,"(",L,"*)")
