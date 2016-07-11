import os
import sys
from scipy import misc

bmp_path=input('Enter bitmap path:')
file_path=input('Enter file path:')

assert os.path.exists(bmp_path), "No bmp at, "+str(bmp_path)
assert os.path.exists(file_path), "No file at, "+str(file_path)

bmp_file=open(bmp_path,'rb+')
file_file=open(file_path,'rb+')

bmp_data=bytearray(bmp_file.read())
file_data=bytearray(file_file.read())

if len(bmp_data)-54<len(file_data)*4:
	print("Image too small!")
	bmp_file.close()
	file_file.close()
	sys.exit(0)

result=bytearray(len(bmp_data))
result[0:54]=bmp_data[0:54]

index=54

for x in file_data:
	for y in (7,0):
		mask=2**y
		bit=x&mask
		if y%2!=0:
			if bit==1:
				bmp_data[index]=bmp_data[index]|0b00000010
			else:
				bmp_data[index]=bmp_data[index]&0b11111101
		if y%2==0:
			if bit==1:
				bmp_data[index]=bmp_data[index]|0b00000001
			else:
				bmp_data[index]=bmp_data[index]&0b11111110
			result.append(bmp_data[index])
			index+=1

for x in bmp_data[index:]:
	result.append(x)

save_path=input('Enter save path:')
with open(save_path,'wb') as output:
	output.write(result[:])

assert os.path.exists(save_path), "No file at, "+str(file_path)

bmp_file.close()
file_file.close()