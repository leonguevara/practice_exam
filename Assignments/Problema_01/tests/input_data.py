# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1  | ( [Input strings list], [Output strings list], "Error message string" )
    (
        ["6", "1000", "30", "1", "32", "1000000000", "5"],
        ["334 333", "10 10", "1 0", "10 11", "333333334 333333333", "1 2"],
        "Checa bien que la diferencia entre ambos sea mínima"
    ),
    (
        ["1", "10111"],
        ["3371 3370"],
        "Checa bien que la diferencia entre ambos sea mínima"
    ),
    (
        ["1", "3000002"],
        ["1000000 1000001"],
        "Checa bien que la diferencia entre ambos sea mínima"
    ),
(
        ["2", "3000002", "3000001"],
        ["1000000 1000001", "1000001 1000000"],
        "Checa bien que la diferencia entre ambos sea mínima"
    )
]
