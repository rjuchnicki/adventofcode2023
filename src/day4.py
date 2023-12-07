from utils import read_input_for_day


DAY = 4
lines = read_input_for_day(DAY)


def part1():
    output = ""
    input = [l[l.find(':') + 1:].split('|') for l in lines]
    tickets = []
    for i in input:
        tickets.append([{int(e) for e in i[0].split()}, [int(e) for e in i[1].split()]])

    output = 0
    for t in tickets:
        pow = -1
        for num in t[1]:
            if num in t[0]:
                pow += 1
        if pow > -1:
            output += 2 ** pow           

    return output


def part2():
    input = [l[l.find(':') + 1:].split('|') for l in lines]
    tickets = []
    for i in input:
        tickets.append([{int(e) for e in i[0].split()}, [int(e) for e in i[1].split()]])

    counts = [1 for t in tickets]
    for i, t in enumerate(tickets):
        num_cards = counts[i]
        matches = 0
        for num in t[1]:
            if num in t[0]:
                matches += 1
        for j in range(0, matches):
            if i + j + 1 < len(counts):
                counts[i + j + 1] += num_cards
    
    return sum(counts)


if __name__ == "__main__":
    print(part1())
    print(part2())
