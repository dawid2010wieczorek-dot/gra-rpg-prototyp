postac = [300,10]
goblin = [70,10]
straznik = [270,90]

while postac[0] >= 0:
    print("walka - a")
    inp = input()
    if inp == "a":
        while goblin[0] >= 0:
            while postac[0] >= 0:
                print(postac)
                print(goblin)
                postac[0] -= goblin[1]
                goblin[0] -= postac[1]
            if goblin[0] <= 0:
                print("zwycięstwo")
                print("level up")
                postac = [300,60]
                print (postac)
                print("dotarłeś do sklepu")
                print("atak czy obrona")
                print("atak to + 30 do ataku")
                print("obrona to + 50 do obrony")
                wybór = input()
                if wybór == "atak":
                    postac = [300,90]
                if wybór == "obrona":
                    postac = [350,60]
                else:
                    print("wybierz coś istotnego")
                print(postac)
                while straznik[0] >= 0:
                    while postac[0] >= 0:
                        print(postac)
                        print(straznik)
                        postac[0] -= straznik[1]
                        straznik[0] -= postac[1]
                    if straznik[0] <= 0:
                        print("zwycięstwo")
                        print("ciąg dalszy nastąpi")
                    else:
                        print("game over")
            else:
                print("game over")            
                

    