x=0
y=0
fruta = str(input("digite uma expressão: "))

for c in fruta:
  if c == "(":
    x+=1
for c in fruta:
  if c == ")":
    y+=1

print()
if x == y:
  print("As expressoes são validas!")
else:
  print("As expressoes não são validas!")