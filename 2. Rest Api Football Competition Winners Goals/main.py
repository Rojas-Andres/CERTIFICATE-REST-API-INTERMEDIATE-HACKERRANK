''' 
https://jsonmock.hackerrank.com/api/football_competitions?name=<name>&year=<year>

https://jsonmock.hackerrank.com/api/football_competitions?name=UEFA Champions League&year=2011
'''
import requests 

def obtener_paginas(year,team,team_gol):
    url_1 = f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&{team_gol}={team}'
    local = requests.get(url_1)
    return local.json()["total_pages"]

def obtener_goles(year,team,pagina,team_gol,competition):
    url_1 = f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&{team_gol}={team}&page={pagina}'
    local = requests.get(url_1)
    tm = f"{team_gol}goals"
    goles = 0
    for i in local.json()["data"]:
        if i["competition"] == competition:
            goles +=int(i[tm]) 
    return goles

def getWinnerAndPage(competicion,year):
    url = f"https://jsonmock.hackerrank.com/api/football_competitions?name={competicion}&year={year}"
    r = requests.get(url)
    ganador = r.json()["data"][0]["winner"]
    return ganador

def getWinnerTotalGoals(competition, year):
    # Write your code here
    team = getWinnerAndPage(competition,year)
    total = obtener_paginas(year,team,"team1")

    if total==1:
        goles1 = obtener_goles(year,team,total,"team1",competition)

    else:
        goles1 = 0
        for i in range(1,total+1):
            goles1+=obtener_goles(year,team,i,"team1",competition)
    total = obtener_paginas(year,team,"team2")
    if total==1:
        goles2 = obtener_goles(year,team,total,"team2",competition)
    else:
        goles2 = 0
        for i in range(1,total+1):
            goles2+=obtener_goles(year,team,i,"team2",competition)
    return goles1+goles2

#Prueba manual de aca para abajo
result = getWinnerTotalGoals('UEFA Champions League',2011)
print(result)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     competition = input()

#     year = int(input().strip())

#     result = getWinnerTotalGoals(competition, year)

#     fptr.write(str(result) + '\n')

#     fptr.close()