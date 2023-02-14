import time
from aiohttp import BodyPartReader
from lcu_driver import Connector
from time import sleep
import json

connector = Connector()
@connector.ready

async def connect(connection):
    reportedSummonerName = input("Enter the nickname to report: ")
    reportedSummoner = await connection.request('get', "/lol-summoner/v1/summoners?name=" +  reportedSummonerName)
    reportedSummoner = await reportedSummoner.json()
    try:
        reportedSummonerId = reportedSummoner['accountId']
        reportedSummonerPuid = reportedSummoner['puuid']
    except:
        print(reportedSummoner)
        print("Summoner not found")
        exit(0)
    response = await connection.request('get', "/lol-match-history/v1/products/lol/" + reportedSummonerPuid + "/matches")
    response = await response.json()
    gameId = response['games']['games'][1]['gameId']
    while True:
        _report = {
            "comment": "[reported by DeathNote.py]",
            "gameId": gameId,
            "offenses": "Negative Attitude, Verbal Abuse, Intentional Feeding",
            "reportedSummonerId": reportedSummonerId
        }
        response = await connection.request('post', "/lol-end-of-game/v2/player-complaints", data=_report)
        response = await response.json()
        try: 
            if response['httpStatus'] == 403:
                print("failed to report", reportedSummonerName) 
            else:
                print("Player", reportedSummonerName, "is reported.")
        except:
            print("Player", reportedSummonerName, "is reported.")
        waitingTime = 60 * 60 + 1
        i = 0
        while i < waitingTime:
            print("\033c", end="")
            time.sleep(1)
            i += 1
            print("\n\nWaiting 1 hours...: ", i // 60, "min", i % 60, "sec")
            #clear the console
            print("\033c", end="")


connector.start()
