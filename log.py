import psycopg2
import csv

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
            self.cursor.execute("""INSERT INTO logtable VALUES (%s, %s, %s, %s, %s, %s, %s, %s);""", (
                1, variables[var[0]], variables[var[1]], variables[var[2]], variables[var[3]], variables[var[4]], variables[var[5]], variables[var[6]]))

        except (Exception, psycopg2.DatabaseError) as error:
            print("Deu caca: ")
            print(error)

        return 0

    def verificaRedo(self):
        self.i = 0
        for self.item in res_list:
            self.instrucao = self.item
            self.instrucao = self.instrucao.replace("<", "")
            self.instrucao = self.instrucao.replace(">", "")
            if 'commit' in self.instrucao:
                lista1 = list(self.instrucao.split(' ', 2))
                redo.append(lista1[1])
            else:
                if 'start' in self.instrucao:
                    lista3 = list(self.instrucao.split(' ', 2))
                    tr = lista3[1]
                    if tr in redo:
                        pass
                else:
                    if 'Start' in self.instrucao:
                        check = redo
                    else:
                        pass

            self.i += 1

    def redoBeforeCheck(self):
        self.checkpoint = False
        self.i = 0
        self.save = -1
        for self.item in res_list:
            self.instrucao = self.item
            self.instrucao = self.instrucao.replace("<","")
            self.instrucao = self.instrucao.replace(">","")
            if 'commit' in self.instrucao:
                lista1 = list(self.instrucao.split(' ', 2))
                if self.checkpoint == True:
                    redo.remove(lista1[1])
                else:
                    pass
            else:
                #aqui vão os casos das outras instruções
                if 'start' in self.instrucao:
                    pass
                else :
                    if 'Start' in self.instrucao: #considera o checkpoint
                        if not self.checkpoint:
                            self.save = self.i; #salva a posição em que o checkpoint foi encontrado
                            self.checkpoint = True
                        else:
                            pass

            self.i += 1
            if self.checkpoint == True:
                while self.i != self.save:
                    if res_list[self.i][:1] == 'T':
                        #a ultima instrução que faltou foi a opereção
                        if self.instrucao in redo:
                            variables[res_list[self.i+1]] = res_list[self.i+3].replace(">", "")
                        else:
                            pass
                    else:
                        if res_list[self.i][:1] == 'c':
                            lista1 = list(res_list[i].split(' ', 2))
                            redo.remove(lista1[1])
                        else:
                            pass
                    self.i -= 1

    def executeRedo(self):
        self.i = 0
        for self.item in res_list:
            self.instrucao = self.item
            self.instrucao = self.instrucao.replace("<","")
            self.instrucao = self.instrucao.replace(">","")
            if 'commit' in self.instrucao:
                pass
            else:
                if 'start' in self.instrucao:
                    pass
                else :
                    if 'Start' in self.instrucao:
                        #o checkpoint não faz diferença
                        pass
                    else:
                        if self.instrucao[:1] == 'T':
                            #a ultima instrução que faltou foi a opereção
                                if self.instrucao in redo:
                                    variables[res_list[self.i+1]] = res_list[self.i+3].replace(">", "")
                                else:
                                    pass
                        else:
                            pass
            self.i += 1


variables = {'A': 20, 'B': 20, 'C': 70, 'D': 50, 'E': 17, 'F': 1, 'G': 0}
var = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
varlenght = 7
redo = []
check = []
arquivo = []

with open('teste.txt', newline='') as inputfile:
    for row in csv.reader(inputfile):
        arquivo.append(row)

arquivo.reverse()

res_list = [item for list2 in arquivo for item in list2]

banco = Banco()
banco.connect()
banco.restoreOriginal()
banco.verificaRedo()

print("Redo:")
print(redo)
print("Check:")
print(check)
print("Variables:")
print(variables)
print()
input()

banco.redoBeforeCheck()

print("Redo:")
print(redo)
print("Check:")
print(check)
print("Variables:")
print(variables)
print()
input()

banco.executeRedo()
print("Variables:")
print(variables)
print()
input()