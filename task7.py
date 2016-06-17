
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step


def calc(func,a,b,c):
    return [ "argument :"+ str(x) +" -- value "+str(eval(func)) for x in my_range(a,b,c)]

function = input("enter function  ")
if (not function.__contains__("x")):
    print("funtion input should contains x ")
    print(" program closing....")
    exit(0)

try:
    a=int(input('Input a:'))
    b=int(input('Input b:'))
    dx=int(input('Input delta x:'))    
except ValueError:
    print ("Not a number")


res =calc(function,a,b,dx)
print(res)
print("save data to file Output.txt")
with open("Output.txt", "w") as text_file:
    print(res, file=text_file)


#неправильный набор входных