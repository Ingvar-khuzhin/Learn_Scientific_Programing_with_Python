print("Question 2.2.4")
i = 1j
print(i**i)
print()


def d6_top_edge(a: int, b: int) -> int:
    return 3 * (a**3 * b - a * b**3) % 7


print("Question 2.2.7")
print(f"a = 2, b = 6, top edge = {d6_top_edge(2, 6)}")
print(f"a = 3, b = 5, top edge = {d6_top_edge(3, 5)}")
print()
