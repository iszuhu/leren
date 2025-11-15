woorden = {'wachten':'attendre',
           'verwarren':'confondre',
           'overeenkomen/corresponderen':'correspondre'}

for fr_woord in woorden:
    nl = input(f"wat betekent {woorden[fr_woord]} in het Frans")
    if nl == fr_woord:
        print('goed gedaan.')
    else:
        print('dat is niet goed.')
