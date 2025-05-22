import numpy as np

vec1 = np.array([1., 3., 5.])
print(vec1 * 2)
# Kết quả: [ 2.  6. 10.]

print(vec1 * vec1)
# Kết quả: [ 1.  9. 25.]  # Phép nhân từng phần tử (element-wise)

print(vec1 / 2)
# Kết quả: [0.5 1.5 2.5]

print(vec1 + vec1)
# Kết quả: [ 2.  6. 10.]

vec2 = np.array([2., 4.])
# print(vec1 + vec2)  # Lỗi: shapes (3,) and (2,) not aligned

vec3 = np.array([2., 4., 6.])
print(vec1 + vec3)
# Kết quả: [ 3.  7. 11.]

print(vec1 / vec3)
# Kết quả: [0.5 0.75 0.83333333]

print(vec1 * vec3)
# Kết quả: [ 2. 12. 30.]

print(2 * vec1 + 5 * vec3)
# Kết quả: [12. 26. 40.]

print(vec3[2])
# Kết quả: 6.0

vec4 = np.linspace(0, 20, 5)
print(vec4)
# Kết quả: [ 0.  5. 10. 15. 20.]

vec5 = np.zeros(5)
print(vec5)
# Kết quả: [0. 0. 0. 0. 0.]

vec6 = np.ones(5)
print(vec6)
# Kết quả: [1. 1. 1. 1. 1.]

vec7 = np.empty(5)
print(vec7)
# Kết quả: [giá trị rác ngẫu nhiên]

print(np.random.random(5))
# Kết quả: [giá trị ngẫu nhiên trong [0, 1)]

v = np.array([1., 3., 5.])
print(np.sum(v))
# Kết quả: 9.0

print(v.shape)
# Kết quả: (3,)

print(v.transpose())
# Kết quả: [1. 3. 5.]

v1 = v[:2]
print(v1)
# Kết quả: [1. 3.]

v[0] = 5
print(v)
# Kết quả: [5. 3. 5.]

print(v1)
# Kết quả: [5. 3.]  # v1 thay đổi theo v vì là view

v1[:2] = [1., 2., 3.]
print(v1)
# Kết quả: [1. 2.]

v1[:2] = [1., 2]
print(v)
# Kết quả: [1. 2. 5.]

v3 = 2 * v[:2] + v1 * 3
print(v3)
# Kết quả: [5. 10.]

v1 = np.array([4, 6])
print(v3)
# Kết quả: [5. 10.]  # v3 không thay đổi

print(v)
# Kết quả: [1. 2. 5.]

print(v + 10.0)
# Kết quả: [11. 12. 15.]

print(np.sqrt(v))
# Kết quả: [1.         1.41421356 2.23606798]

print(np.cos(v))
# Kết quả: [ 0.54030231 -0.41614684  0.28366219]

print(np.sin(v))
# Kết quả: [0.84147098 0.90929743 0.95892427]

print(np.dot(v1, v3))
# Kết quả: 4*5 + 6*10 = 20 + 60 = 80

print(v1.dot(v3))
# Kết quả: 80

print(v3.dot(v1))
# Kết quả: 80