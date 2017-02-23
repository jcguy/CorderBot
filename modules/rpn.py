import math

binary_operators = ["+", "-", "*", "/", "^"]
unary_operators = ["sqrt"]


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
            if token in binary_operators:
                y = stack.pop()
                x = stack.pop()

                if token == "+":
                    stack.append(x + y)
                elif token == "-":
                    stack.append(x - y)
                elif token == "*":
                    stack.append(x * y)
                elif token == "/":
                    stack.append(x / y)
                elif token == "^":
                    stack.append(x ** y)

            elif token in unary_operators:
                x = stack.pop()

                if token == "sqrt":
                    stack.append(math.sqrt(x))

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
