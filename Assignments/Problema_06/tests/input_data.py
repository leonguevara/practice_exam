# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1  | ( [Input strings list], [Output strings list], "Error message string" )
    (
        ["ABA", "DDBBCCCBBEZ", "FFGZZZY", "Z", "AB", "0"],
        ["No", "No", "Sí", "Sí", "Sí"],
        "Revisa tu lógica de conjuntos"
    ),
    (
        ["BAA", "CBC", "DACD", "BBAC", "DAAA", "DCAC", "AAAAAAAAAA", "ILOVEELINA", "0"],
        ["Sí", "No", "No", "Sí", "Sí", "No", "Sí", "No"],
        "Revisa tu lógica de conjuntos"
    ),
    (
        ["MURCIELAGO", "PERRO", "RATA", "GATO", "ELEFANTE", "CAMELLO", "ESCORPION", "0"],
        ["Sí", "Sí", "No", "Sí", "No", "Sí", "No"],
        "Revisa tu lógica de conjuntos"
    )
]
