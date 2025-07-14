def alp_mult(s):
    alpL=[chr(l) for l in range(97,123)]
    alpU=[chr(l) for l in range(65,97)]
    l=list(s)
    new_s=""
    for s in l:
        if s in alpL:
            new_s=new_s+(s*(alpL.index(s)+1))
        if s in alpU:
            new_s=new_s+(s*(alpU.index(s)+1))   
    return new_s

print(alp_mult("Chinthan"))