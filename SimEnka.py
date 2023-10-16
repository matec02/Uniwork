import sys

def izracun_eps_okruzenja(stanje, eps_okruzenje, stanje_i_simbol, sljedeca_stanja):
    
    if (stanje + ",$") in stanje_i_simbol:
        pre_eps=sljedeca_stanja[stanje_i_simbol.index(stanje + ",$")].split(",")
        for j in range(len(pre_eps)):
            if pre_eps[j] not in eps_okruzenje:
                eps_okruzenje.append(pre_eps[j])
                izracun_eps_okruzenja(pre_eps[j], eps_okruzenje, stanje_i_simbol, sljedeca_stanja)
                
    return

def main():
    nizovi=[]
    skup_stanja=[]
    abeceda=[]
    prihvatljiva_stanja=[]
    pocetno_stanje=[]
    prijelazi=[]
    skup=[]
    i=1
    for line in sys.stdin:
        if i<=5:
            if i==1:
                nizovi=line.strip().split("|")
            if i==2:
                skup_stanja=line.strip().split(",")
            if i==3:
                abeceda=line.strip().split(",")
            if i==4:
                prihvatljiva_stanja=line.strip().split(",")
            if i==5:
                pocetno_stanje=line.strip()
            i+=1
        else:
            prijelazi.append(line.strip())

    index=0
    for i in nizovi:
        nizovi[index]=i.split(",")
        index+=1

    index=0
    for prijelaz in prijelazi:
        prijelazi[index]=prijelaz.split("->")
        index+=1


    stanje_i_simbol=[]
    sljedeca_stanja=[]

    for prijelaz in prijelazi:
        stanje_i_simbol.append(prijelaz[0])
        sljedeca_stanja.append(prijelaz[1])


    eps_okruzenje=[]
    nakon_znaka=[]

    for niz in nizovi:
        eps_okruzenje.clear()
        nakon_znaka.clear()
        nakon_znaka.append(pocetno_stanje)
        for i in range(len(niz)):
            for stanje in nakon_znaka:
                izracun_eps_okruzenja(stanje, eps_okruzenje, stanje_i_simbol, sljedeca_stanja)
                if (stanje not in eps_okruzenje):
                    eps_okruzenje.append(stanje)
            if (len(eps_okruzenje)!=1 and "#" in eps_okruzenje):
                eps_okruzenje.remove("#")
            eps_okruzenje.sort()
            for l in range(len(eps_okruzenje)):
                if (l==len(eps_okruzenje)-1):
                    print(eps_okruzenje[l] + "|", end="")
                else:
                    print(eps_okruzenje[l] + ",", end="")
            nakon_znaka.clear()
            for stanje in eps_okruzenje:
                if stanje not in eps_okruzenje:
                    nakon_znaka.append(stanje)
                if (stanje + "," + niz[i]) in stanje_i_simbol:
                    sljedece_stanje=sljedeca_stanja[stanje_i_simbol.index(stanje + "," + niz[i])].split(",")
                    for k in range(len(sljedece_stanje)):
                        nakon_znaka.append(sljedece_stanje[k])
                else:
                    if ("#" not in nakon_znaka):
                        nakon_znaka.append("#")

            eps_okruzenje.clear()

            if (i==len(niz)-1):
                for stanje in nakon_znaka:
                    izracun_eps_okruzenja(stanje, eps_okruzenje, stanje_i_simbol, sljedeca_stanja)
                    if (stanje not in eps_okruzenje):
                        eps_okruzenje.append(stanje)
                if (len(eps_okruzenje)!=1 and "#" in eps_okruzenje):
                    eps_okruzenje.remove("#")
                eps_okruzenje.sort()
                for l in range(len(eps_okruzenje)):
                    if (l==len(eps_okruzenje)-1):
                        print(eps_okruzenje[l])
                    else:
                        print(eps_okruzenje[l] + ",", end="")
            

main()



        

