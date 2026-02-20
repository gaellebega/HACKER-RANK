defaultdict()
result=defaultdict(list)
for s in strs:
  key="".join(sorted(s))
  result[key].append(s)
return list(result.values())