user_input = input().replace(" ", "")


def get_two_numbers_by_operator(numbers: str, operator: str):
    return numbers.split(operator)


if "+" in user_input:
    number1, number2 = get_two_numbers_by_operator(user_input, "+")
    print(float(number1) + float(number2))


elif "*" in user_input:
    number1, number2 = get_two_numbers_by_operator(user_input, "*")
    print(float(number1) * float(number2))

elif "/" in user_input:
    number1, number2 = get_two_numbers_by_operator(user_input, "/")
    print(float(number1) / float(number2))

elif "-" in user_input:
    number1, number2 = get_two_numbers_by_operator(user_input, "-")
    print(float(number1) - float(number2))
