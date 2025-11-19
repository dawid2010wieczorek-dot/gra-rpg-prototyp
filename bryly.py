import math
pi = math.pi
def pp_kuli(pi:float,r:float)->float:
    return 4*pi*r**2
def pp_stozka(pi:float,r:float,l:float)->float:
    return pi*r**2+2*pi*r*l
def pp_walca(pi:float,r:float,h:float)->float:
    return 2*pi*r**2+2*pi*r*h
def pp_ostroslupa(pp:float,pb:float)->float:
    return pp+pb
def pp_graniastoslupa(pp:float,pb:float)->float:
    return 2*pp+pb
def pp_prostopadloscianu(a:float,b:float,c:float)->float:
    return 2*a*b+2*a*c+2*b*c
def pp_szescianu(a:float)->float:
    return 6*a**2