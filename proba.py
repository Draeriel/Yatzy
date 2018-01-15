def two_pair(*dice):
    '''pareja = [numero for numero in dice if dice.count(numero) >= 2]'''
    contador = 0
    recolector = []
    for numero in range(1,7):
    	actual = dice.count(numero)
    	if actual >= 2 and actual not in recolector:
    		recolector.append(numero)	
    if len(recolector) == 2:
    	return sum(recolector)*2
    return 0	


print(two_pair(4,5,5,4,4))
print(two_pair(6,6,6,6,6))



