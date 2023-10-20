"""
Advent of Code - Day 4: The Ideal Stocking Stuffer
"""

import hashlib

# load text file
with open('input.txt', 'r') as input:
    secret_key = input.read().strip()

###########
# Part One
###########
# Convert string into bytes to be acceptable by hash function, and return encoded data in hexadecimal format
md5_hash = hashlib.md5(secret_key.encode()).hexdigest()

lowest_number = 0
while md5_hash[:5] != "00000":
    hash_input = secret_key + str(lowest_number)
    md5_hash = hashlib.md5(hash_input.encode()).hexdigest()
    lowest_number += 1

print(f"lowest number: {lowest_number - 1}, MD5 hash: {md5_hash}")

###########
# Part Two
###########
md5_hash = hashlib.md5(secret_key.encode()).hexdigest()

lowest_number = 0
while md5_hash[:6] != "000000":
    hash_input = secret_key + str(lowest_number)
    md5_hash = hashlib.md5(hash_input.encode()).hexdigest()
    lowest_number += 1

print(f"lowest number: {lowest_number - 1}, MD5 hash: {md5_hash}")
