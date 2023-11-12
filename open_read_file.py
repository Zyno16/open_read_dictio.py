fname=input("enter the text")
if len(fname)<1: fname="clown.txt"
hand = open(fname)
dir=dict()
for lin in hand:
    lin =lin.strip()
    print(lin)
    wds =lin.split()
    #print(wds)
    for w in wds:
        if w in dir:
            dir[w]=dir[w]+1
            print(" ****existing****")
        else:
            dir[w]=1
            print("****NEW*****")
        print(w,dir[w])


    


