# -*- coding:utf-8 -*-
num =0
for i in range(1,5):
	for j in range(1,5):
		for k in range(1,5):
			if i !=j and i !=k and j!=k:
				num += 1
				print("%d%d%d"%(i,j,k))
print(num)