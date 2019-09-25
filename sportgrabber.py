import json, requests, sys, pprint, os

class Date():
    def __init__(self, date):
        self.date = date
    
    def date_checker(date):
        separate = date.split('-')
        if len(separate) == 3:
            
            if len(separate[0]) == 4:
            
                if len(separate[1]) == 2:
                
                    if len(separate[2]) == 2:
                        return True
                    
                else: return False
            else: return False
        else: return False


class LeagueInfo():
    def __init__(self):
        self.league = league

    def get_leagues():
        
        url = "https://www.thesportsdb.com/api/v1/json/1/all_leagues.php"
        response = requests.get(url)
        response.raise_for_status()
        lookup = json.loads(response.text)
        leagues = lookup['leagues']
       
        usr_input = ''
        get_league = []
        i = 0
        while not get_league:
            input_league = input("Which League? ") 
            for i in range(len(leagues)):
                if input_league.lower() in (leagues[i]['strLeague'].lower()):
                    get_league.append(leagues[i]['strLeague'])
            
            if len(get_league) == 1: #if only one team is found return the ID # of that team
                for league in leagues:
                    if get_league[0].lower() in (league['strLeague'].lower()):
                        return league['strLeague']

            if len(get_league) > 1:             
    #if more than 1 match is found list the matches and ask the user to choose one
                print("More than one match, please choose a league:" + "\n")
                for y in range(len(get_league)):
                    print(str(y) + ". " + get_league[y] + "\n")
                
                usr_input = input("Select a number:")
            # using that choice, search for the team again 
                for league in leagues:
                    if get_league[int(usr_input)].lower() in (league['strLeague'].lower()):
                        return league['strLeague']

            else:
                print ("No Matches Found")

class TeamInfo():
    def __init__(self, league):
        self.league = league
        
    
    def get_teams(self, league):
        
        url = "https://www.thesportsdb.com/api/v1/json/1/search_all_teams.php?l=" + league
        response = requests.get(url)
        response.raise_for_status()
        lookup = json.loads(response.text)
        teams = lookup['teams']
     

        usr_input = ''
        get_team = []
        i = 0
        while not get_team:
            input_team = input("Which team? ")
            for i in range(len(teams)):
                if input_team.lower() in (teams[i]['strTeam'].lower()):
                    get_team.append(teams[i]['strTeam'])
            
            if len(get_team) == 1: #if only one team is found return the ID # of that team
                for team in teams:
                    if get_team[0].lower() in (team['strTeam'].lower()):
                        return team['idTeam']
            
            if len(get_team) > 1:      
    #if more than 1 match is found list the matches and ask the user to choose one
                print("More than one match, please choose a team:" + "\n")
                for y in range(len(get_team)):
                    print(str(y) + ". " + get_team[y] + "\n")
                
                usr_input = input("Select a number:")
            # using that choice, search for the team again 
                for team in teams:
                    if get_team[int(usr_input)].lower() in (team['strTeam'].lower()):
                        return team['idTeam']
            else:
                print ("No Matches Found")



    def get_last_game(self, teamid):
        url = "https://www.thesportsdb.com/api/v1/json/1/eventslast.php?id=" + str(teamid)
        response = requests.get(url)
        response.raise_for_status()
        lookup = json.loads(response.text)
        last_game = lookup['results']
        return last_game
    
    def date_played(self, date, teamid):
        url = "https://www.thesportsdb.com/api/v1/json/1/eventsday.php?d=" + str(date)
        response = requests.get(url)
        response.raise_for_status()
        lookup = json.loads(response.text)
        events = lookup['events']
        for event in events:
            if (event['idHomeTeam']) == teamid:
                return (event)
            
            if (event['idAwayTeam']) == teamid:
                return (event)
        
        print("Sorry, No Match")
        

    def create_nfo(self, gameinfo, scores = False):
        date = gameinfo['dateEvent']
        hometeam = gameinfo['strHomeTeam']
        awayteam = gameinfo['strAwayTeam']
        eventname = gameinfo['strEvent']
        leaguename = gameinfo['strLeague']
        awayteamscore = gameinfo['intAwayScore']
        hometeamscore = gameinfo['intHomeScore']
        filename = gameinfo['strFilename']
        season = gameinfo['strSeason']
        if type(gameinfo) == dict: 
            path = (os.path.dirname(__file__) + "/" + filename + ".nfo")
            NFO = open(path, 'w')


            NFO.write('<?xml version="1.0" encoding="utf-8" standalone="yes"?>' + "\n")
            NFO.write("<episodedetails>" + "\n")
            NFO.write("  <plot>" + awayteam + " vs. " + hometeam + "</plot>" + "\n")
            NFO.write("<lockdata>false</lockdata>" + "\n")
            NFO.write("<title>" + eventname + "</title>" + "\n")
            NFO.write("<year>" + season + "</year>" + "\n")
            NFO.write("</episodedetails>" + "\n")


            NFO.close()

        else:
            pass
