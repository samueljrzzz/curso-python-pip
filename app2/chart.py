import matplotlib.pyplot as plt


def graficarbar(labels, values, name):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./imgs/{name}Bar.png')
  plt.close()

def graficarpie(labels, values, name):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig(f'./imgs/{name}Pie.png')
  plt.close()