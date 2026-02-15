players = [['Alice', 50], ['Bob', 40], ['Charlie', 50]]
scores=([score for name, score in players])
max_score=max(scores)
winners=[name for name, score in players if score == max_score]
print("Winners(s):",winners)