##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
##
### Punto 12
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

result = {}

for element in data:
	for key in element[3]:
		if key in result:
			result[key] += int(element[1])
		else:
			result[key] = int(element[1])

for key in sorted(result.keys()):
     print(key + ',' + str(result[key]))