import pytest

from datetime import datetime
from waybackweb import WayBackWebEntry, WrongURLFormatInputException, WrongArticleDateInputException

datestring = "12/07/2019"
other_datestring = "07/12/2019"
faulty_url = "example.com"
good_https_url = "https://example.com"
good_http_url = "http://example.com"


def test_new_wbe_object_date_type():
    with pytest.raises(WrongArticleDateInputException) as excep:
        WayBackWebEntry(article_date=datestring, url=faulty_url)
    assert "<class 'str'>" in str(excep.value)


def test_new_wbe_object_wrong_url():
    dto = datetime.strptime(datestring, "%d/%m/%Y")
    with pytest.raises(WrongURLFormatInputException) as excep:
        WayBackWebEntry(article_date=dto, url=faulty_url)
    assert f"The URL {faulty_url} is in the wrong format. Must be one of http[s]://sub.example.com" == str(excep.value)


def test_date_to_wbtimestamp():
    dto = datetime.strptime(datestring, "%d/%m/%Y")
    test_obj = WayBackWebEntry(url=good_http_url, article_date=dto)
    assert test_obj.date_as_wb_timestamp == "20190712"

    # We should be able to change the date.
    test_obj.request_date = datetime.strptime(other_datestring, "%d/%m/%Y")
    assert test_obj.date_as_wb_timestamp == "20191207"
