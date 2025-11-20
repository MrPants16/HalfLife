import matplotlib.pyplot as plt
import json

def halfLife(half_life, amount, cycle_length, times_week=1, par=0) -> tuple[list, list]:
    freq: float = 7 / times_week
    day_list: list = [i for i in range(int(cycle_length))]
    dose_days: list = [int(round(freq * i)) for i in range(int(times_week * (cycle_length / 7)))]
    life_list: list = [0.0] * cycle_length

    if par:
        dose_days = [0]
    
    for day in range(cycle_length):
        if day > 0:
            life_list[day] = life_list[day -1] * (0.5 ** (1 / half_life))
        if day in dose_days:
            life_list[day] += amount
            
    five_cycle: int = int(half_life * 5)
    print(f"{five_cycle} days to run 5 cycles")
    
    return (day_list, life_list)

def plotGraph(day_list, quantity_list) -> None:
    plt.plot(day_list, quantity_list, color="blue") 
    plt.ylim(0, max(quantity_list) + max(quantity_list) / 10)
    plt.xlabel("Time (day)")
    plt.ylabel("Substance left (mg)")
    plt.title("Half life grapher")
    plt.show()

# half life function (half life, amount in mg, cycle length, [optional times a week substance is added (default is 1, cannot be 0)] [optional value of 1 for no extra additions])
item: tuple = (6, 71, 84, 3)
# days, doses = halfLife(item[0], item[1], item[2], item[3] if len(item) > 3 else 1, item[4] if len(item) > 4 else 0)
# plotGraph(days, doses)

def choiceMade(list: int, choice: int):
    pass

def userInput():
    mat_list: list = []
    print(f"Half life Grapher\nCreator Rylan Rees\n{"=" * 18}")
    choice: int = int(input("For object to test:\n[1] To choose preset drug\n[2] To choose preset material\n[3] Choose your previous save\n[0] To create your own\n>"))
    if choice == 1:
        with open("presets/substances.json", "r") as file:
            data = json.load(file)
        for index, sub in enumerate(data):
            print(f"[{index + 1}] {sub["name"]}")
            mat_list.append(sub["name"])
        choice = int(input(">"))
        print(mat_list[choice - 1])
    elif choice == 2:
        with open("presets/materials.json", "r") as file:
            data = json.load(file)
        for index, mat in enumerate(data):
            print(f"[{index + 1}] {mat["name"]}")
            mat_list.append(mat["name"])
        print(data["name"] == mat_list[0])
    elif choice == 3:
        with open("presets/custom.json", "r") as file:
            data = json.load(file)
        for index, mat in enumerate(data):
            print(f"[{index + 1}] {mat["name"]}")
    else:
        pass
    # return (halflife, amount, cycle_length, per_week, perm)
if __name__ == "__main__":
    material = userInput()