# Социологический опрос на тему:"Социальные сети"
# 6.	Со сколькими из друзей вы знакомы лично?

import matplotlib.pyplot as plt

labels = 'до 50', '51-100', '101-200', '201-500', 'Больше 500'
sizes = [4,2,1,0,0]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
ax.axis('equal')

plt.show()