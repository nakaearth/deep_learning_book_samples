import numpy as np

a = np.array([1010, 1000, 999])
result = np.exp(a) / np.sum(np.exp(a))

print(result)

c = np.max(a)
a - c

result2 = np.exp(a - c) / np.sum(np.exp(a - c))
print(result2)
