import time
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            'ROFL': 'una respuesta a una broma',
            'SHEESH': 'ligera desaprobación',
            'CREEPY': 'aterrador, siniestro',
            'AGGRO': 'ponerse agresivo/enojado'
            }
            
for i in range(5):
    print('hola')
    time.sleep(1)
    print('estamos aqui para ayudarte para expandir tu diccionario... :D')
    time.sleep(1)
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    time.sleep(1)
    print('generando...')
    time.sleep(2)

    if word in meme_dict.keys():
        print(meme_dict[word])
        time.sleep(2)
    else:
        print('no se ha encontrado el significado... :C')
        time.sleep(2) 