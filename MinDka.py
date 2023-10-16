import sys

skup_stanja=[]
abeceda=[]
prihvatljiva_stanja=[]
neprihvatljiva_stanja=[]
pocetno_stanje=[]
prijelazi=[]
dohvatljiva_stanja=[]
stanje_i_simbol=[]
sljedeca_stanja=[]
treba_maknuti = []
rjecnik = {}

def nedohvatljivost(stanje, abeceda, stanje_i_simbol, sljedeca_stanja, dohvatljiva_stanja):
    if stanje in dohvatljiva_stanja:
        return
    dohvatljiva_stanja.append(stanje)
    for j in abeceda:
        if (stanje + "," + j) in stanje_i_simbol:
            if sljedeca_stanja[stanje_i_simbol.index(stanje + "," + j)] not in dohvatljiva_stanja:
                nedohvatljivost(sljedeca_stanja[stanje_i_simbol.index(stanje + "," + j)], abeceda, stanje_i_simbol, sljedeca_stanja, dohvatljiva_stanja)


def minimizacija(par_stanja, abeceda, prihvatljiva_stanja, neprihvatljiva_stanja, parovi1, parovi2, nesto_krivo):
    l = sorted(par_stanja)
    parovi1.append(l)
    parovi2.append(par_stanja)
    #print(par_stanja)
    #print(list(par_stanja)[0] + list(par_stanja)[1])

    if (list(par_stanja)[0] in prihvatljiva_stanja and list(par_stanja)[1] in neprihvatljiva_stanja):
        nesto_krivo[0]=False
        #print("uslo u nesto krivo")
    elif (list(par_stanja)[1] in prihvatljiva_stanja and list(par_stanja)[0] in neprihvatljiva_stanja):
        nesto_krivo[0]=False
        #print("uslo u nesto krivo")
    
    if (nesto_krivo[0]==False):
        return
        
    for i in abeceda:
        novi_par_stanja = set()
        for j in par_stanja:
            novi_par_stanja.add(rjecnik.get((j,i)))
        #print(novi_par_stanja)
        if len(novi_par_stanja)==1:
            continue   
        if (novi_par_stanja not in parovi2):
            minimizacija(novi_par_stanja, abeceda, prihvatljiva_stanja, neprihvatljiva_stanja, parovi1, parovi2, nesto_krivo)

def printanje(lista):
    if (len(lista)==0):
        print()
    for i in lista:
        if i==lista[len(lista)-1]:
            print(i)
        else:
            print(i, end=",")
                    


def main():
    
    i=1
    for line in sys.stdin:
        if i<=4:
            if i==1:
                skup_stanja=line.strip().split(",")
            if i==2:
                abeceda=line.strip().split(",")
            if i==3:
                prihvatljiva_stanja=line.strip().split(",")
            if i==4:
                pocetno_stanje=line.strip()
            i+=1
        else:
            prijelazi.append(line.strip())

    index=0
    for prijelaz in prijelazi:
        prijelazi[index]=prijelaz.split("->")
        index+=1


    

    for prijelaz in prijelazi:
        #print(prijelaz)
        stanje_i_simbol.append(prijelaz[0])
        sljedeca_stanja.append(prijelaz[1])

    nedohvatljivost(pocetno_stanje, abeceda, stanje_i_simbol, sljedeca_stanja, dohvatljiva_stanja)
    dohvatljiva_stanja.sort()

    #print(dohvatljiva_stanja)
    #print(prihvatljiva_stanja)
    

    for i in stanje_i_simbol:
        if i.split(",")[0] not in dohvatljiva_stanja:
            treba_maknuti.append(i)

    for i in treba_maknuti:
        sljedeca_stanja.pop(stanje_i_simbol.index(i))
        stanje_i_simbol.remove(i)

    new_prihvatljiva_stanja = []
    for i in prihvatljiva_stanja:
        if i in dohvatljiva_stanja:
            new_prihvatljiva_stanja.append(i)

    prihvatljiva_stanja = new_prihvatljiva_stanja

    for i in dohvatljiva_stanja:
        if i not in prihvatljiva_stanja:
            neprihvatljiva_stanja.append(i)

    for i in range(len(stanje_i_simbol)):
        stanje, simbol = stanje_i_simbol[i].split(",")
        rjecnik[(stanje, simbol)] = sljedeca_stanja[i]

    #print(prihvatljiva_stanja)
    
    svi_parovi=[]
    #print(svi_parovi)
    #print(parovi1)
    if (len(prihvatljiva_stanja)>1):
        for i in range(len(prihvatljiva_stanja)):
            for j in range(i+1, len(prihvatljiva_stanja)):
                par_stanja = {prihvatljiva_stanja[i], prihvatljiva_stanja[j]}
                #print(par_stanja)
                parovi1 = []
                parovi2 = []
                nesto_krivo = [True]
                minimizacija(par_stanja, abeceda, prihvatljiva_stanja, neprihvatljiva_stanja, parovi1, parovi2, nesto_krivo)
            if (nesto_krivo[0] == True and parovi1 not in svi_parovi):
                svi_parovi.append(parovi1)

    if (len(neprihvatljiva_stanja)>1):
        for i in range(len(neprihvatljiva_stanja)):
            for j in range(i+1, len(neprihvatljiva_stanja)):
                par_stanja = {neprihvatljiva_stanja[i], neprihvatljiva_stanja[j]}
                parovi1 = []
                parovi2 = []
                nesto_krivo = [True]
                minimizacija(par_stanja, abeceda, prihvatljiva_stanja, neprihvatljiva_stanja, parovi1, parovi2, nesto_krivo)
            if (nesto_krivo[0] == True and parovi1 not in svi_parovi):
                svi_parovi.append(parovi1)
    

    #print(svi_parovi)
    veliko=[]
    for veliki_par in svi_parovi:
        #print(veliki_par)
        #print()
        for par in veliki_par:
            #print(par)
            veliko.append(par)
            
    #print(veliko)

    for i in range(len(veliko)):
        for j in range(i+1,len(veliko)):
            if (veliko[i][1]==veliko[j][1] and veliko[i]!=veliko[j]):
                veliko[j][1]=veliko[j][0]
                veliko[j][0]=veliko[i][0]

    for i in veliko:
        i.sort()

    #print()

    #print(veliko)
    #print("ide velikooo")

    for par in veliko:
            #print(par)
            if (par[1] in prihvatljiva_stanja):
                prihvatljiva_stanja.remove(par[1])
            elif (par[1] in neprihvatljiva_stanja):
                neprihvatljiva_stanja.remove(par[1])
            if (par[1] in dohvatljiva_stanja):
                dohvatljiva_stanja.remove(par[1])
            if (par[1]==pocetno_stanje):
                pocetno_stanje=par[0]
            #print("prih: ", end="")
            #print(prihvatljiva_stanja)

            for key, value in rjecnik.items():
                if value == par[1]:
                    rjecnik[key]=par[0]

            for slovo in abeceda:
                #print((par[1], slovo) in rjecnik)
                if (par[1], slovo) in rjecnik:
                    del(rjecnik[(par[1], slovo)])

    

    printanje(dohvatljiva_stanja)
    printanje(abeceda)
    printanje(prihvatljiva_stanja)
    print(pocetno_stanje)

    for key, value in rjecnik.items():
        print(key[0] + ',' + key[1] + '->' + value)


    
    


    '''print(skup_stanja)
    print(neprihvatljiva_stanja)
    print(stanje_i_simbol)
    print(sljedeca_stanja)
    print(rjecnik)'''
    
    

main()