class Yatzy:


    def __init__(self, d1, d2, d3, d4, d5):
        self.dice = [0]*5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = d5


    @staticmethod
    def chance(*dice):
        '''Cambiado argumento para facilitar abstracción, cambiamos lógica para acceder al nuevo tipo de argumentos.'''
        score = 0
        for die in dice:
            score += die
        return score

    @staticmethod
    def yatzy(*dice):
        '''Hemos cambiado la lógica del programa cambiando el argumento counts para que ser más legible'''
        firstDie = dice[0]
        for die in dice:
            if die == firstDie:
                pass
            else:
                return 0
        return 50
    
    @staticmethod
    def ones(*dice):
        '''simplificancón del código'''

        resultado = sum([uno for uno in dice if uno == 1])
        return resultado
    

    @staticmethod
    def twos(*dice):
        '''simplificancón del código'''

        resultado = sum([dos for dos in dice if dos == 2])
        return resultado

    @staticmethod
    def threes(*dice):
        '''simplificancón del código'''

        resultado = sum([tres for tres in dice if tres == 3])
        return resultado
    
    
    def fours(self):

        resultado = sum([cuatro for cuatro in self.dice if cuatro == 4])
        return resultado

    

    def fives(self):
        resultado = sum([cinco for cinco in self.dice if cinco == 5])
        return resultado

    def sixes(self):
        sum = 0
        for at in range(len(self.dice)): 
            if (self.dice[at] == 6):
                sum = sum + 6
        return sum
    
    @staticmethod
    def score_pair(*dice):
        pareja = [numero for numero in dice if dice.count(numero) >= 2]
        if pareja:
            return max(pareja)*2
        return 0    
    
    @staticmethod
    def two_pair(*dice):
        recolector = []
        for numero in range(1,7):
            actual = dice.count(numero)
            if actual >= 2 and actual not in recolector:
                recolector.append(numero)   
        if len(recolector) == 2:
            return sum(recolector)*2
        return 0


    @staticmethod
    def three_of_a_kind(*dice):
        trio = [numero for numero in dice if dice.count(numero) >= 3]
        if trio:
            return max(trio)*3
        return 0 


    @staticmethod
    def four_of_a_kind(*dice):
        cuarteto = [numero for numero in dice if dice.count(numero) >= 4]
        if cuarteto:
            return max(cuarteto)*4
        return 0
    

    @staticmethod
    def smallStraight(*dice):
        for numero in range(1,6):
            if numero not in dice:
                return 0
        return sum(dice)
    

    @staticmethod
    def largeStraight(*dice):
        for numero in range(2,7):
            if numero not in dice:
                return 0
        return sum(dice)
    

    @staticmethod
    def fullHouse(*dice):
        trio = [numero for numero in dice if dice.count(numero) == 3]
        pareja = [numero for numero in dice if dice.count(numero) == 2]
        if trio and pareja:
            return sum(dice)
        return 0