# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1  | ( [Input strings list], [Output strings list], "Error message string" )
    (
        ["a", "ba", "ab", "bac", "ihfcbadeg", "z", "aa", "ca", "acb", "xyz", "ddcba", "0"],
        ["Sí", "Sí", "Sí", "Sí", "Sí", "No", "No", "No", "No", "No", "No"],
        "Valida tus comparaciones y tu lògica computacional"
    ),
    (
        ["cbaed", "edab", "ddba", "dbaec", "cabb", "bbbcd", "aab", "0"],
        ["No", "No", "No", "No", "No", "No", "No"],
        "Valida tus comparaciones y tu lògica computacional"
    ),
    (
        ["cdeab", "kihgj", "a", "pno", "dabc", "cbac", "cab", "ac", "aa", "0"],
        ["No", "No", "Sí", "No", "Sí", "No", "Sí", "No", "No"],
        "Valida tus comparaciones y tu lògica computacional"
    )
]
