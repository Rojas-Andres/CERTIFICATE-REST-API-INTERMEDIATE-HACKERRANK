#!/bin/python3

import math
import os
import random
import re
import sys


import requests
#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#
def obtener_paginas(year,team,team_gol):
    url_1 = f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&{team_gol}={team}'
    local = requests.get(url_1)
    return local.json()["total_pages"]

def obtener_goles(year,team,pagina,team_gol):
    url_1 = f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&{team_gol}={team}&page={pagina}'
    local = requests.get(url_1)
    tm = f"{team_gol}goals"
    goles = 0
    for i in local.json()["data"]:
        goles +=int(i[tm]) 
    return goles
def getTotalGoals(team, year):
    # Write your code here
        
    total = obtener_paginas(year,team,"team1")
    # total = 1
    if total==1:
        goles1 = obtener_goles(year,team,total,"team1")
        print(goles1)
    else:
        goles1 = 0
        for i in range(1,total+1):
            goles1+=obtener_goles(year,team,i,"team1")
    total = obtener_paginas(year,team,"team2")
    if total==1:
        goles2 = obtener_goles(year,team,total,"team2")
    else:
        goles2 = 0
        for i in range(1,total+1):
            goles2+=obtener_goles(year,team,i,"team2")
    return goles1+goles2

#Prueba manual de aca para abajo

result = getTotalGoals("Chelsea", 2014)
print(result)
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     team = input()

#     year = int(input().strip())

#     result = getTotalGoals(team, year)

#     fptr.write(str(result) + '\n')

#     fptr.close()
