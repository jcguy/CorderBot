def calculate(bot, message):
    calculation = message.text.split(" ")[2:]

    stack = []
    for token in calculation:
        try:
            stack.append(float(token))
            continue
        except ValueError:
            pass

        try:
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

        except IndexError:
            bot.send_message(message.chat.id, "Syntax error")
            return

        except ZeroDivisionError:
            bot.send_message(message.chat.id, "Division by zero")
            return

    bot.send_message(message.chat.id, str(stack[-1]))
