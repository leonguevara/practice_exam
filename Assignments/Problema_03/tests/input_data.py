# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1  | ( [Input strings list], [Output strings list], "Error message string" )
    (
        ["6 6 4", "1 1 1", "2 3 4", "12 13 4", "222 332 5", "0"],
        ["4", "1", "1", "12", "3015"],
        "Revisa tus operaciones y que estés usando la función predefinida correcta"
    ),
    (
        ["1000 1000 10", "1001 1000 10", "1000000000 1000000000 192", "0"],
        ["10000", "10100", "27126743055556"],
        "Revisa tus operaciones y que estés usando la función predefinida correcta"
    ),
    (
        ["1000000000 987654321 1", "456784567 1000000000 51", "39916800 134217728 40320", "100 10001 1000000000",
         "1000000000 1000000000 1", "0"],
        ["987654321000000000", "175618850864484", "3295710", "1", "1000000000000000000"],
        "Revisa tus operaciones y que estés usando la función predefinida correcta"
    )
]
