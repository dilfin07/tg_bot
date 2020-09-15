import logging, ephem, datetime, requests, re
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from setting import API_KEY, MARSS, MERCURY, URANUS, JUPITER, VENUS, NEPTUNE, SATURN, system, NOT_Plan

now = datetime.datetime.now()
logging.basicConfig(filename='bot.log', level=logging.INFO)


def greet_user(update, context):
    print('Вызван /start')
    print(update.message.text.split())
    update.message.reply_text('Привет! На какую планету отправимся?)')
    update.message.reply_photo(photo=system)
    update.message.reply_text('Чтобы отправится к нужной планете просто используй конду /planet [planet] например  '
                              '/planet Venus')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def planet(update, context):
    get_planet = update.message.text.split()
    print(get_planet)
    if get_planet[1] == "Mars":
        update.message.perly_photo(MARSS)
        mars = ephem.Mars(now)
        planet_now = ephem.constellation(mars)
        update.message.reply_text(f'Сегодня планета "{get_planet[1]}" находится в созвездии: {planet_now[1]}')
    elif get_planet[1] == "Neptune":
        update.message.reply_photo(NEPTUNE)
        Neptune = ephem.Neptune(now)
        planet_now = ephem.constellation(Neptune)
        update.message.reply_text(f'Сегодня планета "{get_planet[1]}" находится в созвездии: {planet_now[1]}')
    elif get_planet[1] == "Uranus":
        update.message.reply_photo(URANUS)
        Uranus = ephem.Uranus(now)
        planet_now = ephem.constellation(Uranus)
        update.message.reply_text(f'Сегодня планета "{get_planet[1]}" находится в созвездии: {planet_now[1]}')
    elif get_planet[1] == "Saturn":
        update.message.reply_photo(SATURN)
        Saturn = ephem.Saturn(now)
        planet_now = ephem.constellation(Saturn)
        update.message.reply_text(f'Сегодня планета "{get_planet[1]}" находится в созвездии: {planet_now[1]}')
    elif get_planet[1] == "Jupiter":
        update.message.reply_photo(JUPITER)
        Jupiter = ephem.Jupiter(now)
        planet_now = ephem.constellation(Jupiter)
        update.message.reply_text(f'Сегодня планета "{get_planet[1]}" находится в созвездии: {planet_now[1]}')
    elif get_planet[1] == "Venus":
        update.message.reply_photo(VENUS)
        Venus = ephem.Venus(now)
        planet_now = ephem.constellation(Venus)
        update.message.reply_text(f'Сегодня планета "{get_planet[1]}" находится в созвездии: {planet_now[1]}')
    elif get_planet[1] == "Mercury":
        update.message.reply_photo(MERCURY)
        Mercury = ephem.Mercury(now)
        planet_now = ephem.constellation(Mercury)
        update.message.reply_text(f'Сегодня планета "{get_planet[1]}" находится в созвездии: {planet_now[1]}')
    else:
        update.message.reply_text('Упс, чтото пошло не так и мы отклонились от курса')
        update.message.reply_photo(NOT_Plan)


def main():
    mybot = Updater(API_KEY, use_context=True)
    dp = mybot.dispatcher

    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    # dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()



if __name__ == '__main__':
    main()
