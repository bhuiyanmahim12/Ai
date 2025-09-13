
def tower_of_hanoi(n, source, target, auxiliary, step=[1], count=[0]):
    if n == 1:
        print(f"Step-> {step[0]} Move disk 1 from {source} to {target}")
        step[0] += 1
        count[0] += 1
        return
    tower_of_hanoi(n-1, source, auxiliary, target, step, count)
    print(f"Step-> {step[0]} Move disk {n} from {source} to {target}")
    step[0] += 1
    count[0] += 1
    tower_of_hanoi(n-1, auxiliary, target, source, step, count)

n = int(input("Enter number of disks: "))
tower_of_hanoi(n, 'A', 'C', 'B')
print(f"Total Step is Required : {2**n - 1}")
 