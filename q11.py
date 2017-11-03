# Социологический опрос на тему:"Социальные сети"
# 11.	Вы считаете себя зависимым от социальных сетей?

import matplotlib.pyplot as plt

labels = 'Да', 'Нет', 'Немного'
sizes = [2,4,1]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
ax.axis('equal')

plt.show()