# bounce.py
#
# Exercise 1.5
def bounce(height: float, bounce_height: float, bounces: int) -> None:
    for i in range(bounces):
        print(i + 1, "{:.4f}".format(height))
        height *= bounce_height


bounce(60, .6, 10)