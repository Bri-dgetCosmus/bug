#write a program that prints numners 1- 100. if the numberv is divisible by 3, print 'Fizz' if divisible by 5, print 'Buzz', if div by both print 'FizzBuzz'
def fizzbuzz():
    for num in range(1,100):
        if num % 3 == 0 and num % 5 == 0 :
            print("FizzBuzz")
        elif num % 3 == 0:
                print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 7 == 0:
             print("Bazz")
        else :
            print(num)
if __name__ == "__main__":
    fizzbuzz()
