import plaskie
import bryly 
print("---- WYBIERZ FIGURĘ ----")
print('''
      a - Prostokąt
      b - Kwadrat
      c - Rownoleglobok
      d - Trojkat
      e - Trapez
      1 - Kula
      2 - Szescian
      3 - Prostopadloscian
      4 - Graniastosłup
      5 - Ostrosłup
      6 - Walec
      7 - Stozek
      Stop - Koniec
      ''')

while True:
    inp:str = input().lower()
    if inp == "Stop":
        break
    elif inp == "a":
        a:float = float(input("a: "))
        b:float = float(input("b: "))
        wynik = plaskie.pp_prostokat(a,b)
        print(f"ppProstokata = {wynik}")
    elif inp == "b":
        a:float = float(input("a: "))
        wynik = plaskie.pp_kwadratu(a)
        print(f"ppkwadratu = {wynik}")
    elif inp == "c":
        a:float = float(input("a: "))
        h:float = float(input("h: "))
        wynik = plaskie.pp_rownolegloboku(a,h)
        print(f"ppRownolegloboku = {wynik}")
    elif inp == "d":
        a:float = float(input("a: "))
        h:float = float(input("h: "))
        wynik = plaskie.pp_trojkata(a,h)
        print(f"ppTrojkata = {wynik}")
    elif inp == "e":
        a:float = float(input("a: "))
        b:float = float(input("b: "))
        h:float = float(input("h: "))
        wynik = plaskie.pp_trapzeu(a,b,h)
        print(f"ppTrapezu = {wynik}")
    elif inp == "1":
        r:float = float(input("r: "))
        wynik = bryly.pp_kuli(r)
        print(f"ppKuli = {wynik}")
    elif inp == "2":
        a:float = float(input("a: "))
        wynik = bryly.pp_szescianu(a)
        print(f"ppSzescianu = {wynik}")
    elif inp == "3":
        a:float = float(input("a: "))
        b:float = float(input("b: "))
        c:float = float(input("c: "))
        wynik = bryly.pp_prostopadloscianu(a,b,c)
        print(f"ppProstopaadloscianu = {wynik}")
    elif inp == "4":
        pp:float = float(input("pp: "))
        pb:float = float(input("pb: "))
        wynik = bryly.pp_graniastoslupa(pp,pb)
        print(f"ppGraniastoslupa = {wynik}")
    elif inp == "5":
        pp:float = float(input("pp: "))
        pb:float = float(input("pb: "))
        wynik = bryly.pp_ostroslupa(pp,pb)
        print(f"ppOstroslupa = {wynik}")
    elif inp == "6":
        r:float = float(input("r: "))
        h:float = float(input("h: "))
        wynik = bryly.pp_walca(r,h)
        print(f"ppWalca = {wynik}")
    elif inp == "7":
        r:float = float(input("r: "))
        l:float = float(input("l: "))
        wynik = bryly.pp_stozka(r,l)
        print(f"ppStozka = {wynik}")
    else:
        print("nie ma takiej opcji")