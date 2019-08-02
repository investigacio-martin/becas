import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statistics as stats
from statistics import mean
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

lista_sucia = []
lista_limpia = []

data = pd.read_excel (r'BasedeDatos.xlsx')
df = pd.DataFrame(data, columns= ['SEXO'])
  
mylist = df.values.tolist()

for i in range (0, 30):
  lista_sucia.append(mylist[i][0])

masc = lista_sucia.count('M')
fem = lista_sucia.count('F')

labels = 'Maculino', 'Femenino'
sizes = [masc, fem]
explode = (0, 0.1)  
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')
plt.style.use('seaborn')

for i in range(0, len(lista_sucia)):
  if lista_sucia[i] == 'M':
    lista_limpia.append(1)
  elif lista_sucia[i] == 'F':
    lista_limpia.append(0)

media = str(round(mean(lista_limpia)))
moda = str(round(stats.mode(lista_limpia)))
desviacion = str(stats.stdev(lista_limpia))
    

pdf.set_font("Arial", size=30)
pdf.cell(200, 10, "Datos edad", ln=1, align="C")
pdf.set_font("Arial", size=18)
pdf.cell(200, 10, "La media es: " + 'Mujeres', ln=3, align="C")
pdf.cell(200, 10, "La moda es: " + 'Mujeres', ln=5, align="C")
pdf.output("pdf/dato-sexo.pdf")

plt.show()