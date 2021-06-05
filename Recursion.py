#
#  FUNKCE
#

def nice(val):
    if val == 1:
        print("▼ 0")
        print("\n\n  [KONEC]")
        return
    else:
        val = val - 1
        print("┃",val)
        nice(val)

def ziskat():
    global cislo
    try:
        cislo = int(input("Číslo: "))
    except:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n---------------------------------------------\n               To není číslo!\n---------------------------------------------\n\n")
        ziskat()
    if cislo > 995:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n---------------------------------------------\n             Zadej menší číslo!\n---------------------------------------------\n\n")
        ziskat()
    else:
        pass

#
# START
#

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n---------------------------------------------\n   Zadej, od jakého čísla mám počítat dolů\n---------------------------------------------\n\n")
ziskat()
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("  [ZAČÁTEK]\n\n")
print("┏", cislo)
nice(cislo)
