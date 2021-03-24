from libro import Libro
from autor import Autor

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

def mas_antiguos(libros, anyo_limite):
    if anyo_limite < 1900 or anyo_limite > 2021:
        raise ValueError("El año no es válido.")
    else:
        lista_antiguos = list()
        for i in range(len(libros)):
            if libros[i].anyo < anyo_limite:
                lista_antiguos.append(libros[i].titulo)
        return lista_antiguos

# main
if __name__ == "__main__":
    try:
        print(get_list("palabras.txt"))
    except ValueError:
        print("El fichero está vacío.")

    try:
        print(get_list("vacio.txt"))
    except ValueError:
        print("El fichero está vacío.")

    libros = [Libro(1, "Lazarillo", 1352), Libro(2, "Quijote", 1462), Libro(3, "Hola", 2000)]
    try:
        print(mas_antiguos(libros, 2000))
    except ValueError:
        print("El año no es válido.")