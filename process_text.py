teams = ['nyjets', 'CHIBears', 'cowboys', 'Texans', 'panthers', 'Patriots',
       'LosAngelesRams', 'DenverBroncos', 'steelers', 'Browns',
       'buffalobills', 'miamidolphins', 'GreenBayPackers', 'Seahawks',
       'eagles', 'ravens', 'falcons', 'Tennesseetitans',
       'KansasCityChiefs', '49ers', 'NYGiants', 'bengals', 'detroitlions',
       'minnesotavikings', 'Chargers', 'Jaguars', 'Colts', 'Redskins',
       'oaklandraiders', 'Saints', 'buccaneers', 'AZCardinals',"highest",
       "high"]
def convert_name(team_name):
    try:
        for team in teams:
            team_upper = team.upper()
            team_check_upper = team_name.upper()
            if team_check_upper in team_upper:
                return team
            
    except Exception:
        return "Invalid Team Name try removing the city name"
        
