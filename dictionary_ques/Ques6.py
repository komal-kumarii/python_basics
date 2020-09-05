dic={
    "ball":"red",
    "bat":4,
    "wickets":8,
    "ball":"green",
    "bat":3
}
d={}
for i in dic:
	if i not in d:
		d.update(dic)
print(d)