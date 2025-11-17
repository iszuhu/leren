import random
fr_woord = {'wachten':'attendre',
            'verwarren':'confondre',
            'overeenkomen':'correspondre',
            'corresponderen':'correspondre',
            'verliezen':'perdre',
            '(zich) verdedigen':'(se) défendre',
            'beweren':'prétendre',
            'afhangen(van)':'dépendre',
            'teruggeven':'rendre',
            'naar beneden gaan':'descendre',
            'afdalen':'descendre',
            '(zich) verspreiden':'(se) répandre',
            'zich ontspannen':'se détendre',
            'antwoorden':'répondre',
            'horen':'entendre',
            'verkopen':'vendre',
            'smelten':'fondre',
            'ophangen':'pendre',
            'bijten':'mordre'}

'''def van_fr_naar_nl():
    woorden = list(fr_woord.keys())
    random.shuffle(woorden)
    for nl_woord in fr_woord:
        nl = input(f"wat betekent {fr_woord[nl_woord]} in het Frans")
        if nl == nl_woord:
            print('goed gedaan.')
        else:
            print('dat is niet goed.')
'''
def van_nl_naar_fr():
    incorrectents = list(fr_woord.keys())
    woorden=incorrectents
    random.shuffle(woorden)
    while incorrectents:
        for nl_woord in woorden:
            fr = input(f"wat betekent {nl_woord} in het Frans \n")
            if fr == fr_woord[nl_woord]:
                print('goed gedaan.')
                incorrectents.remove(nl_woord)
            else:
                print(f'dat is niet goed.                           (het moest {fr_woord[nl_woord]} zijn...)')
        print(incorrectents)
    print('Je hebt de hele woordenlijst doorlopen.')
van_nl_naar_fr()