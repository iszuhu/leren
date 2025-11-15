woorden = {'wachten':'attendre',
           'verwarren':'confondre',
           'overeenkomen':'correspondre',
           'corresponderen':'correspondre'}

def van_fr_naar_nl():
    for nl_woord in woorden:
        nl = input(f"wat betekent {woorden[nl_woord]} in het Frans")
        if nl == nl_woord:
            print('goed gedaan.')
        else:
            print('dat is niet goed.')

def van_nl_naar_fr():
    for nl_woord in woorden:
        fr = input(f"wat betekent {nl_woord} in het Frans")
        if fr == woorden[nl_woord]:
            print('goed gedaan.')
        else:
            print('dat is niet goed.')

van_nl_naar_fr()