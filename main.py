#!/usr/bin/env python3

import modules.help
import modules.rpn
import modules.weather
import modules.quotes
import telebot

with open("token", "r") as token:
    bot = telebot.TeleBot(token.readlines()[0].strip())


@bot.message_handler(commands=["Corder", "C", "c"])
def handle_commands(message):
    content = message.text.split(" ", maxsplit=1)[-1]
    print(content)

    if len(message.text.split(" ")) == 1:
        modules.help.send_help(bot, message)
        return

    if "help" in content.lower():
        modules.help.send_help(bot, message)
        return

    if content.lower().startswith("rpn"):
        modules.rpn.calculate(bot, message)
        return

    if content.lower().startswith("weather"):
        modules.weather.weather(bot, message)
        return

    if "ice" in content.lower() and "water" in content.lower():
        modules.quotes.ice(bot, message)

    bot.send_message(message.chat.id, "Command not recognized.")


def main():
    print("Starting bot")
    bot.polling()
    print("Shutting down")


if __name__ == "__main__":
    main()
