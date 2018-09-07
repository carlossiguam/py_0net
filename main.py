from ejemplo.factoria import Factoria

if __name__ == '__main__':
    mi_factoria = Factoria()
    persona = mi_factoria.get_persona("Guido Van Rosum", 30, 'F')
    print(persona)


