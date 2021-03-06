from urllib import request, error
from re import findall


def download_page(_url: str, _user_agent='wswp', _num_retries=3, _charset='utf-8'):
    print('\nDownloading:', _url)
    reqst = request.Request(_url)
    reqst.add_header('User-agent', _user_agent)
    try:
        resp = request.urlopen(reqst)
        cs = resp.header.get_content_charset()
        if not cs:
            cs = _charset
        html = resp.read().decode(cs)
    except (error.URLError, error.HTTPError, error.ContentTooShortError) as erro:
        print('Download error:', erro.reason)
        html = None
        if _num_retries > 0:
            if hasattr(erro, 'code') and 500 <= erro.code < 600:
                return download_page(_url, _num_retries-1)
    return html


def crawl_sitemap(_url: str):
    sitemap = download_page(_url)
    links = findall('<loc>(.*?)</loc>', sitemap)
    for link in links:
        html = download_page(link)


if __name__ == '__main__':
    url = input('Digite aqui o endereço do site:\n> ')
    download_page(_url=url)
