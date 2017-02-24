def send_help(bot, message):
    bot.send_message(message.chat.id,
                     "All commands start with /c\n" +
                     "\nAvailable commands:" +
                     "\n\thelp" +
                     "\n\trpn" +
                     "\n\tweather"
                     )
