class Language:
    ENGLISH = "en"
    RUSSIAN = "ru"

    def echo_start(self, language, username):
        """Text to show when the /start is called"""

        if language == self.RUSSIAN:
            message = f'Привет, {username}! С помощью этого бота ты можешь получить ' \
                      f'свежие новости по интересующему тебя запросу. Просто введи пару слов для ' \
                      f'поиска, и я сразу же отправлю тебе результат!'
        else:
            message = f'Hi, {username}! Using this bot you can get latest news ' \
                      f'on a topic of your interest. Just type a few words for search ' \
                      f'and I will immediately send you the result!'
        return message

    def echo_404(self, language):
        """Text to show when the API request caused error"""

        if language == self.RUSSIAN:
            message = f'Ой! Что-то пошло не так. Стоит попробовать ещё раз!'
        else:
            message = f'Oops! Something went wrong. Try again!'
        return message

    def echo_nothing_found(self, language):
        """Text to show when no news were found"""

        if language == self.RUSSIAN:
            message = f'К сожалению, я не нашёл ничего по данному запросу. Прощу прощения!'
        else:
            message = f'Unfortunately, I have not found any information about this. Sorry!'
        return message

    def echo_help(self, language):
        """Text to show when /help is called"""

        if language == self.RUSSIAN:
            message = f'Для того чтобы получить новости по интересующей теме необходимо ' \
                      f'просто ввести несколько слов для поиска! Результат будет сразу же показан.'
        else:
            message = f'To get the news you are interested in just type a couple of key words' \
                      f'for search. The result will be shown to you as soon as it arrives.'
        return message

