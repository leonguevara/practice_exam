# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1  | ( [Input strings list], [Output strings list], "Error message string" )
    (
        ["3 7 9 5", "4 5 6 9", "5 3 8 1", "6 5 3 2", "0"],
        ["Sí", "No", "Sí", "No"],
        "Revisa que estés segmentando y ordenando bien tus arreglos"
    ),
    (
        ["6 54 28 29", "56 66 99 89", "87 51 41 63", "44 84 46 67", "75 67 61 83", "30 14 89 23", "13 42 74 17",
         "55 45 62 70", "48 75 53 78", "0"],
        ["Sí", "No", "Sí", "Sí", "Sí", "Sí", "Sí", "No", "Sí"],
        "Revisa que estés segmentando y ordenando bien tus arreglos"
    ),
    (
        ["19 88 56 74", "57 27 12 4", "9 67 99 42", "7 99 84 12", "69 92 35 53", "51 19 81 99", "59 98 40 54",
         "85 80 57 50", "90 7 25 11", "61 89 56 36", "0"],
        ["Sí", "No", "Sí", "Sí", "No", "No", "No", "No", "Sí", "No"],
        "Revisa que estés segmentando y ordenando bien tus arreglos"
    )
]
