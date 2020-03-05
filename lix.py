import ssl
import requests
import click
from collections import namedtuple
from bs4 import BeautifulSoup
from HTTPResponses import response_code_dict
from styled_symbols import print_error, print_fallback, print_good, print_info, print_warning

import urllib


# requests stuff
root_url = "https://pybit.es/pages/articles.html"
ua_string = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"
base_header = {'User-Agent': ua_string}

# Create namedtuple
ArtLink = namedtuple("ArtLink", "title link")
artlink_list = []
ignorecodes = []


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
        # anchor doesnt have href so...
        pass

    # We will ignore relative links for now.
    [abs_links_hreflist.append(al) for al in all_links_hreflist if al[:4] == "http"]

    return abs_links_hreflist


def test_single_link(link):
    with requests.Session() as _sess:
        try:
            resp = _sess.get(link, headers=base_header)
            if resp.status_code in response_code_dict.keys() and resp.status_code not in ignorecodes:
                resp_style = response_code_dict[resp.status_code]
                click.secho(message=f"\t[{resp_style.label}] {link} => {resp_style.message}", fg=resp_style.color_name)
        except requests.exceptions.SSLError as ex:
            print_error(f"\tSSL Error for {link}")
        except requests.exceptions.InvalidURL as ex:
            print_error(f"\t{link} is not a valid URL, Skipping (Probably URL Example)")
        except OSError as ex:
            print_error(f"\t{link} threw an OSError, target server down? (Dead Link!)")
        except KeyboardInterrupt:
            print_info("Exiting because of CTRL+C!")
            exit()


@click.command()
@click.option("-i", "--ignore-code", "ignore", type=str)
def main(ignore):
    global ignorecodes
    if ignore is not None:
        if "," in ignore:
            [ignorecodes.append(int(code)) for code in ignore.split()]
        else:
            ignorecodes.append(int(ignore))
    all_artlinks = get_article_list()
    for article_link in all_artlinks:
        print_info(f"Article: {article_link.title}")
        art_block = get_post_content(article_link)
        all_links = get_all_links(art_block)
        for link in all_links:
            test_single_link(link)


if __name__ == '__main__':
    main()