# Социологический опрос на тему:"Социальные сети"
# 4.	Какой социальной сетью вы пользуетесь больше всего? 

import matplotlib.pyplot as plt

labels = 'Вконтакте', 'Facebook', 'Twitter', 'Одноклассники', 'Мой мир (mail.ru)'
sizes = [5,1,1,0,0]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
ax.axis('equal')

plt.show()