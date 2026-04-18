def print_steps(conversion_steps):
    for from_u, to_u, value in conversion_steps:
        if from_u != to_u:
            print(f"{from_u} → {to_u}: {value:.4f}")