def read_input(filename: str) -> list[str]:
    with open(f"../data/{filename}") as f:
        return [line.strip() for line in f.readlines()]

def read_input_for_day(n: int) -> list[str]:
    return read_input(f"day{n}.txt")
