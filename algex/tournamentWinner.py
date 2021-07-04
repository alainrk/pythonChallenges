def tournamentWinner(competitions, results):
	first, maxPoints = None, 0
	teams = {}
	for i in range(len(competitions)):
		winner = competitions[i][1 - results[i]]
		if not winner in teams:
			teams[winner] = 0
		teams[winner] += 3
		if maxPoints < teams[winner]:
			first, maxPoints = winner, teams[winner]
	return first