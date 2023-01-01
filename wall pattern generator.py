import time
w=5 #width of board
h=4 #height of board
empty=' '*w*h
spots=[]
for i in range(w*h):
    spots.append(i)
cant=[1,w-2,w,2*w-1,w*(h-2),w*(h-1)-1,w*(h-1)+1,w*h-2]
for c in cant:
    if c in spots:
        spots.remove(c)

def getblockingspawns(i):
    if 0<i%w<w-1 and 0<i//w<h-1:
        bs=[i-w-1,i-w,i-w+1,i-1,i+1,i+w-1,i+w,i+w+1]
    elif i%w==0:
        if i//w==0:
            bs=[i+2,i+w+1,i+w+w]
        elif i//w==h-1:
            bs=[i-w-w,i-w+1,i+2]
        else:
            bs=[i-w,i-w-w,i+w,i+w+w,i-w+1,i+1,i+w+1]
        if i//w==2:
            bs.append(i-w-w+2)
        if i//w==h-3:
            bs.append(i+w+w+2)
    elif i%w==w-1:
        if i//w==0:
            bs=[i-2,i+w-1,i+w+w]
        elif i//w==h-1:
            bs=[i-w-w,i-w-1,i-2]
        else:
            bs=[i-w,i-w-w,i+w,i+w+w,i-w-1,i-1,i+w-1]
        if i//w==2:
            bs.append(i-w-w-2)
        if i//w==h-3:
            bs.append(i+w+w-2)
    elif i//w==0:
        bs=[i-1,i-2,i+1,i+2,i+w-1,i+w,i+w+1]
        if i%w==2:
            bs.append(i+w+w-2)
        if i%w==w-3:
            bs.append(i+w+w+2)
    elif i//w==h-1 and i%w!=1 and i%w!=w-2:
        bs=[i-1,i-2,i+1,i+2,i-w-1,i-w,i-w+1]
        if i%w==2:
            bs.append(i-w-w-2)
        if i%w==w-3:
            bs.append(i-w-w+2)
    for c in cant:
        if c in bs:
            bs.remove(c)
    bs.append(i)
    bs.sort()
    bs.reverse()
    return bs

a=[]
for spot in range(w*h):
    if spot in cant:
        a.append([])
    else:
        a.append(getblockingspawns(spot))

all_valid_spawns=[]
extremes=[w*h,0]

def get_all_valid_spawns(board,lastplaced,walls):
    ns=True
    for i in spots:
        check=''
        for num in a[i]:
            check+=board[num]
        if '█' not in check:
            if i>=lastplaced:
                get_all_valid_spawns(board[:i]+'█'+board[i+1:],i,walls+1)
            else:
                if a[i][0]<=lastplaced:
                    return
            ns=False
    if ns==True:
        all_valid_spawns.append(board)
        #s='----------'
        #for i in range(h):
        #    s+='\n'+board[i*w:(i+1)*w]
        #print(s)
        #uncomment above code if you want it to print every pattern it discovers
        if walls>extremes[1]:
            extremes[1]=walls
        if walls<extremes[0]:
            extremes[0]=walls

abc=time.time()
get_all_valid_spawns(empty,0,0)
print(len(all_valid_spawns))
print(time.time()-abc)
print(extremes)

def writetofile():
    with open(str(h)+'by'+str(w)+'.txt', 'w') as f:
        total=''
        for pattern in all_valid_spawns:
            s='-'*w
            for i in range(h):
                s+='\n'+pattern[i*w:(i+1)*w]
            total+=s+'\n'
        total+='\n'+str(len(all_valid_spawns))+'\n'+str(extremes)
        print(total,file=f)

writetofile()
