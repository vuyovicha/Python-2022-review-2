from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import web
import languages
import os


TOKEN = os.getenv('TOKEN')
HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')
PORT = int(os.environ.get('PORT', 8443))


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, context):
    """Command /start handler"""
    lang = update.message.from_user.language_code
    user = update.message.from_user.first_name
    message = Language.echo_start(language=lang, username=user)
    update.message.reply_text(message)


def help(update, context):
    """Command /help handler"""
    update.message.reply_text('Help!')


def respond(update, context):
    """Respond to the user's news request"""
    lang = update.message.from_user.language_code
    data_news, data_urls = web.get_news(update.message.text, lang)
    if not data_news:
        Language.echo_404(lang)
    elif len(data_news) == 0:
        Language.echo_nothing_found(lang)
    else:
        for i in range(len(data_news)):
            update.message.reply_text(f'{data_news[i]}\n\n{data_urls[i]}')


def error(update, context):
    """Log Errors caused by Updates"""
    Language.echo_404(update.message.from_user.language_code)
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot"""
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, respond))
    dp.add_error_handler(error)

    # updater.start_polling()
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com/'
    updater.bot.setWebhook(WEBHOOK_HOST + TOKEN)
    updater.idle()


Language = languages.Language()
main()

