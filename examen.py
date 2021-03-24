def get_list(fichero):
    f = open(fichero, mode="rt", encoding="utf-8")
    dic = {}
    linea = f.readline()
    while linea != "":
        palabras = linea.split(" ")
        for i in range(len(palabras)):
            palabra = palabras[i].replace("\n", "")
            if dic[len(palabra)] == None:
                dic[len(palabra)] = list()
            dic[len(palabra)].append(palabra)
    return dic
    

print(get_list("palabras.txt"))