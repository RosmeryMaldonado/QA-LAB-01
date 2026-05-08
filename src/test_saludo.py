def saludar(nombre):
        return f"Hola : {nombre}"

#creo mi prueba 
def test_saludar():
            assert saludar("Ana") == "Hola : Ana"