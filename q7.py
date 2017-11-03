# Социологический опрос на тему:"Социальные сети"
# 7.	Сколько времени в день Вы проводите в социальных сетях?

import matplotlib.pyplot as plt

labels = '15-20 мин', 'от 20 мин до часа', 'от часа до трех', 'больше трех часов'
sizes = [2,2,3,0]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
ax.axis('equal')

plt.show()