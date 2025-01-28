"""Planning a tea party"""

__author__: str = "730649767"


def main_planner(guests: int) -> None:
    """Brings all functions together"""
    needed_tea = tea_bags(people=guests)
    needed_treats = treats(people=guests)
    cost_per = cost(needed_tea, needed_treats)

    print(f"A Cozy Tea Party for {guests} People!")
    print(f"Tea Bags: {needed_tea}")
    print(f"Treats: {needed_treats}")
    print(f"Cost: ${cost_per:}")


def tea_bags(people: int) -> int:
    """Calculates amount of tea bags needed per person"""
    return people * 2


tea_bags(people=10)


def treats(people: int) -> int:
    """Calculate amount of treats needed per person"""
    tea_total = tea_bags(people=people)
    return int(tea_total * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculating total cost of everything"""
    return (tea_count * 0.50) + (treat_count * 0.75)


cost(tea_count=2, treat_count=1)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
