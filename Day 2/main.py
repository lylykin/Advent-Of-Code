def is_safe(rep):
    '''rep : list
    ---
    checks if a report is safe or not
    ---
    returns bool'''
    
    rep_cop,rep_copr = rep.copy(), rep.copy()
    rep_cop.sort()
    rep_copr.sort(reverse = True)
    
    if rep != rep_cop and rep != rep_copr:  #n'est pas croissante ni décroissante
        return False
    else : #il faut check si la var est bien entre 1 et 3
        for i in range(1,len(rep)):
            dist = abs(rep[i]-rep[i-1])
            if dist>3 or dist == 0 :
                return False
    return True 
        

        

with open('./Day 2/input.txt','r') as f:
    lines = f.readlines()
    safecount = 0
    
    for line in lines:
        numbers = line.split()
        report = [int(n) for n in numbers]
        
        if is_safe(report):
            safecount += 1 

    print(safecount)
