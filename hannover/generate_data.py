import os,re
import numpy as np
from scipy.interpolate import LinearNDInterpolator

def find_xy(p1, p2, z):

    x1, y1, z1 = p1
    x2, y2, z2 = p2
    if z2 < z1:
        return find_xy(p2, p1, z)

    x = np.interp(z, (z1, z2), (x1, x2))
    y = np.interp(z, (z1, z2), (y1, y2))

    return x, y

bases=[]
lista=[-1, -5,  -25,  -500, 32, 36, 41, 56, 531 ]
lista1=[-1, -5, -10, -25,  -500, 32, 36, 56, 531 ]
listb=[-1, -5, -10, 32, 36, 41 ]
#listb=[41 ]
reso=32

for x in lista:
    for y in lista1:
        for z in listb:
            bases.append([x,y,z])

for i in range(len(bases)):
    base=np.array(bases[i])
    print(base)

    for targetz in range(1,31,1):
        for i in range(1):
            a=np.zeros((reso,reso,reso))
            #targetz=14
            a[:,:,targetz:targetz+1]=1

            #f=np.array(60,60,60)

            #a[:1,:,:]=1

            x,y,z = a.nonzero()
            #print(a.nonzero())
            #raise

            ix = np.random.choice(len(x), 5, replace=False)


            xi=x[ix]
            yi=y[ix]
            zi=z[ix]

            #print(xi,yi,zi)


            #print(  np.dstack([xi,yi,zi]) )
            poins= np.dstack([xi,yi,zi])
            #print(poins)
            #print(poins[0,:,:])


            #print(poins-base)
            b=np.zeros((reso,reso,reso))
            #print(poins.shape)
            for ii in range( poins.shape[1]):
                minx=np.round(np.min(xi)) 
                miny=np.round(np.min(yi)) 
                minz=np.round(np.min(zi))
                maxx=np.round(np.max(xi)) 
                maxy=np.round(np.max(yi)) 
                maxz=np.round(np.max(zi))
                if minx==maxx: maxx+=1
                if miny==maxy: maxy+=1
                if minz==maxz: maxz+=1
                #print(minx,maxx,miny,maxy,targetz,targetz+1)
                b[minx:maxx,miny:maxy,targetz:targetz+1]=1
                b[poins[0][ii][0],poins[0][ii][1],poins[0][ii][2]]=2
                a[poins[0][ii][0],poins[0][ii][1],poins[0][ii][2]]=2

                    
                #print(ii)
                stepsize=1
                if poins[0][ii][2]<base[2]+1: stepsize=-1
                for zp in range( base[2]+1 , poins[0][ii][2], stepsize):
                    if zp==32: zp=31
                    if zp<0 or zp>32: continue
                    #zp=base[2]+1
                    xp,yp= find_xy(poins[0][ii],base,zp)
                    if xp<0 or yp<0 or xp>32 or yp>32:continue
                    if xp==32: xp=31
                    if yp==32: yp=31
                    poin=np.round( np.array([xp,yp,zp]) ).astype('int')
                    #print(poin)
                    poin[poin==32]=31
                    b[poin[0],poin[1],poin[2]]=-2
                    a[poin[0],poin[1],poin[2]]=-2
                    #print(b.nonzero)

            loadable=1
            if loadable==1:
                with open('input.csv','a+') as opener:
                    
                    aa=a.reshape(reso**3)
                    np.savetxt(opener, aa, newline=" ",fmt="%d", delimiter=",")
                    opener.write("\n")
                    
                    #header = ','.join(map(str, a.shape))
                    #np.savetxt(opener, a.reshape(-1, a.shape[-1]), header=header,delimiter=',') 

                '''                     
                with open('input.csv','r') as opener1:
                    aaa=np.loadtxt(opener1)
                    aaa=aaa.reshape(aaa.shape[0],reso,reso,reso)
                    print(aaa)
                    raise
                '''
                
                with open('output.csv','a+') as opener2:
                    
                    bb=b.reshape(reso**3)
                    np.savetxt(opener2, bb, newline=" ",fmt="%d", delimiter=",")
                    opener2.write("\n")
                    
                    #header = ','.join(map(str, a.shape))
                    #np.savetxt(opener, a.reshape(-1, a.shape[-1]), header=header,delimiter=',') 

                '''                                    
                with open('output.csv','r') as opener3:
                    bbb=np.loadtxt(opener3)
                    bbb=bbb.reshape(bbb.shape[0],reso,reso,reso)
                    print(bbb)
                    #raise
                '''
                    
            #poin=np.round( np.expand_dims(poin,axis=0) )
            #print(poin)

            xinp,yinp,zinp = b.nonzero()
            #print(xinp)
            '''
            zp=3
            xp,yp=find_xy(poins[0][0],base,zp)
            poin0=np.array([xp,yp,zp])
            poin0=np.round( np.expand_dims(poin0,axis=0) )
            poin=np.append(poin,poin0,axis=0)
            print(poin)
            zp=4
            xp,yp=find_xy(poins[0][0],base,zp)
            poin0=np.array([xp,yp,zp])
            poin0=np.round( np.expand_dims(poin0,axis=0) )
            poin=np.append(poin,poin0,axis=0)
            print(poin)
            '''


            #print(np.interp(np.array([0,1,2,3,4]), np.array([ xi[0],base[0]) ,np.array([ yi[0],base[1])))
            #raise
            '''
            import matplotlib.pyplot as plt
            from mpl_toolkits.mplot3d import Axes3D
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.scatter(x, z, y, zdir='z', c= 'red')
            ax1 = fig.add_subplot(111, projection='3d')
            ax1.scatter(xinp, zinp, yinp, zdir='z', c= 'green')

            plt.savefig("demo.png")
            plt.show()
            '''
