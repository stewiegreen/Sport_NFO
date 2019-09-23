import json, requests, sys, pprint

class TeamInfo():
    def __init__(self, league, team):
        self.league = league
        self.team = team

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
    
    
    def get_team_id(self):
        i = 0
        url = "https://www.thesportsdb.com/api/v1/json/1/search_all_teams.php?l=" + self.league
        response = requests.get(url)
        response.raise_for_status()
        lookup = json.loads(response.text)
        teams = lookup['teams']
        for i in range(len(teams)):
            if (teams[i]['strTeam'].lower()) == self.team.lower():
                return (teams[i]['idTeam'])
            else:
                continue


    def get_last_game(self, teamid):
        url = "https://www.thesportsdb.com/api/v1/json/1/eventslast.php?id=" + str(teamid)
        response = requests.get(url)
        response.raise_for_status()
        lookup = json.loads(response.text)
        last_game = lookup['results']
        return last_game

input_league = input("Which League is your team is? ")
input_team = input("Which team's latest game should I find? ")
print("Thank you, I'll look for the lastest " + input_league + " game " + " where the " + input_team + " played." )

TI = TeamInfo(input_league.title(), input_team.title())

teamid = TI.get_team_id()

last_game = TI.get_last_game(teamid)


path = (os.path.dirname(__file__) + "/" + last_game[0]['strFilename'] + ".nfo")
NFO = open(path, 'w')

NFO.write('<?xml version="1.0" encoding="utf-8" standalone="yes"?>' + "\n")
NFO.write("<episodedetails>" + "\n")
NFO.write("  <plot>" + last_game[0]["strAwayTeam"] + " vs. " + last_game[0]["strHomeTeam"] + "\n")
NFO.write("<lockdata>false</lockdata>" + "\n")
NFO.write("<title>" + last_game[0]['strEvent'] + "</title>" + "\n")
NFO.write("<year>" + last_game[0]['strSeason'] + "</year>" + "\n")
NFO.write("</episodedetails>" + "\n")

NFO.close()
