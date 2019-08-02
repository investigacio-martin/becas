import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statistics as stats
from statistics import mean
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

lista_sucia = []
data = pd.read_excel (r'BasedeDatos.xlsx')
df = pd.DataFrame(data, columns= ['EDAD'])
  
mylist = df.values.tolist()

for i in range (0, 30):
  lista_sucia.append(mylist[i][0])

anos15 = lista_sucia.count(15)
anos16 = lista_sucia.count(16)
anos17 = lista_sucia.count(17)
anos18 = lista_sucia.count(18)
anos19 = lista_sucia.count(19)
anos20 = lista_sucia.count(20)

# print(lista_sucia)

labels = '15 años', '16  años', '20 años', '17 años', '18 años'
sizes = [anos15, anos16, anos20, anos17, anos18]
explode = (0, 0, 0, 0.1, 0)  
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')
plt.style.use('seaborn')

media = str(round(mean(lista_sucia)))
moda = str(round(stats.mode(lista_sucia)))
desviacion = str(stats.stdev(lista_sucia))

pdf.set_font("Arial", size=30)
pdf.cell(200, 10, "Datos edad", ln=1, align="C")
pdf.set_font("Arial", size=18)
pdf.cell(200, 10, "La media es: " + media, ln=3, align="C")
pdf.cell(200, 10, "La moda es: " + moda, ln=5, align="C")
pdf.cell(200, 10, "La desviacion estandar es: " + desviacion, ln=7, align="C")
pdf.output("pdf/dato-edad.pdf")

plt.show()