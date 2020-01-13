import os
programRuns = True

def read():
    print("Lesemodus[ "+datei+" ]\n")
    print(f.read())

def write():
    f.write(str(input("Schreibmodus[ "+datei+" ]\n")))


def append():
    f.write(str(input("Erweiterungsmodus [ "+datei+" ]\n")))

while programRuns:
    os.system('cls' if os.name == 'nt' else 'clear')
    datei = str(input("Pfad oder Dateiname\n~> "))
    modus = str(input("'r' read | 'w' write | 'a' append\n"))
    f = open (datei,modus)
    if modus == "r": #ergab fehler mit ''
        read()
    elif modus == "w":
        write()
    elif modus == "a":
        append()
    weiter = input("\nWeitermachen? j/n\n")
    if weiter == 'n':
        f.close()
        print('Danke, bis demnächst!')
        programRuns = False
    elif weiter =='j':
        f.close()
    else print('Ungültige eingabe')
os.system('cls' if os.name == 'nt' else 'clear')
