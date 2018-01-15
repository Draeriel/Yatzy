from yatzy import *

if __name__ == "__main__":
	assert (Yatzy.chance(1,1,1,1,1) == 5), "Metodo chance"
	assert(Yatzy.chance(1,2,3,4,5) == 15), "Metodo chance"
	assert(Yatzy.chance(2,2,3,3,4) == 14), "Metodo chance"


	assert(Yatzy.yatzy(1,1,1,1,1)==50), "Método Yatzy"  
	assert(Yatzy.yatzy(1,2,1,1,1)==0), "Método Yatzy"

	assert(Yatzy.ones(1,1,1,1,1)==5), "Método ones" 
	assert(Yatzy.ones(2,3,4,5,6)==0), "Método ones"


	assert(Yatzy.twos(1,1,2,2,2)==6), "Método twos" 
	assert(Yatzy.twos(2,3,4,5,6)==2), "Método twos"

	assert(Yatzy.threes(3,3,3,1,1)==9), "Método threes" 
	assert(Yatzy.threes(2,3,4,5,6)==3), "Método threes"

	dado = Yatzy(1,2,3,4,5)
	assert dado.fours() == 4, "Método fours"
	dado = Yatzy(4,4,4,4,4)
	assert dado.fours() == 20, "Método fours"

	dado = Yatzy(1,2,3,4,5)
	assert dado.fives() == 5, "Método fives"
	dado = Yatzy(5,5,5,3,5)
	assert dado.fives() == 20, "Método fives"

	assert Yatzy.score_pair(1,2,2,3,3) == 6, "Método score_pair"
	assert Yatzy.score_pair(1,1,1,1,2) == 2, "Método score_pair"
	assert Yatzy.score_pair(1,1,6,6,6) == 12, "Método score_pair"
	assert Yatzy.score_pair(1,2,3,4,5) == 0, "Método score_pair"

	assert Yatzy.two_pair(4,5,5,4,4) == 18, "Método two_pair"
	assert Yatzy.two_pair(6,6,6,6,6) == 0, "Método two_pair"
	assert Yatzy.two_pair(3,2,1,3,4) == 0, "Método two_pair"

	assert Yatzy.three_of_a_kind(1,5,1,6,6) == 0, "Método three_of_a_kind"
	assert Yatzy.three_of_a_kind(1,2,6,2,2) == 6, "Método three_of_a_kind"


	assert Yatzy.four_of_a_kind(1,1,1,2,2) == 0, "Método four_of_a_kind"
	assert Yatzy.four_of_a_kind(1,2,2,2,2) == 8, "Método four_of_a_kind"


	assert Yatzy.smallStraight(1,2,3,4,5) == 15, "Método smallStraight"  
	assert Yatzy.smallStraight(2,4,5,3,1) == 15, "Método smallStraight"
	assert Yatzy.smallStraight(5,2,3,4,6) == 0, "Método smallStraight"


	assert Yatzy.largeStraight(2,4,5,3,1) == 0, "Método largeStraight"
	assert Yatzy.largeStraight(5,2,3,4,6) == 20, "Método largeStraight"


	assert Yatzy.fullHouse(4,5,5,4,4) == 22, "Método fullHouse"
	assert Yatzy.fullHouse(1,2,3,1,2) == 0, "Método fullHouse"


	






