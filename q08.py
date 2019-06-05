##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras (ordenadas) de la primera 
## columna que aparecen asociadas a dicho valor de la segunda 
## columna. Esto es:
##
## ('0', ['C'])
## ('1', ['A', 'A', 'B', 'D', 'E', 'E'])
## ('2', ['A', 'D', 'E'])
## ('3', ['A', 'B', 'D', 'E', 'E'])
## ('4', ['B', 'E'])
## ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E'])
## ('6', ['A', 'B', 'C', 'E'])
## ('7', ['A', 'C', 'D', 'E'])
## ('8', ['A', 'B', 'E', 'E'])
## ('9', ['A', 'B', 'C', 'E'])
##
##### Punto 8
BD = open('data.csv', 'r').readlines()
BD = [row[0:-1] for row in BD]
BD = [row.split('\t') for row in BD]
data = BD

result = {}

for elemt in data:
	result[elemt[1]] = []

for elemt in data:
	result[elemt[1]].append(elemt[0])

result2 = {}

for i in sorted(result.items()):
	result2[i[0]] = sorted(i[1])

for i in sorted(result2.items()):
	print(i)
