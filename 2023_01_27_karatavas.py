# Uvis Virsnītis 11.4.
from random import randint
from colorama import Back, Fore, Style

while True:
    vardu_izvele=["vien", "divi", "tris", "cits"]
    vards=vardu_izvele[randint(0,len(vardu_izvele)-1)]
    dzivibas=5
    minetais_vards=list("_" for _ in vards)
    while(dzivibas>0 and not "".join(minetais_vards) == vards):
        minejums=str(input("Ievadiet minējumu (vārds)-> "))
        if len(minejums)<1: continue
        if len(minejums) != len(vards): continue

        for aaa in range(0, len(vards)):
            if vards[aaa]==minejums[aaa]:
                minetais_vards[aaa]=minejums[aaa]
                print(f"{Fore.GREEN}{minejums[aaa]}{Style.RESET_ALL}", end="")
            elif minejums[aaa] in vards:
                print(f"{Fore.YELLOW}{minejums[aaa]}{Style.RESET_ALL}", end="")
            else:
                print(f"{minejums[aaa]}", end="")
        print()

        dzivibas -= 1

    if(dzivibas > 0): 
        print("UZVARA! HOOOORAAAHHH!")
    else:
        print("Zaudēts beeeeeeeee NI")

    if input("Vai beigt spēli? (Y/N)")[0].lower() == "y":
        break