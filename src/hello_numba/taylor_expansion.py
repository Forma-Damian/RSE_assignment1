
import numpy as np
from numba import njit

@njit
def math_func(x: float):
    return np.sin(x)

@njit
def factorial(n: int):
    if n == 0:
        return 1
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

@njit
def taylor_expansion_sin(x: float, n_terms: int):
    result = 0.0
    for i in range(n_terms):
        sign = (-1) ** i
        term = (x ** (2 * i + 1)) / factorial(2 * i + 1)
        result += sign * term
    return result



# import pint
# from numba import njit
# import random
# from sympy import *
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.interpolate import approximate_taylor_polynomial

# # @njit
# # def monte_carlo_pi(nsamples):
# #     acc = 0
# #     for i in range(nsamples):
# #         x = random.random()
# #         y = random.random()
# #         if (x ** 2 + y ** 2) < 1.0:
# #             acc += 1
# #     return 4.0 * acc / nsamples

# # print(monte_carlo_pi(10_000_000))

# def taylor_expansion(f, x0, max_degree):
#   curves = {}
#   x = np.linspace(-10.0, 10.0, num=100)
#   plt.plot(x, f(x+x0), label="curve")
#   for deg in np.arange(1, max_degree + 1, step=2):
#       curve_taylor = approximate_taylor_polynomial(f, x0, deg, 1,
#                                                 order=deg + 2)
#       curves[deg] = curve_taylor(x)
#       plt.plot(x, curve_taylor(x), label=f"degree={deg}")
#   plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left',
#             borderaxespad=0.0, shadow=True)
#   plt.tight_layout()
#   plt.axis([-10, 10, -10, 10])
#   plt.minorticks_on()
#   plt.grid(which='major', linestyle='-', linewidth=1.0)
#   plt.grid(which='minor', linestyle='--', linewidth=0.5)
#   print(curves)
#   for curve in curves.values():
#       print(curve[49] + curve[50])
#   plt.show()


# @njit
# def math_func(x, f=np.sin):
#     return f(x)

# taylor_expansion(math_func, np.pi, 12)








# # @njit
# # def taylor_expansion(f, x0, degree):
# #     x = symbols('x')
# #     # f = cos(x)
# #     # coeffs = [f(x0)]
# #     # for n in range(1, degree + 1):
# #     #     coeffs.append((f(x0 + 1e-5) - f(x0 - 1e-5)) / (2 * 1e-5) / np.math.factorial(n))
# #     # return coeffs
# #     # Expand around x = π/2
# #     expr = f(x)
# #     s = series(expr , x, x0, n=degree)
# #     print(f"{f} around x = {x0}:")
# #     print(s)




# # taylor_expansion(math_func, 1, 5)

# # # Substitute to verify: cos(π/2) should be ≈ 0
# # print("\nAt x = π/2:", s.removeO().subs(x, pi/2))