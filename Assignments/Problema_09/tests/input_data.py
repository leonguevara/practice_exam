# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1  | ( [Input strings list], [Output strings list], "Error message string" )
    (
        ["3", "abacaba", "1 3", "2 5", "1 7"],
        ["4", "7", "11"],
        "Revisa bien tus índices."
    ),
    (
        ["4", "abbabaa", "1 3", "5 7", "6 6", "2 4"],
        ["5", "4", "1", "5"],
        "Revisa bien tus índices."
    ),
    (
        ["7", "sonoshikumiwo", "1 5", "2 10", "7 7", "1 13", "4 8", "2 5", "3 9"],
        ["82", "125", "9", "191", "62", "63", "97"],
        "Revisa bien tus índices."
    )
]
