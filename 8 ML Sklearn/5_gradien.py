# gradient = slope/kemiringan garis
# y = mx + b

import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])

def gradien(x,y):
    m_curr = b_curr = 0
    iterasi = 1000
    n = len(x)
    learning_rate = 0.001
    for i in range(iterasi):
        y_predicted = m_curr * x + b_curr

        md = -(2/n)*sum(x*(y - y_predicted))
        bd = -(2/n)*sum(y - y_predicted)

        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print('m {}, b {}, iterasi {}'.format(m_curr, b_curr, i))

gradien(x,y)