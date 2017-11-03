# Социологический опрос на тему:"Социальные сети"
#2.	Ваш возраст:
import matplotlib.pyplot as plt

labels = 'Меньше 17', '17-20', 'Старше 20'

sizes = [0,7,0]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
ax.axis('equal')

plt.show()