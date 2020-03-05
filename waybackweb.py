from datetime import datetime


class WrongArticleDateInputException(Exception):
    def __init__(self, msg=None, datetype=str):
        if msg is None:
            msg = f"The date provided must be a datetime object, not a {datetype}"
        super(WrongArticleDateInputException, self).__init__(msg)


class WrongURLFormatInputException(Exception):
    def __init__(self, msg=None, url="No Url"):
        if msg is None:
            msg = f"The URL {url} is in the wrong format. Must be one of http[s]://sub.example.com"
        super(WrongURLFormatInputException, self).__init__(msg)


class WayBackWebEntry(object):
    url = ""
    article_date_string = ""
    available = False
    _datetype = None

    def __init__(self, url, article_date):
        self.url = url
        if not isinstance(article_date, datetime):
            raise WrongArticleDateInputException(None, type(article_date))

        if not url[:7] == "http://" and not url[:8] == "https://":
            raise WrongURLFormatInputException(None, url)

    def __str__(self):
        return self.url


