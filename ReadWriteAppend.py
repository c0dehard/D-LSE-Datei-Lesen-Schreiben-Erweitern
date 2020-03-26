import os
programRuns = True
# TODO: modernize, optimize this
# TODO: translate to english (readablity for anyone)
def read():
    print("Readmode[ "+datei+" ]\n")
    print(f.read())

def write():
    f.write(str(input("Writemode[ "+datei+" ]\n")))


def append():
    f.write(str(input("Appendmode [ "+datei+" ]\n")))

while programRuns:
    #bc im on UNIX-Like system, this negation makes more sence
    os.system('clear' if os.name != 'nt' else 'cls')
    datei = str(input('File > '))
    modus = str(input("'r' read | 'w' write | 'a' append\n"))
    f = open (datei,modus)
    if modus == "r": #ergab fehler mit '' #what the.. not sure anymore, need to check
        read()
    elif modus == "w":
        write()
    elif modus == "a":
        append()
    weiter = input("\nContinue? y/n\n")
    if weiter == 'n':
        f.close()
        print('Thanks, good bye!')
        programRuns = False #HAHAHA embarrassing dear reader, this was an older sourcecode of mine, I am sorry!
    elif weiter =='y':
        f.close() # just ignore this for now
