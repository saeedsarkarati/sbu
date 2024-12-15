import numpy as np
x = [-1, -1, 1, 1]
y = [-1, 1, -1, 1]
z = [0, 0, 0, 0]
lx = [2, 2, 2, 2]
ly = [2, 2, 2, 2]

hx = [0, 2, 2, 0]
hy = [0, 0, 2, 0]
hz = [0, 0, 0, 1e-4]
hlx = [1, 1, 0.25, 4]
hly = [1, 4, 0.25, 4]

X = np.array(x)
Y = np.array(y)
Z = np.array(z)
LX = np.array(lx)
LY = np.array(ly)

HX = np.array(hx)
HY = np.array(hy)
HZ = np.array(hz)
HLX = np.array(hlx)
HLY = np.array(hly)

import numpy as np

# ایجاد دو آرایه یک بعدی
array1 = np.array([1, 2])
array2 = np.array([4, 5, 6])

# ایجاد یک آرایه دو بعدی ۲ در ۳ از حاصل ضرب‌های عناصر
result = np.outer(array1, array2)

print(result)



import numpy as np

# ایجاد دو آرایه یک بعدی
array1 = np.array([10, 20])
array2 = np.array([4, 5, 6])

# تغییر شکل آرایه‌ها به منظور استفاده از عملیات برداری
array1 = array1[:, np.newaxis]  # تبدیل به بردار ستونی
array2 = array2[np.newaxis, :]  # تبدیل به بردار ردیفی
print()
print (array1)
print (array2)
# ایجاد آرایه دو بعدی با جمع عناصر
result = array1 + array2

print(result)

