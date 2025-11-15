import random
fr_woord = {'wachten':'attendre',
           'verwarren':'confondre',
           'overeenkomen':'correspondre',
           'corresponderen':'correspondre'}

def van_fr_naar_nl():
    woorden = list(fr_woord.keys())
    random.shuffle(woorden)
    for nl_woord in fr_woord:
        nl = input(f"wat betekent {fr_woord[nl_woord]} in het Frans")
        if nl == nl_woord:
            print('goed gedaan.')
        else:
            print('dat is niet goed.')

def van_nl_naar_fr():
    woorden=list(fr_woord.keys())
    random.shuffle(woorden)
    for nl_woord in woorden:
        fr = input(f"wat betekent {nl_woord} in het Frans \n")
        if fr == fr_woord[nl_woord]:
            print('goed gedaan.')
        else:
            print('dat is niet goed.')

van_nl_naar_fr()
