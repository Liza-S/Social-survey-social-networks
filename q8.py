# Социологический опрос на тему:"Социальные сети"
# 8.	Откуда Вы в основном заходите в социальные сети?

import matplotlib.pyplot as plt

labels = 'из дома', 'на учебе', 'на улице', 'в кафе баре и тд.'
sizes = [5,1,1,0]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
ax.axis('equal')

plt.show()