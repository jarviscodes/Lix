import requests
import json
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


class WaybackRequestError(Exception):
    def __init__(self, msg=None):
        if msg is None:
            msg = "We couldnt connect to wayback. Check your internet, DNS, and the status of archive.org"
        super(WaybackRequestError, self).__init__(msg)


class WayBackWebEntry(object):
    url = ""
    available = False
    request_date = None
    snapshots = {}

    def __init__(self, url, article_date):
        if not isinstance(article_date, datetime):
            raise WrongArticleDateInputException(None, type(article_date))
        self.request_date = article_date

        if not url[:7] == "http://" and not url[:8] == "https://":
            raise WrongURLFormatInputException(None, url)
        self.url = url

        self.snapshots = self._get_snapshots_from_wayback()

    def __str__(self):
        return self.url

    def _get_snapshots_from_wayback(self):
        try:
            with requests.Session() as _sess:
                resp = _sess.get(self._wayback_request_url)
                json_string = resp.text
            json_obj = json.loads(json_string)
            snapshots = json_obj['archived_snapshots']
            return snapshots
        except requests.RequestException:
            raise WaybackRequestError

    @property
    def _wayback_request_url(self):
        wb_req_url = f"https://archive.org/wayback/available?url={self.url}&timestamp={self.date_as_wb_timestamp}"
        return wb_req_url

    @property
    def date_as_wb_timestamp(self):
        wb_timestamp = self.request_date.strftime("%Y%m%d")
        return wb_timestamp

    @property
    def has_snapshots(self):
        return len(self.snapshots) > 0
