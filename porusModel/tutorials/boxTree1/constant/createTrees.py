from numpy import genfromtxt,linspace
from random import randint
import pyvista as pv 

x=linspace(-256,256,17)
y=linspace(-256,256,17)

data=open("treeTable","w")
counter=0
for i in range(0,len(x)):
    for j in range(0,len(y)):
        z=0
        xtree=x[i]
        ytree=y[j]
        Ht=randint(5,25)
        Girth=randint(2,10)
        LAI=randint(1,10)
        Cd=randint(2,4)*0.1
        Zm=randint(1,7)*0.1
        if(counter==0):
            localbox=pv.Cube(bounds=(xtree-0.5*Girth,xtree+0.5*Girth, \
                                     ytree-0.5*Girth,ytree+0.5*Girth, \
                                     0,0.4*Ht))
            localBig=pv.Cube(bounds=(xtree-2.5*Girth,xtree+2.5*Girth, \
                                     ytree-2.5*Girth,ytree+2.5*Girth, \
                                     0.4*Ht,Ht))                                            
            globalbox=localbox
            globalbox=globalbox.merge([localBig])
        else:
            localbox=pv.Cube(bounds=(xtree-0.5*Girth,xtree+0.5*Girth, \
                                     ytree-0.5*Girth,ytree+0.5*Girth, \
                                     0,0.4*Ht))
            localBig=pv.Cube(bounds=(xtree-2.5*Girth,xtree+2.5*Girth, \
                                     ytree-2.5*Girth,ytree+2.5*Girth, \
                                     0.4*Ht,Ht))
            tempbox=globalbox.merge([localbox,localBig])
            globalbox=tempbox
        data.write("(%g %g %g %g %g %g %g %g)\n"%(x[i],y[j],z,Ht,Girth,LAI,Cd,Zm))
        counter=counter+1
data.close()
pv.save_meshio("triSurface/trees.obj",globalbox)
