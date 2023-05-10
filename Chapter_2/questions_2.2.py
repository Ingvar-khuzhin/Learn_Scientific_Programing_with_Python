import math

print("Question 2.2.4")
i = 1j
print(i**i)
print()


def d6_top_edge(a: int, b: int) -> int:
    """Calculate number on top edge of d6 dice, from 2 number on sides."""
    return 3 * (a**3 * b - a * b**3) % 7


print("Question 2.2.7")
print(f"a = 2, b = 6, top edge = {d6_top_edge(2, 6)}")
print(f"a = 3, b = 5, top edge = {d6_top_edge(3, 5)}")
print()


def half_paper(t: float, d: float) -> int:
    """Calculate how many times need to half sheet with thick t to achieve total thick in d"""
    return int(math.ceil(math.log2(d / t)))


print("Question 2.2.8")
print(f"t = 0.1, d = 384 400, fold in half {half_paper(0.1, 384_400)} times.")
