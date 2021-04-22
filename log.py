import psycopg2
import re

class Banco:
    def connect(self):
        try:
            self.connection = psycopg2.connect(user="postgres", password="root", host="127.0.0.1", database="log")
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
        self.cursor.execute("""SELECT A FROM logtable where id = 1;""")
        dados = self.cursor.fetchall()
        dado = str(dados[0]).replace("(", "")
        dado = dado.replace(")","")
        dado = dado.replace(",","")

        if(int(dado) == variables['A']):
            pass
        else:
            try:
                self.cursor.execute("""update logtable set A = {0} where id = 1;""".format(variables['A']))
                input()

            except (Exception, psycopg2.DatabaseError) as error:
                print("Deu caca: ")
                print(error)
            
            print("Valor A atualizado")

        self.cursor.execute("""SELECT B FROM logtable where id = 1;""")
        dados1 = self.cursor.fetchall()
        dado = str(dados1[0]).replace("(", "")
        dado = dado.replace(")","")
        dado = dado.replace(",","")
        if(int(dado) == variables['B']):
            pass
        else:
            try:
                self.cursor.execute("""update logtable set B = {0} where id = 1;""".format(variables['B']))

            except (Exception, psycopg2.DatabaseError) as error:
                print("Deu caca: ")
                print(error)
            
            print("Valor B atualizado")

        self.cursor.execute("""SELECT C FROM logtable where id = 1;""")
        dados2 = self.cursor.fetchall()
        dado = str(dados2[0]).replace("(", "")
        dado = dado.replace(")","")
        dado = dado.replace(",","")
        if(int(dado) == variables['C']):
            pass
        else:
            try:
                self.cursor.execute("""update logtable set C = {0} where id = 1;""".format(variables['C']))

            except (Exception, psycopg2.DatabaseError) as error:
                print("Deu caca: ")
                print(error)
            
            print("Valor C atualizado")

        self.cursor.execute("""SELECT D FROM logtable where id = 1;""")
        dados3 = self.cursor.fetchall()
        dado = str(dados3[0]).replace("(", "")
        dado = dado.replace(")","")
        dado = dado.replace(",","")
        if(int(dado) == variables['D']):
            pass
        else:
            try:
                self.cursor.execute("""update logtable set D = {0} where id = 1;""".format(variables['D']))

            except (Exception, psycopg2.DatabaseError) as error:
                print("Deu caca: ")
                print(error)
            
            print("Valor D atualizado")

        self.cursor.execute("""SELECT E FROM logtable where id = 1;""")
        dados4 = self.cursor.fetchall()
        dado = str(dados4[0]).replace("(", "")
        dado = dado.replace(")","")
        dado = dado.replace(",","")
        if(int(dado) == variables['E']):
            pass
        else:
            try:
                self.cursor.execute("""update logtable set E = {0} where id = 1;""".format(variables['E']))

            except (Exception, psycopg2.DatabaseError) as error:
                print("Deu caca: ")
                print(error)
            
            print("Valor E atualizado")

        self.cursor.execute("""SELECT F FROM logtable where id = 1;""")
        dados5 = self.cursor.fetchall()
        dado = str(dados5[0]).replace("(", "")
        dado = dado.replace(")","")
        dado = dado.replace(",","")
        if(int(dado) == variables['F']):
            pass
        else:
            try:
                self.cursor.execute("""update logtable set F = {0} where id = 1;""".format(variables['F']))

            except (Exception, psycopg2.DatabaseError) as error:
                print("Deu caca: ")
                print(error)
            
            print("Valor F atualizado")

        self.cursor.execute("""SELECT G FROM logtable where id = 1;""")
        dados6 = self.cursor.fetchall()
        dado = str(dados6[0]).replace("(", "")
        dado = dado.replace(")","")
        dado = dado.replace(",","")
        if(int(dado) == variables['G']):
            pass
        else:
            try:
                self.cursor.execute("""update logtable set G = {0} where id = 1;""".format(variables['G']))

            except (Exception, psycopg2.DatabaseError) as error:
                print("Deu caca: ")
                print(error)
            
            print("Valor G atualizado")

        self.cursor.execute("""SELECT H FROM logtable where id = 1;""")
        dados7 = self.cursor.fetchall()
        dado = str(dados7[0]).replace("(", "")
        dado = dado.replace(")","")
        dado = dado.replace(",","")
        if(int(dado) == variables['H']):
            pass
        else:
            try:
                self.cursor.execute("""update logtable set H = {0} where id = 1;""".format(variables['H']))

            except (Exception, psycopg2.DatabaseError) as error:
                print("Deu caca: ")
                print(error)
            
            print("Valor H atualizado")

    def fezRedo(self):
        self.final = 0
        for linha in reversed(arquivolist): 
            if 'Start CKPT' in linha:
                if self.final: 
                    check = extracT.findall(linha)
                    print("Start Checkpoint em", check)         
                    break

            elif 'commit' in linha:
                check = extracT.findall(linha)[0]
                REDO1.append(check)

            elif 'End CKPT' in linha:
                self.final += 1

        print("\nAplicar REDO nas transações:", REDO1)

    def valoresAtuais(self):
        try:
            self.cursor.execute("""SELECT * FROM logtable;""")

        except (Exception, psycopg2.DatabaseError) as error:
            print("Deu caca: ")
            print(error)


        print("Valores no banco:")
        self.data = self.cursor.fetchall()
        for self.row in self.data:
            print(self.row)

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

REDO = []
REDO1 = []

#variables = {'A': 20, 'B': 20, 'C': 70, 'D': 50, 'E': 17, 'F': 1, 'G': 0, 'H': 0}
variables = {'A': 32, 'B': 30, 'C': 90, 'D': 40, 'E': 28, 'F': 2, 'G': 0, 'H': 0}
var = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

arquivo = open('teste1.txt', 'r')
arquivolist = list(arquivo)     #cria uma lista com o .txt

checkvalue = re.compile(r'T[0-9]*,', re.IGNORECASE) #re.IGNORECASE -> ignorar se maiuscula ou minuscula
commit = re.compile(r'commit', re.IGNORECASE) #re.IGNORECASE -> ignorar se maiuscula ou minuscula
extracT = re.compile(r'(?!commit\b)(?!CKPT\b)(?!Start\b)\b\w+', re.IGNORECASE) #Ignora as palavras descritas e coloca as demais em uma lista com .findall
words = re.compile(r'\w+', re.IGNORECASE)   #Utilizado p/ pegar o valor das variaveis

banco = Banco()
banco.connect()

print("Valores iniciais - ", variables)

banco.restoreOriginal() #restaurar banco

for linha in reversed(arquivolist): #Verificar os casos e criar as listas de REDO
    if commit.search(linha):  #Procura commit
        REDO.append(extracT.findall(linha)[0])

for j in range(1,len(arquivolist)-1,1):
    linha = arquivolist[j]    
    if (checkvalue.search(linha)):
        if(extracT.findall(linha)[0] in REDO):           
            variables[words.findall(linha)[1]] = words.findall(linha)[2]

banco.fezRedo() #indica quais transações irão realizar o redo
banco.verificaRedo() #executará o redo no banco
banco.valoresAtuais() #irá printar os valores que estão no banco
banco.disconnect() #desconectar banco