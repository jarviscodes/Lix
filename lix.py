import ssl
import requests
from collections import namedtuple
from bs4 import BeautifulSoup
import urllib


# requests stuff
root_url = "https://pybit.es/pages/articles.html"
ua_string = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"
base_header = {'User-Agent': ua_string}

# Create namedtuple
ArtLink = namedtuple("ArtLink", "title link")
artlink_list = []


def get_article_list():
    with requests.Session() as _sess:
        articles_resp = _sess.get(root_url, headers=base_header)
        articles_page_text = articles_resp.text
        articles_soup = BeautifulSoup(articles_page_text, 'html.parser')
        articles_ul = articles_soup.find("ul", {"id": "articleList"})
        all_arts_raw = articles_ul.find_all("a")
        for anchor in all_arts_raw:
            tmp_al = ArtLink(anchor.text, anchor['href'])
            artlink_list.append(tmp_al)
        return artlink_list


def get_post_content(artlink: ArtLink):
    with requests.Session() as _sess:
        article_content_resp = _sess.get(artlink.link, headers=base_header)
        article_text = article_content_resp.text
        soup = BeautifulSoup(article_text, 'html.parser')
        article_block = soup.find('article', {'class': 'single'})
        return article_block


def get_all_links(article_block):
    all_links_hreflist = []
    abs_links_hreflist = []
    all_links = article_block.find_all("a")
    try:
        [all_links_hreflist.append(linkhref['href']) for linkhref in all_links if linkhref['href'] is not None]
    except KeyError as ke:
        pass

    # We will ignore relative links for now.
    [abs_links_hreflist.append(al) for al in all_links_hreflist if al[:4] == "http"]

    return abs_links_hreflist


def test_single_link(link):
    with requests.Session() as _sess:
        try:
            resp = _sess.get(link, headers=base_header)
            if resp.status_code != 200:
                print(f"\t ==> No 200 for {link}, instead got {resp.status_code}")
        except requests.exceptions.SSLError as ex:
            print(f"\t ==> SSL Error for {link}")
        except requests.exceptions.InvalidURL as ex:
            print(f"\t ==> {link} is not a valid URL, Skipping (Probably URL Example)")



all_artlinks = get_article_list()
for alitm in all_artlinks:
    print(f"Running article: {alitm.title}")
    artBlock = get_post_content(alitm)
    all_links = get_all_links(artBlock)
    for link in all_links:
        test_single_link(link)

