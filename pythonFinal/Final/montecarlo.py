# Function to calculate the Net Profit
def run01():
    def Profit(Sales, Price, Cost, Fixed_Cost):
        profit = (Price - Cost) * Sales - Fixed_Cost

        return profit


    # Average Model
    fixed_cost = 120000 #given in the problem statement
    sales_v_avg = 75000
    price_avg = 9.67
    unit_cost = 6.50

    # Net Profit
    Net_Profit_Avg = Profit(sales_v_avg, price_avg, unit_cost,fixed_cost)
    print(f"The Net Profit for an Average model: {Net_Profit_Avg}")

    # Function to model the market scenario and select sales volume and price per unit

    import numpy as np


    def Market_Scenario():
        market_condition = np.random.choice([1, 2, 3], size=1)[0]

        # Selecting the Sales volume and price per unit based on the market condition
        # Hot Market
        if market_condition == 1:
            sales_v = 100000
            unit_price = 8

        # OK Market
        elif market_condition == 2:
            sales_v = 75000
            unit_price = 10

        # Slow Market
        else:
            sales_v = 50000
            unit_price = 11

        return market_condition, sales_v, unit_price

    # Function to model the Unit cost for making the product
    def UnitCost():
        unit_cost = np.random.normal(loc = 6.50, scale = (7.5 - 5.5)/3.29) #For 90% confidence, z-score = 3.29
        return unit_cost

    # Simulation
    import matplotlib.pyplot as plt
    import seaborn as sns

    sns.set()

    # number of simulations
    num_simulations = 10000

    # create an empty list to store the simulation estiamtes
    profit_estimates = []

    for i in range(num_simulations):
        # Get the market scenario
        market, sales, price = Market_Scenario()

        # Find the unit cost
        cost = UnitCost()

        # Calculate the Net Profit
        p = Profit(sales, price, cost, fixed_cost)
        profit_estimates.append(p)

    negative_profits = [1 if x < 0 else 0 for x in profit_estimates]

    print(f"Minimum Net Profit could be: ${round(min(profit_estimates),3)}")
    print(f"Maximum Net Profit could be: ${round(max(profit_estimates),3)}")
    print(f"Average Net Profit could be: ${round(np.mean(profit_estimates),3)}")
    print(f"Probability of Loss: {round(np.mean(negative_profits)*100,3)}%")

def run02():
    import random

    def random_walk(n):
        x = 0
        y = 0
        for i in range(n):
            step = random.choice(['N','S','E','W'])
            if step == 'N':
                y = y + 1
            elif step == 'S':
                y = y - 1
            elif step == 'E':
                x = x + 1
            else:
                x = x - 1
        return (x, y)

    for i in range(25):
        walk = random_walk(10)
        print(walk, "Distance from home = ", abs(walk[0]) + abs(walk[1]))

def run03():

    import random

    def random_walk_2(n):
        x, y = 0, 0
        for i in range(n):
            (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
            x += dx
            y += dy
        return (x, y)


    number_of_walks = 20000

    for walk_length in range(1, 31):
        no_transport = 0
        for i in range(number_of_walks):
            (x, y) = random_walk_2(walk_length)
            distance = abs(x) + abs(y)
            if distance <= 4:
                no_transport += 1
        no_transport_percentage = float(no_transport) / number_of_walks
        print("Walk size = ", walk_length, " / % of no transport = ", 100*no_transport_percentage)
