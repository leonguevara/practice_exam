# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1  | ( [Input strings list], [Output strings list], "Error message string" )
    (
        ["11 13 11 11", "1 4 4 4 4", "3 3 3 3 10 3 3 3 3 3", "20 20 10", "0"],
        ["2", "1", "5", "3"],
        "Valida tus condicionales y la lógica de programación"
    ),
    (
        ["68 68 68 68 68 68 68 68 68 68 68 68 68 68 68 40 68 68 68", "3 2 2 2 2",
         "1 1 1 1 1 1 1 1 1 1 1 1 1 100 1 1 1 1 1 1 1", "4 4 4 4 4 4 4 4 4 4 4 6 4 4 4 4 4 4",
         "100 100 100 100 100 100 100 100 100 100 1 100 100 100 100", "0"],
        ["16", "1", "14", "12", "11"],
        "Valida tus condicionales y la lógica de programación"
    ),
    (
        ["5 6 6", "7 7 6", "5 5 5 5 3", "4 4 4 1 4", "2 4 2 2 2", "0"],
        ["1", "3", "5", "4", "2"],
        "Valida tus condicionales y la lógica de programación"
    )
]
