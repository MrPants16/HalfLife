import matplotlib.pyplot as plt

def halfLife(half_life, amount, cycle_length, times_week=1, par=0) -> tuple[list, list]:
    freq: float = 7 / times_week
    day_list: list = [i for i in range(cycle_length)]
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
    print(five_cycle)
    
    return (day_list, life_list)

def plotGraph(day_list, quantity_list) -> None:
    plt.plot(day_list, quantity_list, color="blue") 
    plt.ylim(0, max(quantity_list) + max(quantity_list) / 10)
    plt.xlabel("Time (day)")
    plt.ylabel("Substance left (mg)")
    plt.title("Half life grapher")
    plt.show()

# half life function (half life, amount in mg, cycle length, [optional times a week substance is added (default is 1, cannot be 0)] [optional value of 1 for no extra additions])
days, doses = halfLife(7, 250, 56, 2, 0)
plotGraph(days, doses)