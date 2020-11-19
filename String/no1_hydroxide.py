def is_hydroxide(chemical):
    hydroxide = chemical.endswith("OH")

    return hydroxide

chem = "H2O"
print(is_hydroxide(chem))