from libro import Libro
form autor import Autor


def get_list(fichero):
    f = open(fichero, mode="rt", encoding="utf-8")
    if f.read() == "":
        f.close()
        raise ValueError("El fichero está vacío.")
    else:
        f.seek(0)
        dic = {}
        linea = f.readline()
        while linea != "":
            palabras = linea.split(" ")
            for i in range(len(palabras)):
                palabra = palabras[i].replace("\n", "")
                if dic.get(len(palabra)) == None:
                    dic[len(palabra)] = list()
                dic[len(palabra)].append(palabra)
            linea = f.readline()
        f.close()
        return dic


def mas_antiguos(libros, anyo):
    lista_antiguos = list()
    for i in range()


# main
try:
    print(get_list("palabras.txt"))
except ValueError:
    print("El fichero está vacío.")

try:
    print(get_list("vacio.txt"))
except ValueError:
    print("El fichero está vacío.")


libros = [Libro("Anónimo", "Lazarillo", 1352), Libro("Cervantes", "Quijote", 1462), Libro("Anónimo", "Hola", 2000)]
mas_antiguos(libros, 1500)
