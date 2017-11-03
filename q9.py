# Социологический опрос на тему:"Социальные сети"
# 9.	Что Вас привлекает в социальных сетях?

import matplotlib.pyplot as plt

labels = 'Общение с друзьями/родственниками', 'Прослушивание музыки', 'Просмотр видеозаписей', 'Играю в приложения'
sizes = [3,2,2,0]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
ax.axis('equal')

plt.show()