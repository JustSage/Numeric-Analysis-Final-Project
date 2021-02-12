"""

code to decide which questions to pick based on the id numbers of the participants.

"""

from random import randint

ids = {
    "Nikolay": 321123242,
    "Sagie": 205591829,
    "Alex": 317414506,
    "Avi": 203397666
}

options = (9, 8, 12, 12, 6, 6)


def decide(options):
    base = sum(ids.values())
    return (base + randint(0, options - 1)) % options + 1


def make_decisions(all_options):
    result = [decide(all_options[0]),
              decide(all_options[1]) + options[0],
              decide(all_options[2]) + options[0] + options[1],
              decide(all_options[3]) + options[0] + options[1],
              decide(all_options[4]) + options[0] + options[1] + options[2],
              decide(all_options[5]) + options[0] + options[1] + options[2] + options[4]]

    while result[3] == result[2]:
        result[3] = decide(all_options[3]) + options[0] + options[1]

    return result


if __name__ == "__main__":
    result = make_decisions(options)
    for i in range(len(result)):
        print("Question #{0}: {1}".format(i+1, result[i]))
