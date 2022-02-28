def analisa_info(informacoes):



    total_por_ano = {}
    total_sexo = {}
    total_regiao = {}
    total_mais_de_quarenta = 0
    municipiorj = []


    for chave in informacoes:
        for valor in informacoes[chave]:

            if chave == 'ano':

                if valor in total_por_ano:


                    total_por_ano[valor] += 1

                else:
                    total_por_ano[valor] = 0
                    total_por_ano[valor] += 1

            if chave == 'regiao':
                if valor in total_regiao:

                    total_regiao[valor] += 1

                else:
                    total_regiao[valor] = 0
                    total_regiao[valor] += 1

            if chave == 'sexo':
                if valor in total_sexo:

                    total_sexo[valor] += 1

                else:
                    total_sexo[valor] = 0
                    total_sexo[valor] += 1

            if chave == 'idade':
                if valor > '40':
                    total_mais_de_quarenta += 1


            if chave == 'municipio':
                if 'RJ' in valor:
                    municipiorj.append(valor[1])

    print("O total de participantes por ano é:")
    print(total_por_ano)
    print("O total de participantes por região é:")
    for x in total_regiao:
        if '1' in x:
            print("Norte: {} ".format(total_regiao[x]))
        if '2' in x:
            print("Nordeste: {} ".format(total_regiao[x]))
        if '3' in x:
            print("Sudeste: {} ".format(total_regiao[x]))
        if '4' in x:
            print("Sul: {} ".format(total_regiao[x]))
        if '5' in x:
            print("Centro-oeste: {} ".format(total_regiao[x]))

    print("O total de participantes por sexo é:")
    for x in total_sexo:
        if '1' in x:
            print("Homens: {} ".format(total_sexo[x]))
        if '2' in x:
            print("Mulheres: {} ".format(total_sexo[x]))

    print("O total de participantes acima de 40 anos é:")
    print(total_mais_de_quarenta)
    print("Os municípios do Rio de Janeiro participantes são:")
    print(municipiorj)