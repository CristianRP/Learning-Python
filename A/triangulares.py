def draw_triangle(n):
    for x in range(0, n):
        z = (x * 2) + 1
        print(" " * n, "*" * z)
        n -= 1

print(draw_triangle(5))