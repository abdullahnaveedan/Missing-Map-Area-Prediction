import numpy as np
import skimage.io as skio
import math
#import matplotlib.pyplot as plt
def takethird(elem):
    return elem[2]

def generatePixel(var):
    if var==1:
        return [102, 153, 0]
    elif var==2:
        return [0, 204, 255]
    else:
        return [255,255,255]

def distance(x1,y1,x2,y2):
    value = abs(x1-x2) + abs(y1-y2)
    return value


def pridict(arrzero,r,c,k):
    data=[]
    row = col = 0
    erow = ecol = 0
    val=6
    if r<val:
        row=0
        erow=val
        if c < val:
            col=0
            ecol=c+val
        elif c>=val and c<(img_cols-val):
            col=c-val
            ecol=c+val
        elif c>=(img_cols-val):
            col=c-val
            ecol=img_cols      
    elif r>=val and r<(img_row-val):
        row=r-val
        erow=r+val
        if c < val:
            col=0
            ecol=c+val
        elif c>=val and c<(img_cols-val):
            col=c-val
            ecol=c+val
        elif c>=(img_cols-val):
            col=c-val
            ecol=img_cols
    elif r>=(img_row-val):
        row=r-val
        erow=img_row
        if c < val:
            col=0
            ecol=c+val
        elif c>=val and c<(img_cols-val):
            col=c-val
            ecol=c+val
        elif c>=(img_cols-val):
            col=c-val
            ecol=img_cols 
        
    
    
    for i in range(row,erow):
        for j in range(col,ecol):
            if arrzero[i,j]==1 or arrzero[i,j]==2:
                dist = distance(r,c,i,j)
                data.append([i,j,dist])
                
    data.sort(key = takethird)
    #print(data)
    
    templist=[]
    for i in range(0,k):
        templist=data[i]
    
    tland=0
    twater=0
    for i in range(0,k):
        if arrzero[templist[0],templist[1]]==1:
            tland+=1
        elif arrzero[templist[0],templist[1]]==2:
            twater+=1
    
    var = 0
    
    if tland>twater:
        var = 1
    elif tland < twater:
        var = 2 
    
    return var

#Enter the name of file
arr = skio.imread('Italy50.png')
skio.imshow(arr)
arr_size=len(arr)
#print(arr_size)
img_row , img_cols , img_chs = arr.shape


arrzero = np.zeros(shape = (img_row,img_cols), dtype = np.uint8)
#Enter the value of k

k=9
newrow = 0
newcol = 0

for rows in arr:
    newcol = 0
    for cols in rows:
        if cols[0]== cols[1] and cols[1]== cols[2]: #i==j==k
            #print("White")
            arrzero[newrow][newcol] = 0
        elif cols[1]>cols[0] and cols[1]>cols[2]: #i<j>k
            #print("Land")
            arrzero[newrow][newcol] = 1
        elif cols[2]>cols[0] and cols[2]>cols[1]: #j<k>i
            #print("Water")
            arrzero[newrow][newcol] = 2        
        newcol+=1
    newrow+=1

outmap = np.zeros(shape=(img_row,img_cols),dtype=np.int8)
#print(arrzero)

for r in range(0,img_row):
    print("processing: {:.2f}%".format((r*100)/img_row))
    for c in range(0,img_cols):
        if arrzero[r,c] == 1 or arrzero[r,c] == 2:
            outmap[r,c] = arrzero[r,c]
        else:
            #print(pridict(arrzero,r,c,k))
            outmap[r,c]=pridict(arrzero,r,c,k)

outimg = np.zeros(shape=(img_row,img_cols,img_chs),dtype=np.uint8)

for r in range(0,img_row):
    for c in range(0,img_cols):
        px = generatePixel(outmap[r,c])
        outimg[r,c]=px
 
    #print(outimg)
    
skio.imshow(outimg)

skio.imsave('output50ak9.png',arr=outimg)
print("Image saved")
