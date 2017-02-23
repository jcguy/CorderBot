import math

constants = {"e" : math.e, "pi" : math.pi}

binary_operators = ["+", "-", "*", "/", "^", "log"]
unary_operators = ["sqrt", "ln"]


def calculate(bot, message):
    calculation = message.text.split(" ")[2:]

    print(calculation)

    stack = []
    for token in calculation:
        try:
            stack.append(float(token))
            continue
        except ValueError:
            pass

        try:
            if token in constants.keys():
                stack.append(constants[token])

            elif token in binary_operators:
                x = stack.pop()
                y = stack.pop()

                if token == "+":
                    stack.append(y + x)
                elif token == "-":
                    stack.append(y - x)
                elif token == "*":
                    stack.append(y * x)
                elif token == "/":
                    stack.append(y / x)
                elif token == "^":
                    stack.append(y ** x)
                elif token == "ln":
                    stack.append(math.log(y, x))

            elif token in unary_operators:
                x = stack.pop()

                if token == "sqrt":
                    stack.append(math.sqrt(x))
                elif token == "ln":
                    stack.append(math.log(x))

            else:
                bot.send_message(message.chat.id, "Unrecognized operator")

        except IndexError:
            bot.send_message(message.chat.id, "Syntax error")
            return

        except ValueError:
            bot.send_message(message.chat.id, "Domain error")
            return

        except ZeroDivisionError:
            bot.send_message(message.chat.id, "Division by zero")
            return

    if len(stack) == 1:
        bot.send_message(message.chat.id, str(stack[-1]))
    else:
        bot.send_message(message.chat.id, "Syntax error")
