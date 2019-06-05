##
## Imprima la suma de la segunda columna.
##
### Punto 1
BD = open('data.csv', 'r').readlines()
BD = [row[0:-1] for row in BD]
BD = [row.split('\t') for row in BD]
data = BD

suma_col = 0
for i in data:
    suma_col += int(i[1])
print(suma_col)