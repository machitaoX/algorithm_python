import numpy as np

if __name__ == '__main__':
    x = [0, 1, 2]
    prob = [0.05, 0.8, 0.15]

    # 计算期望E(X)
    E_X = sum(x_i * p_i for x_i, p_i in zip(x, prob))

    # 计算期望E(X^2)
    E_X_squared = sum((x_i ** 2) * p_i for x_i, p_i in zip(x, prob))

    # 计算方差Var(X)
    Var_X = E_X_squared - E_X ** 2

    print(Var_X)
    print(E_X)
    print(E_X_squared)

