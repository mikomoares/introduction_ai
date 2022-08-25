from SearchAlgorithms import BuscaLargura
from SearchAlgorithms import BuscaProfundidade
from SearchAlgorithms import BuscaProfundidadeIterativa
from Graph import State

class VacuumWorld3Room(State):

    def __init__(self, vacuumPosition, isLeftRoomClean, isRightRoomClean, isCenterRoomClean, op):
        self.vacuumPosition = vacuumPosition # [right, left]
        self.isLeftRoomClean = isLeftRoomClean #[True, False]
        self.isRightRoomClean = isRightRoomClean #[True, False]
        self.isCenterRoomClean = isCenterRoomClean #[True, False]
        self.operator = op # string that describes the operation

    def env(self):
        return str(self.vacuumPosition)+";"+str(self.isLeftRoomClean)+";"+str(self.isRightRoomClean)+";"+str(self.isCenterRoomClean)
    
    def sucessors(self):
        sucessors = []
        # É necessario verificar a VacuumPos antes de mover a Vacuum?
        # Nao eh necessario
        if (self.vacuumPosition == 'right'):
            sucessors.append(VacuumWorld3Room('right', self.isLeftRoomClean, self.isRightRoomClean,self.isCenterRoomClean, 'Move Right'))
            sucessors.append(VacuumWorld3Room('center', self.isLeftRoomClean, self.isRightRoomClean,self.isCenterRoomClean, 'Move Left'))
        elif (self.vacuumPosition == 'center'):
            sucessors.append(VacuumWorld3Room('right', self.isLeftRoomClean, self.isRightRoomClean,self.isCenterRoomClean, 'Move Right'))
            sucessors.append(VacuumWorld3Room('left', self.isLeftRoomClean, self.isRightRoomClean,self.isCenterRoomClean, 'Move Left'))
        else:
            sucessors.append(VacuumWorld3Room('center', self.isLeftRoomClean, self.isRightRoomClean,self.isCenterRoomClean, 'Move Right'))
            sucessors.append(VacuumWorld3Room('left', self.isLeftRoomClean, self.isRightRoomClean,self.isCenterRoomClean, 'Move Left'))

        #Implementar ações de limpeza. Importante: Verificar qual a VacuumPos e se a posição está suja
        #Como designar sucessors condicionais?
        if (self.vacuumPosition == 'right'):
            sucessors.append(VacuumWorld3Room(self.vacuumPosition, self.isLeftRoomClean, True, self.isCenterRoomClean, 'clean'))
        if (self.vacuumPosition == 'center'):
            sucessors.append(VacuumWorld3Room(self.vacuumPosition, self.isLeftRoomClean, self.isRightRoomClean, True, 'clean'))
        else:
            sucessors.append(VacuumWorld3Room(self.vacuumPosition, True, self.isRightRoomClean, self.isCenterRoomClean, 'clean'))

        return sucessors
    
    def is_goal(self):
        return (self.isLeftRoomClean and self.isRightRoomClean and self.isCenterRoomClean and (self.vacuumPosition == 'left'))

    
    def description(self):
        return "Problema do aspirador de pó, contendo três (3) salas"
    
    def cost(self):
        return 1

    def print(self):
        return str(self.operator)

def main():
    
    #
    # Executando busca em largura
    #
    state = VacuumWorld3Room('left', False, False, False, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')
    
    #
    # Executando busca em profundidade
    #
    state = VacuumWorld3Room('left', False, False, False, '')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, 10)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

            #
    # Executando BPI
    #
    state = VacuumWorld3Room('left', False, False, False, '')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()
