start = int(input("Start: "))
stop = int(input("Stop: "))
step = int(input("Step: "))

print("\nRange with 1 argument (start=0 and step=1 by default)")
for i in range(stop):
    print(i)

print("\nRange with 2 arguments (step=1 by default)")
for i in range(start, stop):
    print(i)
    
print("\nRange with 3 arguments")
for i in range(start, stop, step):
    print(i)