def send_help(bot, message):
    bot.send_message(message.chat.id,
                     "All commands start with /C\n" +
                     "\nAvailable commands:" +
                     "\n\thelp" +
                     "\n\trpn"
                     )
