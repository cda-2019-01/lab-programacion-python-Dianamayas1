##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##
### Punto 5
BD = open('data.csv', 'r').readlines()
BD = [row[0:-1] for row in BD]
BD = [row.split('\t') for row in BD]
data = BD
result = {}

for elemt in data:
	result[elemt[0]] = []

for elemt in data:
	result[elemt[0]].append(int(elemt[1]))

for key in sorted(result.keys()):  
     print(key + ',' + str(max(result[key])) + ',' + str(min(result[key])))