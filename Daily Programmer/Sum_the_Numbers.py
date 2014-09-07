def sum_of_numbers(num):
    sum = 0
    rem = num % 10
    quo = num / 10
    while True:
        sum += rem
        rem = quo % 10
        quo = quo / 10
        if quo == 0:
            sum += rem
            break
    return sum
    

num = int(raw_input("Enter a number"))
sum = sum_of_numbers(num)
while True:
    if sum / 10 == 0:
        print sum
        break
    else:
        sum = sum_of_numbers(sum)
        