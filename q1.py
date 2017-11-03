# Социологический опрос на тему:"Социальные сети"
# 1.	Ваш пол?

import matplotlib.pyplot as plt

labels = 'Мужской пол', 'Женский пол'
sizes = [2,5]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
ax.axis('equal')

plt.show()