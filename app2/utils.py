def filtro(path):
    pais = str
    pais = str(input('Escribe el pais a graficar: '))
    pais = pais.title()
    '''
    df = path[path['Country/Territory'] == pais]
    df = df[df['Population'] in df]
    print(df)

    '''
    countrydict= filter(lambda p: p['Country/Territory'] == pais, path)
    population = {}
    for i in countrydict:
        for k,v in i.items():
            if 'Population' in k and not 'World' in k:
                population [k[:4]] = int(v)

    lables = population.keys()
    values = population.values()
    return lables, values, pais