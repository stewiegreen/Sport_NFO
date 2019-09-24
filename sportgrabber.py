import json, requests, sys, pprint, os

class LeagueInfo:
    def __init__(self, league):
        self.league = league

    def get_league_id(self):
        i = 0
        url = "https://www.thesportsdb.com/api/v1/json/1/all_leagues.php"
        response = requests.get(url)
        response.raise_for_status()
        lookup = json.loads(response.text)
        lstr = lookup['leagues']
        for i in range(len(lstr)):
            if (lstr[i]['strLeague'].lower()) == self.league.lower():
                return (lstr[i]['idLeague'])
            else:
                continue

class TeamInfo():
    def __init__(self, league, team):
        self.league = league
        self.team = team
    
    def get_team_id(self):
        usr_input = ''
        get_team = []
        i = 0
        url = "https://www.thesportsdb.com/api/v1/json/1/search_all_teams.php?l=" + self.league
        response = requests.get(url)
        response.raise_for_status()
        lookup = json.loads(response.text)
        teams = lookup['teams']
        
        for team in teams:
            if self.team.lower() in (team['strTeam'].lower()):
                get_team.append(team['strTeam'])
   
        if len(get_team) == 1: #if only one team is found return the ID # of that team
            return (team['idTeam'])
            
        if len(get_team) < 1: #if no matches are found, give an error
            return ("No Matches Found")
              
#if more than 1 match is found list the matches and ask the user to choose one
        print("More than one match, please choose a team:" + "\n")
        for i in range(len(get_team)):
            print(str(i) + ". " + get_team[i] + "\n")
            
        usr_input = input("Select a number:")
        # using that choice, search for the team again 
        for team in teams:
            if get_team[int(usr_input)].lower() in (team['strTeam'].lower()):
                return team['idTeam']        

    def get_last_game(self, teamid):
        url = "https://www.thesportsdb.com/api/v1/json/1/eventslast.php?id=" + str(teamid)
        response = requests.get(url)
        response.raise_for_status()
        lookup = json.loads(response.text)
        last_game = lookup['results']
        return last_game
    
    def date_played(self, date):
        url = "https://www.thesportsdb.com/api/v1/json/1/eventsday.php?d=" + str(date)
        response = requests.get(url)
        response.raise_for_status()
        lookup = json.loads(response.text)
        events = lookup['events']
        for i in range(len(events)):
            if (events[i]['strHomeTeam']) == self.team:
                return (events[i])
            
            if (events[i]['strAwayTeam']) == self.team:
                return (events[i])
            else:
                continue
