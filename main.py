import matplotlib.pyplot as plt
# formula = quantity_remaining: float = quantity * 0.5 ** (time_elapsed / half_life)

half_life: float = 7 # days
quantity: float = 120 # millagrams
in_system: float = 0
freq: float = 3.5
intake_length: int = 28 * 2
intake: list = []
day_list: list = []
quantity_list: list = []

# Set up the lights and add quanity to the intake days
for take in range(intake_length):
    quantity_list.append(0)
    day_list.append(take)
    intake.append(int(freq * take))
    if take in intake:
        quantity_list[take] += quantity
    for i in range(int(half_life) * 7):
        try:
            quantity_list[take + i] += quantity * 0.5 ** (take / half_life)
        except:
            continue
            
cycles_five: float = intake[-1] * 5
quantity_list[0] = quantity

for i in range(max(len(day_list), len(quantity_list))):
    print(f"{day_list[i]} : {quantity_list[i]:.2f},", end=" ")
    pass

def plotGraph():
    plt.plot(0, 0, color="white") # forces graph to go to 0 on the x and y axis
    plt.plot(day_list, quantity_list, color="blue")
    plt.xlabel("Time (day)")
    plt.ylabel("Substance left (mg)")
    plt.title("Half life grapher")
    plt.show()
    
plotGraph()