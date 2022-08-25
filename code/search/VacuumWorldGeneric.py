from SearchAlgorithms import BuscaProfundidadeIterativa
from Graph import State
import sys

class VacuumWorldGeneric(State):

    def __init__(self,vacuumPosition, room, op):
        self.vacuumPosition = vacuumPosition # [right, left]
        self.room = room; #[[]]
        self.roomlen = [len(room[0]), len(room)]
        self.operator = op # string that describes the operation

    def env(self):
        return str(self.vacuumPosition)+";"+str(self.room)

    def sucessors(self):
        sucessors = []
        newpos = self.vacuumPosition
        
        new_room = self.room
        new_room[self.vacuumPosition[0]][self.vacuumPosition[1]] = "L"
        sucessors.append(VacuumWorldGeneric(self.vacuumPosition, new_room, 'clean'))

        if(self.vacuumPosition[0] == self.roomlen[0]-1):
            sucessors.append(VacuumWorldGeneric(self.vacuumPosition, self.room, 'move_right'))
        else:
            newpos[0] += 1
            sucessors.append(VacuumWorldGeneric(newpos, self.room, 'move_right'))

        if(self.vacuumPosition[0] == 0):
            sucessors.append(VacuumWorldGeneric(self.vacuumPosition, self.room, 'move_left'))
        else:
            newpos[0] -= 1
            sucessors.append(VacuumWorldGeneric(newpos, self.room, 'move_left'))

        if(self.vacuumPosition[1] == self.roomlen[1]-1):
            sucessors.append(VacuumWorldGeneric(self.vacuumPosition, self.room, 'move_down'))
        else:
            newpos[1] += 1
            sucessors.append(VacuumWorldGeneric(newpos, self.room, 'move_down'))

        if(self.vacuumPosition[1] == 0):
            sucessors.append(VacuumWorldGeneric(self.vacuumPosition, self.room, 'move_up'))
        else:
            newpos[1] -= 1
            sucessors.append(VacuumWorldGeneric(newpos, self.room, 'move_up'))
        return sucessors
    
    def is_goal(self):
        for i in self.room:
            for j in i:
                if j == "S": return False
        return True
    
    def description(self):
        return "Describe the problem"
    
    def cost(self):
        return 1

    def print(self):
        #
        # Usado para imprimir a solução encontrada. 
        # O PATH do estado inicial até o final.
        return str(self.operator)
    
    def env(self):
        #
        # IMPORTANTE: este método não deve apenas retornar uma descrição do environment, mas 
        # deve também retornar um valor que descreva aquele nodo em específico. Pois 
        # esta representação é utilizada para verificar se um nodo deve ou ser adicionado 
        # na lista de abertos.
        #
        # Exemplos de especificações adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)+"#"+str(self.cost)
        # - para o problema das cidades: return self.city+"#"+str(self.cost())
        #
        # Exemplos de especificações NÃO adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)
        # - para o problema das cidades: return self.city
        #
        None

def read_input(path):
    with open(path) as f:
        lines = f.readlines()
    
    room = []
    for line in lines:
        line = line.strip()
        line = line.split(";")
        room.append(line)
    return room

def main():
    path = sys.argv[1]
    x = int(sys.argv[2])
    y = int(sys.argv[3])
    print('Busca em profundidade iterativa')

    room = read_input(path)
    state = VacuumWorldGeneric([x,y], room, '')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()