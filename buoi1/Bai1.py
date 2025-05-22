# 1.2.1. Các phép xử lý với danh sách 
# Phép toán với danh sách
danhsach1 = [1., 3.]
danhsach2 = [5., 7.]
danhsach = danhsach1 + danhsach2
print(danhsach)  # Kết quả: [1.0, 3.0, 5.0, 7.0]

danhsach_gapdoi = 2 * danhsach
print(danhsach_gapdoi)  # Kết quả: [1.0, 3.0, 5.0, 7.0, 1.0, 3.0, 5.0, 7.0]

print(danhsach * 2)  # Kết quả: [1.0, 3.0, 5.0, 7.0, 1.0, 3.0, 5.0, 7.0]

# print(danhsach / 2)  # Lỗi: TypeError: unsupported operand type(s) for /: 'list' and 'int'

# Ghép các danh sách bằng zip
mon_hoc = ["ToanCC", "DSTT", "ToanRR", "LaptrinhCB"]
thu_tu = [2, 3, 4, 1]
diem_so = [10, 9, 8, 7]
anh_xa = zip(thu_tu, mon_hoc, diem_so)
print(list(anh_xa))  
# Kết quả: [(2, 'ToanCC', 10), (3, 'DSTT', 9), (4, 'ToanRR', 8), (1, 'LaptrinhCB', 7)]

# Để chuyển thành set, cần tạo lại zip vì zip chỉ dùng được một lần
anh_xa = zip(thu_tu, mon_hoc, diem_so)
tap_hop = set(anh_xa)
print(tap_hop)
# Kết quả: {(1, 'LaptrinhCB', 7), (2, 'ToanCC', 10), (3, 'DSTT', 9), (4, 'ToanRR', 8)}

# Phân rã zip
anh_xa = zip(thu_tu, mon_hoc, diem_so)
lay_TT, lay_monhoc, lay_diem = zip(*anh_xa)
print(lay_monhoc)
# Kết quả: ('ToanCC', 'DSTT', 'ToanRR', 'LaptrinhCB')

# ...existing code...

import itertools

# Tạo danh sách bằng itertools.chain
tap_sinh = list(itertools.chain(range(4), range(5, 10), range(15, 20)))
print(tap_sinh)
# Kết quả: [0, 1, 2, 3, 5, 6, 7, 8, 9, 15, 16, 17, 18, 19]

# Tạo danh sách bằng list comprehension
ds_binhphuong = [x**2 for x in range(6)]
print(ds_binhphuong)
# Kết quả: [0, 1, 4, 9, 16, 25]

# Tạo danh sách bằng zip và range
bo_ba = list(zip(range(4), range(7, 12), reversed(range(11))))
print(bo_ba)
# Kết quả: [(0, 7, 10), (1, 8, 9), (2, 9, 8), (3, 10, 7)]
# ...existing code...

# 1.2.2. Lệnh thực thi một tập tin python
mylist = [100, 200, 300]
a, b, c = mylist
d = print(a, b, c)

import os

def thuc_thi_tap_tin(filepath):
    """Thực thi một tập tin Python."""
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            exec(file.read())
    else:
        print(f"Tập tin {filepath} không tồn tại.")

# Gọi hàm thực thi tập tin
thuc_thi_tap_tin('d:\\DaiSoTuyenTinh\\buoi1\\thucthi1.py')

# 2.1. Định nghĩa Symbol và các phép toán hình thức (symbolic) 
from sympy import Symbol, symbols ,factor, expand

x = Symbol('x')
y = Symbol('y')
s = x*y + y*x
print(s)
# Kết quả: 2*x*y

p = x*(x + 2*x)
print(p)
# Kết quả: 3*x**2

p = (x + 2)*(y + 3)
print(p)
# Kết quả: (x + 2)*(y + 3)

p = (x + 2)*(y + 3) + (x + 2)*(x - 3)
print(p)
# Kết quả: (x + 2)*(y + 3) + (x + 2)*(x - 3)

p = x*(-x + 2*x - x)
print(p)
# Kết quả: 0

# Sử dụng expand để triển khai biểu thức
p = (x + 2)*(y + 3)
print(p.expand())
# Kết quả: x*y + 3*x + 2*y + 6

bieuthuc = x**3 - y**3
print(factor(bieuthuc))
# Kết quả: (x - y)*(x**2 + x*y + y**2)

bieuthuc = (x - y)*(x**2 + x*y + y**2)
print(expand(bieuthuc))
# Kết quả: x**3 - y**3

# 3. Làm quen với thư viện NumPy