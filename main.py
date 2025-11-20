import matplotlib.pyplot as plt
# formula = quantity_remaining: float = quantity * 0.5 ** (time_elapsed / half_life)

def halfLife(half_life, amount, times_week) -> tuple[list, list]:
    freq: float = 7 / times_week
    cycle_length: int = 28
    day_list: list = list(range(cycle_length))
    dose_days: list = [int(round(freq * i)) for i in range(int(times_week * (cycle_length / 7)))]
    life_list: list = [0.0] * cycle_length

    # loop to iterate day then loop of mg on those days
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

# half life in days, mg of substance, times per week
days, doses = halfLife(7, 120, 2)
print(doses)
plotGraph(days, doses)
# days, doses = halfLife(0.5, 6.0, 100)
# plotGraph(days, doses)