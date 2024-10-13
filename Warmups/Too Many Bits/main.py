print(
    ''.join(
        map(
            lambda x: chr(int(x, 2)),
            open("input.txt").read().strip().split(" ")
        )
    )
)
