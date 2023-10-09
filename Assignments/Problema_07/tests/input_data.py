# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1  | ( [Input strings list], [Output strings list], "Error message string" )
    (
        ["10", "1", "2", "3", "4", "5", "6", "7", "8", "9", "1000"],
        ["1", "2", "4", "5", "7", "8", "10", "11", "14", "1666"],
        "Revisa bien el armado de tu serie y tus índices."
    ),
    (
        ["5", "745", "23", "970", "148", "500"],
        ["1240", "37", "1616", "245", "832"],
        "Revisa bien el armado de tu serie y tus índices."
    ),
    (
        ["8", "670", "584", "391", "699", "700", "382", "299", "613"],
        ["1115", "971", "650", "1165", "1166", "635", "497", "1021"],
        "Revisa bien el armado de tu serie y tus índices."
    )
]
