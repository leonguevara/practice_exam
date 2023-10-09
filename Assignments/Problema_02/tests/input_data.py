# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1  | ( [Input strings list], [Output strings list], "Error message string" )
    (
        ["50 50 100", "0 25 50 75", "0 1 8", "96 89 93 95 70", "0"],
        ["66.67 - Sí", "37.50 - No", "3.00 - No", "88.60 - Sí"],
        "Revisa tus operaciones, tu toma de deciones o tu cadena de formato"
    ),
    (
        ["95 70 93 74 94 70 91 70 39 79 80 57 87 75 37 93 48 67 51 90 85 26 23 64 66 84",
         "84 99 72 96 83 92 95 98 97 93 76 84 99 93 81 76 93 99 99 100 95 100 96 95 97 100 71 98 94",
         "100 99 100 100 99 99 99 100 100 100 99 99 99 100 100 100 100 99 100 99 100 100 97 100 100 100 100 100 100 100 98 98 100",
         "14 9 10 5 4 26 18 23 0 1 0 20 18 15 2 2 3 5 14 1 9 4 2 15 7 1 7 19 10 0 0 11 0 2",
         "50 50 50 50 50", "0"],
        ["69.54 - Sí", "91.55 - Sí", "99.52 - Sí", "8.15 - No", "50.00 - No"],
        "Revisa tus operaciones, tu toma de deciones o tu cadena de formato"
    ),
    (
        ["0 100", "78", "0 0 0 0 1",
         "100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100",
         "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 100",
         "10 70 12 89 1 82 100 53 40 100 21 69 92 91 67 66 99 77 25 48 8 63 93 39 46 79 82 14 44 42 1 79 0 69 56 73 67 17 59",
         "7 8 1 16 0 15 1 7 0 11 15 6 2 12 2 8 9 8 2 0 3 7 15 7 1 8 5 7 2 26 0 3 11 1 8 10", "0"],
        ["50.00 - No", "78.00 - Sí", "0.20 - No", "100.00 - Sí", "4.00 - No", "54.95 - Sí", "6.78 - No"],
        "Revisa tus operaciones, tu toma de deciones o tu cadena de formato"
    )
]
