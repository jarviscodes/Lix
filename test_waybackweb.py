import pytest

from datetime import datetime
from waybackweb import WayBackWebEntry, WrongURLFormatInputException, WrongArticleDateInputException

datestring = "12/07/2019"
faulty_url = "hln.be"


def test_new_wbe_object_date_type():
    with pytest.raises(WrongArticleDateInputException) as excep:
        WayBackWebEntry(article_date=datestring, url=faulty_url)
    assert "<class 'str'>" in str(excep.value)


def test_new_wbe_object_wrong_url():
    dto = datetime.strptime(datestring, "%d/%m/%Y")
    with pytest.raises(WrongURLFormatInputException) as excep:
        WayBackWebEntry(article_date=dto, url=faulty_url)
    assert "The URL hln.be is in the wrong format. Must be one of http[s]://sub.example.com" == str(excep.value)
