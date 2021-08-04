import requests
import click
import time 

def fetch_url(url: str, max_retries: int = 5, wait_seconds: int = 3) -> str:

    html: str = None
    for i in range(max_retries):
        try:
            html = requests.get(url).text
        except:
            click.echo(f'An error occured. Try number {i}')
            time.sleep(wait_seconds)

    if html is None:
        raise Exception(f'Html was unable to fetch {url}')

    return html