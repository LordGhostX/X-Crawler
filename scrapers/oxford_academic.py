"""
arachne_lite scrapes Oxford Academic search results
and returns a list of dictionaries
encoded in a json file. The dictionaries contain keys -
author, research_link, research_title, abstract
"""
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin
import time
import json
import logging

from bs4 import BeautifulSoup

import colorer


formatter = '[%(asctime)s] %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO,
                    format=formatter,
                    datefmt='%d-%m-%Y %H:%M:%S')


def get_page(url):
    url = ''.join([char for char in url if not char.isspace()])
    try:
        req = Request(
            url,
            data=None,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
                ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142'
                ' Safari/537.36'
            }
        )
        page = urlopen(req)
    except URLError:
        logging.error(f'URL not found: {url}')
        raise URLError('')
    except HTTPError:
        logging.error(f'Page not found: {url}')
        raise HTTPError('')
    return BeautifulSoup(page, 'html.parser')


class SearchTerm:

    def __init__(self):
        self.terms = []

    def input_terms(self, *args):
        for term in args:
            term = "%20".join(term.split())
            self.terms.append(term)

    def __getitem__(self, i):
        while i < len(self.terms):
            return self.terms[i]
        else:
            raise IndexError('Index out of range')


class OxfordAcademicCrawler:

    def __init__(self, search_terms: SearchTerm, limit=None):
        """
        :param search_terms: a list of search terms
        :param limit: an int that holds the amount of wanted results
        """

        try:
            with open('found_articles.json', 'r') as fp:
                found = json.loads(fp.read())
        except FileNotFoundError:
            found = []

        self.domain = 'https://academic.oup.com/'
        self.base_search = 'https://academic.oup.com/journals/' +\
            'search-results?q='
        self.search_terms = search_terms.terms
        self.found_articles = found
        self.limit = limit

    def crawl(self):
        self.parse_search()
        return self.found_articles

    def parse_search(self):
        for term in self.search_terms:
            url = self.base_search + term
            try:
                search_page = get_page(url)
            except (URLError, HTTPError):
                continue

            if search_page is None:
                continue

            logging.info(f'Currently on search page: {url}')
            self.parse_page(search_page)
            next_page = search_page.find('a', {'id': 'pagination-next'})

            while next_page:
                if self.limit and len(self.found_articles) >= self.limit:
                    return
                url = 'https://academic.oup.com/journals/search-results?' +\
                    next_page['data-url']

                try:
                    search_page = get_page(url)
                except (URLError, HTTPError):
                    break

                logging.info(f'Currently on search page: {url}')
                self.parse_page(search_page)
                next_page = search_page.find('a', {'id': 'pagination-next'})

    def parse_page(self, page: BeautifulSoup):

        if self.limit and len(self.found_articles) >= self.limit:
            return

        articles = page.find_all(
            'div',
            {
                'class': ['sr-list', 'al-article-box']
            }
        )

        if not articles:
            logging.info('What you searched for does not exist.')
            return

        for article in articles:
            time.sleep(2)

            rel_link = article.find('a', {'class': 'article-link'})['href']
            title = article.find('h4', {'class': 'al-title'}).text.strip()
            abstractTag = article.find('div', {'class': 'snippet'})
            abstract = abstractTag.text.strip() if abstractTag else ''
            authors = [name.text for name in article
                       .find_all('a', {'class': 'author-link'})]

            article = {
                    'author': " ".join(authors),

                    'research_link': urljoin(self.domain, rel_link),

                    'research_title': title,

                    'abstract': abstract
                }

            if article not in self.found_articles:
                self.found_articles.append(article)

            with open('found_articles.json', 'w') as fp:
                fp.write(json.dumps(self.found_articles, indent=2,
                                    sort_keys=True))

            logging.info(f'Added article: {title}')


if __name__ == '__main__':

    search_terms = SearchTerm()
    search_terms.input_terms('University of Lagos', 'Unilag')
    crawler = OxfordAcademicCrawler(search_terms=search_terms)
    articles = crawler.crawl()
