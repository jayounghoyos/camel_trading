def split_expression(expression):
    full_expression = []
    number = ""

    for char in expression:
        if char.isdigit():
            number += char  # Construir el número
        else:
            if number:
                full_expression.append(number)  # Añadir el número
                number = ""
            full_expression.append(char)  # Añadir el operador
    if number:
        full_expression.append(number)  # Añadir el último número
    return full_expression


def maximize(full_expression):
    results = []
    current = int(full_expression[0])

    i = 1
    while i < len(full_expression):
        op = full_expression[i]
        next_num = int(full_expression[i + 1])

        if op == "+":
            current += next_num  # Sumar directamente
        elif op == "*":
            results.append(current)
            current = next_num  # Guardar la multiplicación para después
        i += 2
    results.append(current)

    # Multiplicar todos los resultados acumulados
    final_result = 1
    for num in results:
        final_result *= num
    return final_result


def minimize(full_expression):
    results = []
    current = int(full_expression[0])

    i = 1
    while i < len(full_expression):
        op = full_expression[i]
        next_num = int(full_expression[i + 1])

        if op == "*":
            current *= next_num  # Multiplicación directa
        elif op == "+":
            results.append(current)
            current = next_num  # Guardar la suma para después
        i += 2
    results.append(current)

    # Sumar todos los resultados acumulados
    final_result = sum(results)
    return final_result


def main():
    num_cases = int(input().strip())  # Leer número de casos de prueba

    for _ in range(num_cases):
        expression = input().strip()  # Leer la expresión
        full_expression = split_expression(expression)

        max_val = maximize(full_expression)
        min_val = minimize(full_expression)

        print(f"The maximum and minimum are {max_val} and {min_val}.")


if __name__ == "__main__":
    main()
