import random
import csv

teams = 'dragons', 'raptors', 'sharks'
exp_players = []
non_exp_players = []
all_players = []

dragons = []
raptors = []
sharks = []


class Player():
    def __init__(self, exp, team, name, guardians, height):
        self.name = name
        self.height = height
        self.exp = exp
        self.guardians = guardians
        self.team = team


# separates the experienced players from the not-experienced players and puts them into seprate lists
def sort_members(all_players):
    for player in all_players:
        if 'YES' in player.values():
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
        for team in teams:
            player = get_player(exp_players)
            player['team'] = team
            all_players.append(player)
            player = get_player(non_exp_players)
            player['team'] = team
            all_players.append(player)
    return all_players

# Creates welcome letter for the player instance passed in.
def welcome_letter(player_inst):
    name = str(player_inst.name).replace(' ', '_').lower()
    with open(name + '.txt', 'a') as textfile:
        textfile.write('Dear {}, we are happy to report that {} has made the {} team.'.format(player_inst.guardians, player_inst.name, player_inst.team))

# prints name of teams followed by all players associated
def create_doc():
    with open('teams.txt', 'a') as textfile:
        textfile.write('Raptors \n')
        for player in raptors:
            textfile.write(player + '\n')
        textfile.write('\nDragons \n')
        for player in dragons:
            textfile.write(player + '\n')
        textfile.write('\nSharks \n')
        for player in sharks:
            textfile.write(player + '\n')

# sort each player instance into a team based on the teamname assigned to them
def create_team_lists(player_inst):
    if player_inst.team == 'dragons':
        dragons.append('{}, {}, {}'.format(player_inst.name, player_inst.exp, player_inst.guardians))
    if player_inst.team == 'raptors':
        raptors.append('{}, {}, {}'.format(player_inst.name, player_inst.exp, player_inst.guardians))
    if player_inst.team == 'sharks':
        sharks.append('{}, {}, {}'.format(player_inst.name, player_inst.exp, player_inst.guardians))

# creates list of players from CSV and sorts them by EXP and assigns them a team key and value based on EXP
# then creates instances of each player and puts each into a list based on the teamname
def initiate():
    with open('soccer_players.csv') as csvfile:
        league_reader = csv.DictReader(csvfile)
        player_list = list(league_reader)
        sort_members(player_list)
        all_players = assign_teams()
    for player in all_players:
        player_inst = Player(*player.values())
        welcome_letter(player_inst)
        create_team_lists(player_inst)
    create_doc()


if __name__ == "__main__":
    initiate()
