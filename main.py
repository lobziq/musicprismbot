from telegram.ext import Updater, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
from distributor import *
from config import *
import logging

updater = Updater(token=config.get('token'), request_kwargs={
    'proxy_url': config.get('proxy'),
    'urllib3_proxy_kwargs': {
        'username': config.get('proxy_username'),
        'password': config.get('proxy_password')}})
d = Distributor()
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def light_callback(bot, update):
    query = update.inline_query.query
    if not query:
        return

    title, results = d.get_results(query)
    answers = list()
    all_results = title + '\n' + '\n'.join(map(lambda result: result[1], results))

    answers.append(
        InlineQueryResultArticle(
            id=len(results),
            title='share all sources',
            input_message_content=InputTextMessageContent(all_results),
            disable_web_page_preview=True,
            description=title))

    for i, r in enumerate(results):
        answers.append(
            InlineQueryResultArticle(
                id=i,
                title=r[0],
                input_message_content=InputTextMessageContent(r[1]),
                disable_web_page_preview=True,
                description=r[1]))

    bot.answer_inline_query(update.inline_query.id, answers)


updater.dispatcher.add_handler(InlineQueryHandler(light_callback))
updater.start_polling()
