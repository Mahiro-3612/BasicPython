text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""


def letter_count_sequence(input):

    input = input.replace(",", "").replace(".", "").split()

    letter_counts = list(map(len, input))

    output = ""

    for letter_count in letter_counts:
        output += str(letter_count)

    return output


# 問2
print(f"円周率は{letter_count_sequence(text)}")
