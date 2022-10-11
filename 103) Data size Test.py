import sys

sample1 = []
sample2 = []
sample3 = []

for i in range(1000000):
    sample1.append("507f191e810c19729de860ea")

for i in range(500000):
    sample2.append("507f191e810c19729de860ea")

for i in range(100000):
    sample3.append("507f191e810c19729de860ea")

size1 = sys.getsizeof(sample1)
size2 = sys.getsizeof(sample2)
size3 = sys.getsizeof(sample3)

print("######## SAMPLE 1: 1 million id's ############")
print(f"Size in bytes: {size1} bytes")
print(f"Size in megabytes: {size1/1000000} Mb\n")

print("######## SAMPLE 2: 500 thousand id's ############")
print(f"Size in bytes: {size2} bytes")
print(f"Size in megabytes: {size2/1000000} Mb\n")

print("######## SAMPLE 3: 100 thousand id's ############")
print(f"Size in bytes: {size3} bytes")
print(f"Size in megabytes: {size3/1000000} Mb")
