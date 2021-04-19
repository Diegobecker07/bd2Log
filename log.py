import psycopg2
import asyncio

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
            self.cursor.execute("""INSERT INTO logtable VALUES (%s, %s, %s, %s, %s, %s, %s, %s);""",(1, variables[var[0]], variables[var[1]], variables[var[2]], variables[var[3]], variables[var[4]], variables[var[5]], variables[var[6]]))
        
        except (Exception, psycopg2.DatabaseError) as error:
            print("Deu caca: ")
            print(error)

        return 0

    #def async def runTransaction(self):
        #pass
    
    #async def executeQuery(self):
        #pass

variables = {'A': 20, 'B': 20, 'C': 70, 'D': 50, 'E': 17, 'F': 1, 'G': 0}
var = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
varlenght = 7

arquivo = open('teste.txt', 'r')
arquivolist = list(arquivo)     #cria uma lista com o .txt

banco = Banco()
banco.connect()
banco.restoreOriginal()
