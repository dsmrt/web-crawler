# Web Crawler

## Setup and Build
- Clone the repo: `git clone git@github.com:dsmrt/web-crawler.git`
- Change directories into the repository (`cd web-crawler`)
- Initiate venv (on mac osx `python3 -m venv .`)
- Activate venv (on mac osx `source ./bin/activate`)
- Build using `make build`

## Usage/Run 
- Basic usage: `./bin/web-crawler [OPTIONS] URL`
- Example: `./bin/web-crawler https://www.dsmrt.com` or `./bin/web-crawler https://www.dsmrt.com --depth=2`
- For more information, see help: `./bin/web-crawler --help`

## Deactivate VENV
- Run `deactivate`
