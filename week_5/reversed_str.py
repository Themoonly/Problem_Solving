import time

str = str(input("Enter string : "))

start = time.time()
rev = ''.join(reversed(str))
endtime = time.time()
print(rev , endtime - start)

# import time

# str = str(input("Enter string : "))

# start = time.time()
# rev = ''.join(reversed(str))
# endtime = time.time()
# print(rev , endtime - start)
