from inputs import list_input
import cProfile

def forward_rotation(l, n):
    for i in range(n):
        for i in range(len(l)-1):
            l[i],l[i+1] = l[i+1],l[i]
    return l 

def backward_rotation(l, n):
    for i in range(n):
        for i in range(-len(l)-1,-1):
            l[i-1],l[i] = l[i],l[i-1]
    return l 

l = list_input(int(input("Enter the number of numbers you want as inputs : ")))
    
num_rot = int(
        input(
            "Enter the number of rotation you want : "
            )
        )
print(forward_rotation (l, num_rot))
cProfile.run("forward_rotation (l, num_rot)")
