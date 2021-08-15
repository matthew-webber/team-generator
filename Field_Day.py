import random as r

with open('Players.txt') as f:
	players = f.readlines()

all_players = [name.strip() for name in players]
inactive = [name for name in all_players if name[0].lower() == 'x']
active = list(set(all_players) - set(inactive))

if len(active) % 2 != 0:
	print('******WARNING*******\nOdd number of players!\n**************')

loop = True

while loop:

	r.shuffle(active)

	team_size = 'Team size?\n'
	team_size = input(team_size)

	with open('TeamNames.txt') as f:
		team_names = f.readlines()
		team_names = [team.strip() for team in team_names]

	def get_big_team(**kwargs):
		teamA = kwargs['team']
		teamB = list()

		while len(teamA) > len(teamB):
			teamB.append(teamA.pop())

		return teamA, teamB

	def get_small_teams(**kwargs):

		team = kwargs['team']
		return team[:2], team[2:]
		
	if team_size.lower().strip() == 's':
		teams = get_big_team(team=active)
	elif team_size.lower().strip() == '2':
		 teams = []
		 while len(active) != 0:
		 	x, active = get_small_teams(team=active)
		 	teams.append(x)


	for i, team in enumerate(teams): 
		print(f'Team {r.choice(team_names)} -- {list(team)}')

	loop = input('To go again just hit enter, anything else to quit\n')

	if loop.strip().lower() != '':
		loop = False





