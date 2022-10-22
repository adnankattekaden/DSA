HOME_TEAM_WON = 1

def tournamentWinner(competions,results):
    currentBestTeam = ""
    scores = {currentBestTeam:0}

    for idx,competion in enumerate(competions):
        result = results[idx]
        homeTeam,awayTeam = competion

        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

        updateScores(winningTeam,3,scores)

        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam

    print(currentBestTeam)
    return currentBestTeam


def updateScores(team,points,scores):
    if team not in scores:
        scores[team] = 0

    scores[team] += points
    
if __name__ == '__main__':
    competions = [["HTML", "C#"],
                               ["C#", "Python"], 
                               ["Python", "HTML"]]

    results = [0,1,1]

    tournamentWinner(competions,results)