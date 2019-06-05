##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##
### Punto 13
BD = open('data.csv', 'r').readlines()
BD = [row[0:-1] for row in BD]
BD = [row.split('\t') for row in BD]
data = []

i = 0
for elemt in BD:
	data.append([])
	for e in elemt:
		a = e.split(',')
		if(len(a) == 1):
			data[i].append(a[0])
		else:
			data[i].append(a)
	i += 1

for element in data:
	aux = 0
	for e in element[4]:
		aux += int(e.split(':')[1])
	print(element[0] + ',' + str(aux))