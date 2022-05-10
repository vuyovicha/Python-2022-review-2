import json
import strings
import requests
import languages
import os

API_KEY = os.environ.get('API_KEY')


def get_news(keyword, language):
    """API call to Bing news service to get the news"""

    if not language == languages.Language.RUSSIAN:
        language = languages.Language.ENGLISH

    querystring = {"q": keyword, "count": strings.NEWS_COUNT, "sortBy": "Date", "setLang": language, "freshness": "Day", "textFormat": "Raw", "safeSearch": "Off"}

    headers = {
        "X-BingApis-SDK": "true",
        "Accept-Language": language,
        "X-RapidAPI-Host": strings.API_HOST,
        "X-RapidAPI-Key": API_KEY
    }

    response = requests.request("GET", strings.URL, headers=headers, params=querystring)

    if response.status_code == 200:
        data = json.loads(response.text)
        data_news = [i['name'] for i in data['value']]
        data_urls = [i['url'] for i in data['value']]
        return data_news, data_urls
    else:
        return False, False

