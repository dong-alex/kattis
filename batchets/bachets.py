def solve(stones, choices):

    if stones == 1:
        return 1

    for i in range(len(choices)):
        if choices[i] > stones:
            return 0

        if solve(stones-choices[i], choices):
            return 1

    return 0


memo = {}
while True:
    try:
        data = list(map(int, input().split(' ')))
    except Exception:
        break
    stones, numChoices, choices = data[0], data[1], data[2:]
    print(stones, numChoices, choices)
    if solve(stones, choices):
        print("Stan wins")
    else:
        print("Ollie wins")

# TEST - C++ is proper
