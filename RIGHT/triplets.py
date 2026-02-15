alice_score=list(map(int,input().split()))
bob_score=list(map(int,input().split()))
alice=0
bob=0
for n in range(len(alice_score)):
 if alice_score[n] > bob_score[n] :
  alice=alice+1
 elif alice_score[n]<bob_score[n]:
  bob=bob+1
 else:
  break
print(alice,bob)