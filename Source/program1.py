# test program
# works

print ("Hello again World")

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while b < 0:
    print(b)
    a, b = b, a+b

while a<10:
    print(b)
    a,b=b,a+b


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

if ask_ok('quit?') :
    print ('bye')
else:
    print ('bye anyway')
