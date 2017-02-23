#!/usr/bin/env python3

import telebot


with open("token", "r") as token:
    bot = telebot.TeleBot(token.readlines()[0].strip()) 


