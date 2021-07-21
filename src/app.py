import multiprocessing as mp
import re
import click
import requests
from bs4 import BeautifulSoup

# main entry point/command
@click.command()
@click.argument('url')
@click.option('--depth', default=3, help='Depth of pages to follow from the initial url passed.')
def cli(url, depth):
    pool = mp.Pool(mp.cpu_count())
    parse_urls([url], depth, pool)
    pool.close()

# Parse one URL
def parse_url(url):
    click.echo(f"Crawling: {url}")
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    attrs = {
        # fetch absolute urls only
        # also, we probably only want to follow html files?
        'href': re.compile(r'^http(s)?://')
    }

    # Use BeautifulSoup to find all of the anchor tags
    pages_found = soup.find_all('a', attrs=attrs,)

    # store all of the pages in this list
    pages = []

    # loop through the pages and add the URLs/hrefs to the pages list
    for page in pages_found:
        pages.append(page.get('href'))

    return pages


# Parse and array/list of URLs (and pass the depth and pool)
# remaining_depth starts as the initial desired depth and then is decrimented as it traverses throught pages.
def parse_urls(urls, remaining_depth, pool):
    # once we've got to the max depth desired, we're done
    if remaining_depth <= 0:
        # output with this thread is done
        # click.echo("<< done >>")
        return

    # process more urls and return an list of url lists/groups of url arrays
    grouped_urls = pool.map(parse_url, urls)

    # decrement the remaining depth
    remaining_depth-=1

    # loop the grouped urls, output the urls, and recursively call parse_urls to traverse more pages/urls
    for group in grouped_urls:
        for url_found in group:
            click.echo(f"\t{url_found}")
        # click.echo(f"Remaining depth: {remaining_depth}")
        parse_urls(urls=group, remaining_depth=remaining_depth, pool=pool)


