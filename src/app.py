import click
import multiprocessing as mp
from src.utils.parse import parse_html
from src.utils.fetch import fetch_url

# main entry point/command
@click.command()
@click.argument('url')
@click.option('--depth', default=3, help='Depth of pages to follow from the initial url passed.')
def cli(url: str, depth: int):
    pool = mp.Pool(mp.cpu_count())
    parse_urls([url], depth, pool)
    pool.close()

# Parse one URL
def parse_url(url: str):
    html_text = fetch_url(url)
    pages_found= parse_html(html_text)

    # store all of the pages in this list
    pages = []

    # loop through the pages and add the URLs/hrefs to the pages list
    for page in pages_found:
        pages.append(page.get('href'))

    return url,pages


# Parse and array/list of URLs (and pass the depth and pool)
# remaining_depth starts as the initial desired depth and then is decrimented as it traverses throught pages.
def parse_urls(urls: list, remaining_depth:int, pool: mp.Pool):
    # once we've got to the max depth desired, we're done
    if remaining_depth <= 0:
        # output with this thread is done
        return

    # process more urls and return an list of url lists/groups of url arrays
    grouped_urls:tuple[str, list] = pool.map(parse_url, urls)

    # decrement the remaining depth
    remaining_depth-=1

    # loop the grouped urls, output the urls, and recursively call parse_urls to traverse more pages/urls
    for url,group in grouped_urls:
        click.echo(f"Crawled: {url}")
        for url_found in group:
            click.echo(f"\t{url_found}")
        parse_urls(urls=group, remaining_depth=remaining_depth, pool=pool)


