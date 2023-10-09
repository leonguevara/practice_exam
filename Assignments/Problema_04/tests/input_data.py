# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1  | ( [Input strings list], [Output strings list], "Error message string" )
    (
        ["4", "1 1 1", "1 2", "8 4 6 2", "-2"],
        ["0", "1", "16", "1"],
        "Revisa bien la lógica de tu toma de decisiones y tu aritmética"
    ),
    (
        ["7", "6 6", "5071 5071", "4009 4009", "-2 0 2", "-2 -2 -2", "-2 0 -2", "-2 0 -1"],
        ["10", "10140", "8016", "1", "1", "1", "1"],
        "Revisa bien la lógica de tu toma de decisiones y tu aritmética"
    ),
    (
        ["12", "6 1 10 10 7 2 7", "5 2", "10 5 3 3 2", "10 9 3 9 4 7 3 9 4 8", "4 1 6 9 10 7", "4",
         "5 7 3 2 5 4 4 5 3 9", "2 8 5 2 10 2 6 9 10", "6 10 9", "1 2 7 8 9 1 3", "35 82 17 32 36 48 48 15 33 28",
         "100 9"],
        ["36", "5", "18", "56", "31", "3", "37", "45", "22", "24", "364", "107"],
        "Revisa bien la lógica de tu toma de decisiones y tu aritmética"
    )
]
