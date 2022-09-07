class vertice:
    def __init__(self,dado,dado1):
        self.dado=dado
        self.dado1=dado1
        self.grauEntrada=0
        self.grauSaida=0
    def getDado(self):
        return self.dado
    def getGrauEntrada(self):
        return self.grauEntrada
    def getGrauSaida(self):
        return self.grauSaida
    def addGrauSaida(self):
        self.grauSaida+=1
    def removeGrauSaida(self):
        self.grauSaida-=1
    def addGrauEntrada(self):
        self.grauEntrada+=1
    def removeGrauEntrada(self):
        self.grauEntrada-=1
    def printarDados(self):
        print(self.dado)
        print(self.qntArestas)
    
class aresta:
    def __init__(self,origem,destino):
        self.origem=origem
        self.destino=destino
    def getOrigem(self):
        return self.origem
    def getDestino(self):
        return self.destino
    
class Grafo:
    def __init__(self,direcionado=False):
        self.lista_vertices = []
        self.lista_arestas = []
        self.direcionado = direcionado
        
    def insere_v(self,dado,dado1=None):
        self.lista_vertices.append(vertice(dado,dado1))
        
    def veri_vertice(self,vertice):
        for i in self.lista_vertices:
            if i.dado == vertice:
                return i
        else:
            return None
        
    def insere_a(self,u,v):
        origem= self.veri_vertice(u)
        destino= self.veri_vertice(v)
        
        if origem != None and destino != None:
            self.lista_arestas.append(aresta(u,v))
            for i in self.lista_vertices:
                if i.dado == origem.dado:
                    i.addGrauSaida()
                    break
            for i in self.lista_vertices:
                if i.dado == destino.dado:
                    i.addGrauEntrada()
                    break
            
        if self.direcionado:
            self.lista_arestas.append(aresta(v,u))
            for i in self.lista_vertices:
                if i.dado == destino.dado:
                    i.addGrauSaida()
                    break
            for i in self.lista_vertices:
                if i.dado == origem.dado:
                    i.addGrauEntrada()
                    break
                    
    def remove_a(self,u,v):
        origem= self.veri_vertice(u)
        destino= self.veri_vertice(v)
        if origem != None and destino != None:
            for i in self.lista_arestas:
                if i.origem == u and i.destino == v:
                    for j in self.lista_vertices:
                        if j.dado==u:
                            j.removeGrauSaida()
                    for j in self.lista_vertices:
                        if j.dado==v:
                            j.removeGrauEntrada()
                    self.lista_arestas.remove(i)
            if self.direcionado:
                for i in self.lista_arestas:
                    if i.origem == v and i.destino == u:
                        for j in self.lista_vertices:
                            if j.dado==v:
                                j.removeGrauSaida()
                        for j in self.lista_vertices:
                            if j.dado==u:
                                j.removeGrauEntrada()
                        self.lista_arestas.remove(i)
    def remove_v(self,u):
        vertice=self.veri_vertice(u)
        l=[]
        if vertice != None:
            for i in self.lista_vertices:
                if i.dado == u:
                    l.append(i)
            for i in l:
                self.lista_vertices.remove(i)
            l=[]
            for i in self.lista_arestas:
                if i.origem == u or i.destino == u:
                    if i.origem != u:                        
                        for j in self.lista_vertices:
                            if j.dado == i.origem:
                                j.removeGrauSaida()
                    else:
                        for j in self.lista_vertices:
                            if j.dado == i.destino:
                                j.removeGrauEntrada()
                    l.append(i)
            for i in l:                       
                self.lista_arestas.remove(i)
    def printarTodosOsDados(self):
        for i in self.lista_vertices:
            x=0
            print(f'Vertice : {i.dado}')
            print(f'Grau Saida: {i.grauSaida}')
            print(f'Grau Entrada: {i.grauEntrada}')
            l=[]
            for j in self.lista_arestas: 
                if j.origem == i.dado:
                    l.append([j.origem,j.destino])
                    x=1
            if x:
                print('Arestas:',end=' ')
            for i in l:  
                print(" -> ".join([str(i[0]),str(i[-1])]),end='')
                if i != l[-1]:
                    print(' | ',end='')
                else:
                    print('\n',end='')
            else:
                if x == 0:
                    print('Não tem arestas')
                    
    def grau_saida(self,dado):
        for i in self.lista_vertices:
            if i.dado == dado:
                return i.grauSaida
        else:
            return 0
            
    def grau_entrada(self,dado):
        for i in self.lista_vertices:
            if i.dado == dado:
                return i.grauEntrada
        else:
            return 0
    def alcancavel(self,u,v):
        l=[]
        for i in self.lista_arestas:
            if i.origem == u:
                l.append(i)
        for i in l:
            if i.destino == v:
                return True
            else:
                self.alcancavel(i.destino,v)
        else:
            return False
                
b=Grafo(True)
b.insere_v(1)
b.insere_v(2)
b.insere_v(3)
b.insere_v(4)
b.insere_v(5)
b.insere_a(1,2)
b.insere_a(1,3)
b.insere_a(1,4)
b.insere_a(1,5)
b.insere_a(4,1)
b.remove_a(1,4)
b.remove_v(3)
b.printarTodosOsDados()        

