from django.shortcuts import render
from .common import config

import requests
import bs4

import logging
import re
import datetime
import csv
logging.basicConfig(level=logging.INFO)

from requests.exceptions import HTTPError
from urllib3.exceptions import MaxRetryError

logger = logging.getLogger(__name__)
is_well_formed_link = re.compile(r'^http?//.+/.+$')
is_root_path = re.compile(r'^/.+$')

# Create your views here.

class NewsPage:

    def __init__(self, news_site_uid, url):
        self._config = config()['news_sites'][news_site_uid]
        self._queries = self._config['queries']
        self._html = None

        self._visit(url)

    def _select(self, query_string):
        return self._html.select(query_string)

    def _visit(self, url):
        response = requests.get(url)
        response.raise_for_status()

        self._html = bs4.BeautifulSoup(response.text, 'html.parser')


class HomePage(NewsPage):

    def __init__(self, news_site_uid, url):
        super().__init__(news_site_uid, url)

    @property
    def article_links(self):
        link_list = []
        for link in self._select(self._queries['homepage_article_links']):
            if link and link.has_attr('href'):
                link_list.append(link)

        return set(link['href'] for link in link_list)


class ArticlePage(NewsPage):

    def __init__(self, news_site_uid, url):
        super().__init__(news_site_uid, url)

    @property
    def body(self):
        result = self._select(self._queries['article_body'])
        return result[0].text if len(result) else ''

    @property
    def title(self):
        result = self._select(self._queries['article_title'])
        return result[0].text if len(result) else ''


def _new_scraper (new_site_uid):
    host = config()['news_sites'][new_site_uid]['url']
    logging.info('esta escaneando {}'.format(host))
    homepage = HomePage(new_site_uid,host)
    articles = []
    for link in homepage.article_links:
        article = _fetch_article(new_site_uid,host,link)
        if article:
            logger.info('encontro el ariculo')
            articles.append(article)
            break
    _save_articles(new_site_uid,articles)

def _save_articles(new_site_uid,articles):
    now = datetime.datetime.now().strftime('%Y_%m_%d')
    out_file_name = '{}_{}_resultado.csv'.format(new_site_uid,now)
    csv_headers = list(filter(lambda property: not property.startswith('_'), dir(articles[0])))

    with open(out_file_name, mode='w+',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(csv_headers)

        for article in articles:
            row = [str(getattr(article,prop))for prop in csv_headers]
            writer.writerow(row)


def _fetch_article(new_site_uid, host, link):
    logger.info('iniciando busqueda del articulo'+ link)
    article = None
    try:
        article = ArticlePage(new_site_uid,_build_link(host,link))
    except (HTTPError,MaxRetryError) as e:
        logger.warning('Error encontrando el error',exc_info=False)
    if article and not article.body:
        logger.warning('articulo invalido no tiene cuerpo')
        return None
    return article
        
def _build_link(host,link):
    if is_well_formed_link.match(link):
        return link
    elif is_root_path.match(link):
        return '{}{}'.format(host,link)
    else:
        return '{}/{}'.format(host,link)



def AgregarL(request):
    if(request.GET.get('PrimerBoton')):
        encontro = False
        variable = request.GET.get('text')
        new_site_choices = list(config()['news_sites'].keys())
        for i in new_site_choices:
            if i == variable:
                encontro = True
                _new_scraper(variable)
                break
        mensaje = encontro
    return render(request,'PlatziData.html',{'sitios':new_site_choices,'mensaje':mensaje})

def PlatziData(request):
    new_site_choices = list(config()['news_sites'].keys())
    return render(request,'PlatziData.html',{'sitios':new_site_choices})