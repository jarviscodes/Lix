from datetime import datetime


class WrongArticleDateInputException(Exception):
    def __init__(self, msg=None, datetype=None):
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
    available = False
    request_date = None

    def __init__(self, url, article_date):
        if not isinstance(article_date, datetime):
            raise WrongArticleDateInputException(None, type(article_date))
        self.request_date = article_date

        if not url[:7] == "http://" and not url[:8] == "https://":
            raise WrongURLFormatInputException(None, url)
        self.url = url

    def __str__(self):
        return self.url

    # Recalculate when requested. Date might change!
    @property
    def date_as_wb_timestamp(self):
        wb_timestamp = self.request_date.strftime("%Y%m%d")
        return wb_timestamp


