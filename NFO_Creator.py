import sportgrabber as sg


league = sg.LeagueInfo.get_leagues()



TI = sg.TeamInfo(league)

team = TI.get_teams(league)


while True:
    input_date = input("Which date did the game occur? (yyyy-mm-dd)" + "\n" + "Leave blank for latest game :")

    if input_date == "":
        game_day = TI.get_last_game(team)
        TI.create_nfo(game_day)
        break
    
    date = sg.Date(input_date)
    datecheck = date.date_checker()

    if not datecheck:
        print("Please enter a valid date format")
    
    if datecheck:
        print("Thank you, generating file")
        game_day = TI.date_played(input_date, team)
        TI.create_nfo(game_day)
        break

    
    else:
        print("Sorry, something went wrong.")
