def sort_scores(players):  
  score = sorted(players, key = lambda player: (-player[1], player[0]))
  return score
