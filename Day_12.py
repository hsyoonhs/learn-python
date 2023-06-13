import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

# ------------------------------ #

# AND

X = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
Y = np.array([0, 0, 0, 1])

w = np.array([1., 1., 1.]) # [bias, w1, w2]

def forward(x):
    return np.dot(x, w[1:]) + w[0] # 퍼셉트론 수식

def predict(x):
    return np.where(forward(x) > 0, 1, -1) # Step function이며 0보다 크면 1, 아니면 -1

print("bias, w1, w2 (before training)", w)

for epoch in range(50):
    for x_val, y_val in zip(X, Y):
        update = 0.01 * (y_val - predict(x_val)) # 목표 출력과 현재 출력 비교
        w[1:] += update * x_val
        w[0] += update # 가중치와 편향 업데이트

print("bias, w1, w2 (after training)", w)

# ------------------------------ #

# Step function

import matplotlib.pylab as plt

def step_function(x):
    return np.array(x > 0, dtype = np.int)

x = np.arange(-5.0, 5.0, 0.1)
y= step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) # y축의 범위 지정
plt.show()

# ------------------------------ #

# Sigmoid function
    # 비선형 문제 해결
    # 가중치 학습 과정에 미분 활용
    # 데이터 정보 손실 방지

# ------------------------------ #

# 신경망
