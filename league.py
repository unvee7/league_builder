import random
import csv

teams = {'Dragons': [], 'Raptors': [], 'Sharks': []}
exp_players = []
non_exp_players = []
all_players = []


# separates the experienced players from the not-experienced players and puts them into seprate lists
def sort_players(all_players):
    for player in all_players:
        if player['Soccer Experience'] == 'YES':
            exp_players.append(player)
        else:
            non_exp_players.append(player)

#removes players from exp or not_exp list and returns that player to get appended to mater list
def get_player(exp_group):
    for player in exp_group:
        exp_group.remove(player)
        return player

# This feels sloppy but I cant figure out how else to do it?
# anywho..  assigns players a team name key and value and appends them back to master list of all players.
def assign_teams():
    while len(exp_players) != 0 and len(non_exp_players) != 0:
        for team in teams.keys():
            player = get_player(exp_players)
            player['Team'] = team
            all_players.append(player)
            player = get_player(non_exp_players)
            player['Team'] = team
            all_players.append(player)
    return all_players

# checks if the team name assigned to each player matches the dict key. If so the player is added to the teams list
def create_team_lists():
    for key, value in teams.items():
        for player in all_players:
            if player['Team'] == key:
                value.append('{}, {}, {}'.format(player['Name'], player['Soccer Experience'], player['Guardian Name(s)']))

# Creates welcome letter for each player
def welcome_letter():
    for player in all_players:
        name = str(player['Name']).replace(' ', '_').lower()
        with open(name + '.txt', 'a') as textfile:
            textfile.write('Dear {}, we are happy to report that {} has made the {} team.'.format(player['Guardian Name(s)'], player['Name'], player['Team']))

# prints name of teams followed by all players associated
def create_doc():
    with open('teams.txt', 'a') as textfile:
        for keys, values in teams.items():
            textfile.write(keys + '\n')
            for player in values:
                textfile.write(str(player) + '\n')
            textfile.write('\n')


# creates list of players from CSV and sorts them by EXP and assigns them a team key and value based on EXP
def initiate():
    with open('soccer_players.csv') as csvfile:
        league_reader = csv.DictReader(csvfile)
        all_players = list(league_reader)
        sort_players(all_players)
        all_players = assign_teams()
        create_team_lists()
        create_doc()
        welcome_letter()


if __name__ == "__main__":
    initiate()
