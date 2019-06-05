##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##
### Punto 3
BD = open('data.csv', 'r').readlines()
BD = [row[0:-1] for row in BD]
BD = [row.split('\t') for row in BD]
data = BD
result = {}

for elemt in data:
	result[elemt[0]] = 0

for elemt in data:
	result[elemt[0]] = result[elemt[0]] + int(elemt[1])

for key in sorted(result.keys()):  
     print(key + ',' + str(result[key]))