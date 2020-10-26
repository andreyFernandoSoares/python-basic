def escrevendo():
    arquivo = open("C:\\Users\\Andrey Soares\\Desktop\\PythonProjects\\python-basic\\frutas.txt", "w")
    arquivo.write("banana \n")
    arquivo.write("mamao \n")
    arquivo.write("laranja \n")
    arquivo.write("melancia \n")
    arquivo.close

if (__name__ == "__main__"):
    escrevendo()