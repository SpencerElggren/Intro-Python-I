num1 = int(input('number? '))


def isPrime(num):
    for i in range(2, num):
        if (num % i) == 0:
            print("not prime")
            break
    else:
        print("prime!")


isPrime(num1)
