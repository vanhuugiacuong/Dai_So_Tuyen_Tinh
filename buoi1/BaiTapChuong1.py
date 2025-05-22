from sympy import Symbol, solve

x = Symbol('x')
bieuthuc = x + 3 - 5
print(solve(bieuthuc))
# Kết quả: [2]

bieuthuc = x**2 + 3 - 5
nghiemx = solve(bieuthuc)
print(nghiemx)
# Kết quả: [-sqrt(2), sqrt(2)]

print(nghiemx[0])
# Kết quả: -sqrt(2)

print(nghiemx[1])
# Kết quả: sqrt(2)

from sympy import Symbol, solve

x = Symbol('x')

# Phương trình bậc 2: x**2 + 9*x + 8 = 0
ptb2 = x**2 + 9*x + 8
print(solve(ptb2, dict=True))
# Kết quả: [{x: -1}, {x: -8}]

# Phương trình có nghiệm phức: x**2 + x + 10 = 0
ptb2 = x**2 + 1*x + 10
nghiemx = solve(ptb2, dict=True)
print(nghiemx)
# Kết quả: [{x: -1/2 - (19**0.5)*I/2}, {x: -1/2 + (19**0.5)*I/2}]

from sympy import Symbol, solve

x = Symbol('x')
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')

ptb2 = a*x*x + b*x + c
nghiem = solve(ptb2, x, dict=True)
print(nghiem)
# Kết quả:
# [
#   {x: (-b - (b**2 - 4*a*c)**0.5)/(2*a)},
#   {x: (-b + (b**2 - 4*a*c)**0.5)/(2*a)}
# ]

from sympy import Symbol, solve

x = Symbol('x')
y = Symbol('y')
pt1 = 2*x + 3*y - 12
pt2 = 3*x - 2*y - 5

# Giải hệ phương trình
nghiem = solve((pt1, pt2), dict=True)
print(nghiem)
# Kết quả: [{x: 3, y: 2}]

# Thử lại bộ nghiệm trên
nghiem = nghiem[0]
print(pt1.subs({x: nghiem[x], y: nghiem[y]}))
# Kết quả: 0

print(pt2.subs({x: nghiem[x], y: nghiem[y]}))
# Kết quả: 0

import numpy as np

# Khai báo các lưới nguy cơ
A = np.array([[1, 1, 0, 0, 1],
              [3, 2, 1, 1, 2],
              [5, 0, 2, 1, 0],
              [2, 1, 1, 0, 1],
              [0, 2, 1, 2, 1]])

B = np.array([[1, 2, 2, 1, 1],
              [2, 1, 2, 2, 2],
              [1, 1, 1, 2, 1],
              [2, 2, 1, 1, 2],
              [1, 1, 2, 2, 1]])

C = np.array([[2, 0, 0, 1, 1],
              [1, 1, 1, 0, 1],
              [0, 1, 1, 1, 0],
              [1, 0, 1, 1, 1],
              [1, 1, 0, 0, 1]])

D = np.array([[3, 1, 1, 0, 1],
              [1, 2, 2, 1, 1],
              [2, 1, 1, 1, 2],
              [1, 1, 2, 2, 1],
              [0, 1, 1, 1, 0]])

E = np.array([[0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]])

# Hàm kiểm tra vị trí an toàn (tổng nguy cơ <= 5)
def vi_tri_an_toan(*args):
    return np.where(sum(args) <= 5, 1, 0)

# a. An toàn chiến dịch ngắn hạn 1-2 ngày (tránh lũ quét, lộ bí mật)
an_toan_a = (A + C + D <= 5) & (B <= 0) & (E <= 0)
print("a. Vị trí an toàn chiến dịch ngắn hạn 1-2 ngày (1: an toàn, 0: không):")
print(an_toan_a.astype(int))

# b. An toàn tập luyện thời bình (không cần tránh lộ bí mật và bệnh dịch)
an_toan_b = (A + B + C <= 5)
print("\nb. Vị trí an toàn tập luyện thời bình:")
print(an_toan_b.astype(int))

# c. An toàn mùa khô (không có lũ, không sạt núi, nhưng có cháy rừng và bệnh dịch)
an_toan_c = (A + D <= 5)
print("\nc. Vị trí an toàn mùa khô:")
print(an_toan_c.astype(int))

# d. An toàn mùa mưa (có lũ, có lộ bí mật, có bệnh dịch mà không có cháy rừng)
an_toan_d = (B + C + D + E <= 5)
print("\nd. Vị trí an toàn mùa mưa:")
print(an_toan_d.astype(int))

# e. An toàn trong 8 tháng (có đủ các mùa và có yếu tố tránh lộ bí mật)
an_toan_e = (A + B + C + D + E <= 5)
print("\ne. Vị trí an toàn trong 8 tháng:")
print(an_toan_e.astype(int))