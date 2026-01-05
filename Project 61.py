def reverse_bits(number):
    binary_str = bin(number)[2:]
    reversed_str = binary_str[::-1]
    reversed_number = int(reversed_str, 2)
    return reversed_number
num = int(input("Enter a number: "))
result = reverse_bits(num)
print(f"Original number:{num} (binary:{bin(num)[2:]})")
print(f"Reversed number: {result} (binary:{bin(result)[2:]})")