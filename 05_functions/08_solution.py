
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name= "Saktimaan", power= "laser")        
print_kwargs(name= "Saktimaan")        

print_kwargs(name= "Saktimaan", power= "laser", villian= "Dr. Jakaal")        
