import matplotlib.pyplot as plt
import matplotlib.style as stl
stl.use('ggplot')
x1 = [5,8,10]
y1 = [12,6,6]

x2 = [6,9,11]
y2 = [6,15,7]

plt.bar(x1,y1)
plt.bar(x2,y2, color = 'g')

plt.title("Epic Info")
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.show()