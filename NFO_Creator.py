import autosportgrabber as sg


leagues = sg.get_leagues()
input_league = input("Which League? ")
league = sg.find_league(leagues, input_league)
teams = sg.get_teams(league)
input_team = input("Which team? ")
team = sg.find_team(teams, input_team)

while True:
    input_date = input("Which date did the game occur? (yyyy-mm-dd)" + "\n" + "Leave blank for latest game :")

    if input_date == "":
        game_day = sg.get_last_game(team)
        sg.create_nfo(game_day)
        break

    date = sg.Date(input_date)
    datecheck = date.date_checker()

    if not datecheck:
        print("Please enter a valid date format")

    if datecheck:
        print("Thank you, generating file")
        game_day = sg.date_played(input_date, team)
        sg.create_nfo(game_day)
        break


    else:
        print("Sorry, something went wrong.")
