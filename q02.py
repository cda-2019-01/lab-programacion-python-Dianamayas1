##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##
### Punto 2
BD = open('data.csv', 'r').readlines()
BD = [row[0:-1] for row in BD]
BD = [row.split('\t') for row in BD]
data = BD

result = {}

for elemt in data:
	result[elemt[0]] = 0

for element in data:
	result[elemt[0]] = result[elemt[0]] + 1

for key in sorted(result.keys()):  
     print(key + ',' + str(result[key]))