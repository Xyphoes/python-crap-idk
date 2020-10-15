def mos(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return (num1 + num2)
numb1 = 10
numb2 = 10

result = mos(numb1,numb2)
print(result)
