import psycopg2
import re

class Banco:
    def connect(self):
        try:
            self.connection = psycopg2.connect(
                user="postgres", password="root", host="127.0.0.1", database="log")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()

        except (Exception, psycopg2.DatabaseError) as error:
            print("Deu caca\n")
            print(error)

    def restoreOriginal(self):
        try:
            self.cursor.execute("""DELETE FROM logtable;""")
            self.cursor.execute("""INSERT INTO logtable VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);""", (1, variables[var[0]], variables[var[1]], variables[var[2]], variables[var[3]], variables[var[4]], variables[var[5]], variables[var[6]], variables[var[7]]))

        except (Exception, psycopg2.DatabaseError) as error:
            print("Deu caca: ")
            print(error)

        return 0

    def verificaRedo(self):
        pass

    def executeRedo(self):
        pass


REDO = []

variables = {'A': 20, 'B': 20, 'C': 70, 'D': 50, 'E': 17, 'F': 1, 'G': 0, 'H': '0'}
var = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

arquivo = open('teste.txt', 'r')
arquivolist = list(arquivo)     #cria uma lista com o .txt

#Variaveis p/ identificar se existe no .txt
checkvalue = re.compile(r'T[0-9]*,', re.IGNORECASE) #re.IGNORECASE -> ignorar se maiuscula ou minuscula
commit = re.compile(r'commit', re.IGNORECASE) #re.IGNORECASE -> ignorar se maiuscula ou minuscula
extracT = re.compile(r'(?!commit\b)(?!CKPT\b)(?!Start\b)\b\w+', re.IGNORECASE) #Ignora as palavras descritas e coloca as demais em uma lista com .findall
words = re.compile(r'\w+', re.IGNORECASE)   #Utilizado p/ pegar o valor das variaveis

banco = Banco()
banco.connect()
banco.restoreOriginal()

for linha in reversed(arquivolist): #Verificar os casos e criar as listas de REDO
    if commit.search(linha):  #Procura commit
        REDO.append(extracT.findall(linha)[0])

print("Aplicado REDO:", REDO, "\n")

for j in range(1,len(arquivolist)-1,1):
    linha = arquivolist[j]    
    if (checkvalue.search(linha)):
        if(extracT.findall(linha)[0] in REDO):           
            variables[words.findall(linha)[1]] = words.findall(linha)[2]

print("Resultado:", variables)
arquivo.close()