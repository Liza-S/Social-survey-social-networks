# Социологический опрос на тему:"Социальные сети"
# 3.	Что Вас подтолкнуло зарегистрироваться в социальных сетях?

import matplotlib.pyplot as plt

labels = 'Друзья', 'Любопытство', 'Желание завести новых друзей', 'Куда все, туда и я!'
sizes = [2,5,0,0]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
ax.axis('equal')

plt.show()