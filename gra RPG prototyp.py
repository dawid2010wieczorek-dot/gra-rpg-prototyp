postac = [1000,10]
goblin = [70,10]
straznik = [270,90]
czarodziej = [200,9999,99999]
smok = [1000,100]
krol = [10,10,99999]


while postac[0] >= 0:
    print("walka - a")
    inp = input()
    if inp == "a":
        while postac[0] > 0:
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
                print("atak to + 30 do ataku i lekki boost do hp")
                print("obrona to + 50 do obrony")
                wybór = input()
                if wybór == "atak":
                    postac = [1000,90]
                elif wybór == "obrona":
                    postac = [350,60]
                else:
                    print("wybierz coś istotnego")
                print(postac)
                while postac[0] > 0:
                    print(postac)
                    print(straznik)
                    straznik[0] -= postac[1]
                    postac[0] -= straznik[1]
                    if straznik[0] <= 0:
                        print("zwycięstwo")
                        break
                if straznik[0] <= 0:
                    print("napotykasz się na tajmeniczego czarodzieja")
                    print("co robisz ?")
                    print("rozmawiam,proszę o pomoc,atakuję")
                    rozmowa = input()
                    if rozmowa == "rozmawiam":
                        postac[0] += czarodziej[0]
                        print(postac)
                    elif rozmowa =="proszę o pomoc":
                        postac[1] += czarodziej[1]
                        print(postac)
                    elif rozmowa =="atakuje":
                        postac[0] -= czarodziej[2]
                        if postac[0] <= 0:
                            print("game over")
                            break  
                    print("teraz widzisz przed sobą ogramnego smoka")
                    print("co robisz")
                    print("uciekam,atakuje,rozmawiam")
                    smoczek = input()
                    if smoczek == "uciekam":
                        print("nie ma ucieczki")
                        postac[1] -= krol[2]
                    elif smoczek == "rozmawiam":
                        print("w tym świecie amoki nie rozmawiają")
                        postac[1] -= krol[2]
                    elif smoczek == "atakuje":
                        while postac[0] > 0:
                            print(postac)
                            print(smok)
                            smok[0] -= postac[1]
                            postac[0] -= smok[1]
                            if smok[0] <= 0:
                                print("zwycięstwo")
                                break
                        if smok[0] <= 0:
                            print("napotykasz się na bardzo złego krola")
                            print("ktory torturuje swoich poddanych")
                            print("i zostałeś wezwany by go unicestwić")
                            print("co zamierzasz uczynić")
                            print("zabijam go,próbuje go przekonać aby się zmienił,uciekam")
                            krolewicz = input()
                            if krolewicz == "uciekam":
                                print("nie ma ucieczki")
                                postac[1] -= krol[2]
                            elif krolewicz == "próbuje go przekonać aby się zmienił":
                                print("nie mam takiego zamiaru")
                                print("ale moge cie zabić")
                                postac[1] -= krol[2]
                            elif krolewicz == "zabijam go":
                                krol[0] -= postac[1]
                                print(krol)
                                print(postac)
                            if krol[0] <= 0:
                                print("udało ci sie zgładzić złego krola")
                                print("gratulacje za przejście mojej malej gry")
                                print("yipee")


        if postac[0] <= 0:
                print("game over")  
