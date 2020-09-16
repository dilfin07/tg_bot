import logging, ephem, datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from setting import API_KEY, planet_img, NOT_Plan

now = datetime.datetime.now()
logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context):
    print('Вызван /start')
    print(update.message.text.split())
    update.message.reply_text('Привет! На какую планету отправимся?)')
    update.message.reply_photo(planet_img['system_img'])
    update.message.reply_text('Чтобы отправится к нужной планете просто используй конду /planet [planet] например  '
                              '/planet Venus')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def planet(update, context):
    get_planet = update.message.text.split()
    #print(get_planet)
    planet_atr = getattr(ephem, get_planet[1], None)
    if planet_atr is not None:
        update.message.reply_photo(planet_img[get_planet[1]])
        planet_now = getattr(ephem, get_planet[1])
        pl_now = ephem.constellation(planet_now(now))
        update.message.reply_text(f'Сегодня планета "{get_planet[1]}" находится в созвездии: {pl_now[1]}')
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
