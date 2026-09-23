import time
start_time = time.time()

print("Hello World")
# cara mengcompile, buka terminal, ketik python3 -m py_compile main.py

print(time.time() - start_time, "detik")

#variabel adalah tempat menyimpan data
x = 10
a = 7
panjang = 1000
#pemanggilan pertama
print("Nilai a = ", a)
print("Nilai x = ", x)
print("Nilai panjang = ", panjang)

nilai_b = x

#pemanggilan kedua
print("nilai b = ", nilai_b)

#tipe data integer yang gaada koma 
data_integer = 1

print("data : ", data_integer)
print("- bertipe: ", type(data_integer))

#data float 
data_float = 1.4
print("data : ", data_float)
print("- bertipe: ", type(data_float))

#data string
data_string = "ucup"
print("data: ", data_string)
print("- bertipe: ", type(data_string))

#data bool
data_bool = True
print("data : ", data_bool)
print("- bertipe :", type(data_bool))

#data complex
data_complex = complex(5,6)
print("data : ", data_complex)
print("- bertipe :", type(data_complex))

#tipe data dari bahasa c
from ctypes import c_double 

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- bertipe :", type(data_c_double))