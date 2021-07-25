from urllib import request, error
from re import findall


def download_page(url: str, user_agent='wswp', num_retries=3, charset='utf-8'):
    print('\nDownloading:', url)
    reqst = request.Request(url)
    reqst.add_header('User-agent', user_agent)
    try:
        resp = request.urlopen(reqst)
        cs = resp.header.get_content_charset()
        if not cs:
            cs = charset
        html = resp.read().decode(cs)
    except (error.URLError, error.HTTPError, error.ContentTooShortError) as erro:
        print('Download error:', erro.reason)
        html = None
        if num_retries > 0:
            if hasattr(erro, 'code') and 500 <= erro.code < 600:
                return download_page(url, num_retries-1)
    return html


def crawl_sitemap(url: str):
    sitemap = download_page(url)
    links = findall('<loc>(.*?)</loc>', sitemap)
    for link in links:
        html = download_page(link)


if __name__ == '__main__':
    download_page('https://artesgc.home.blog')
