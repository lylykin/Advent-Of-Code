def dist_list(l1,l2):
    """l1,l2 : same-sized lists
    returns the total distance between the elements of the two lists"""
    dist=0
    res=len(l1)
    for i in range (res):
        min1=l1.pop(l1.index(min(l1)))
        min2=l2.pop(l2.index(min(l2)))
        dist+=abs(min2-min1)
    return dist

def similarity(l1,l2): 
    sim=0
    for n in l1:
        t=l2.count(n)
        sim+= n*t
    return sim

with open('input.txt','r') as f:
    l1,l2=[],[]
    lines=f.read().splitlines()
    for line in lines:
        l2.append(int(line[5:]))
        l1.append(int(line[:-5]))

print(f'similarity : {similarity(l1,l2)}')
print(f'distance : {dist_list(l1,l2)}')
