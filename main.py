import matplotlib.pyplot as plt

def halfLife(half_life, amount, times_week) -> tuple[list, list]:
    freq: float = 7 / times_week
    cycle_length: int = 28
    day_list: list = [i for i in range(cycle_length)]
    dose_days: list = [int(round(freq * i)) for i in range(int(times_week * (cycle_length / 7)))]
    life_list: list = [0.0] * cycle_length

    for day in range(cycle_length):
        if day > 0:
            life_list[day] = life_list[day -1] * (0.5 ** (1 / half_life))
        if day in dose_days:
            life_list[day] += amount
    return (day_list, life_list)

def plotGraph(day_list, quantity_list) -> None:
    plt.plot(day_list, quantity_list, color="blue") 
    plt.ylim(0, max(quantity_list) + max(quantity_list) / 10)
    plt.xlabel("Time (day)")
    plt.ylabel("Substance left (mg)")
    plt.title("Half life grapher")
    plt.show()

# half life function (half life, amount in mg, times a week substance is added)
days, doses = halfLife(7, 120, 2)
print(doses)
plotGraph(days, doses)