import json, requests, sys, os, re

class Date():
    def __init__(self, date):
        self.date = date
    
    def date_checker(self):
        dateregex = re.compile(r'\d\d\d\d-\d\d-\d\d')
        if dateregex.search(self.date):
            return True
        else:
            return False

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
                while True:
                    try:
                        usr_input = int(input("Select a number:"))
                        if int(usr_input) > int(y):
                            continue
                        else:
                            break
                    except:
                        print("Not a valid option")
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
        usr_input = ''
        get_team = []
        i = 0
        url = "https://www.thesportsdb.com/api/v1/json/1/search_all_teams.php?l=" + league
        response = requests.get(url)
        response.raise_for_status()
        lookup = json.loads(response.text)
        teams = lookup['teams']
     
        input_team = input("Which team? ")
        for i in range(len(teams)):
            if input_team.lower() == (teams[i]['strTeamShort'].lower()):
                return teams[i]['idTeam']
            else:
                continue                  
        while not get_team:
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
                
                while True:
                    try:
                        usr_input = int(input("Select a number:"))
                        if int(usr_input) > int(y):
                            continue
                        else:
                            break
                    except:
                        print("Not a valid option")    
                
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
        event = lookup['results'][0]['idEvent']
        newurl = "https://www.thesportsdb.com/api/v1/json/1/lookupevent.php?id=" + str(event)
        response = requests.get(newurl)
        response.raise_for_status()
        lookup = json.loads(response.text)
        lastgame = lookup['events'][0]
        return lastgame
    
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
        if type(gameinfo) == dict: 
            date = gameinfo['dateEvent']
            hometeam = gameinfo['strHomeTeam']
            awayteam = gameinfo['strAwayTeam']
            eventname = gameinfo['strEvent']
            leaguename = gameinfo['strLeague']
            awayscore = gameinfo['intAwayScore']
            homescore = gameinfo['intHomeScore']
            awayshots = gameinfo['intAwayShots']
            homeshots = gameinfo['intHomeShots']
            filename = gameinfo['strFilename']
            season = gameinfo['strSeason']
            sport = gameinfo['strSport']
            
            
            
        
            path = (os.path.dirname(__file__) + "/" + filename + ".nfo")
            NFO = open(path, 'w')


            NFO.write('<?xml version="1.0" encoding="utf-8" standalone="yes"?>' + "\n")
            NFO.write("<episodedetails>" + "\n")
            NFO.write("  <plot>The " + leaguename + " presents the "  + awayteam + " against the " + hometeam + ".   " + "\n" + " This game was played on " + date + ".   " + "\n" + "</plot>")
            #leaving score option here
            #NFO.write("***Score: " + "\n")
            #NFO.write(awayteam + ": " + awayscore + "\n" + hometeam + ": " + homescore + "\n" + "</plot>")
            NFO.write("<lockdata>false</lockdata>" + "\n")
            NFO.write("<title>" + eventname + "</title>" + "\n")
            NFO.write("<year>" + season + "</year>" + "\n")
            NFO.write("</episodedetails>" + "\n")


            NFO.close()

        else:
            print("Sorry, something has gone wrong")

