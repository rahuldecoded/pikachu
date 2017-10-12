import requests

wiki_summary_url = 'https://en.wikipedia.org/api/rest_v1/page/summary/{term}'


def summary(term):
    return '{term}: {description}'.format(
        term=term,
        description=fetch_summary(term).get('description', 'Not found'))


def fetch_summary(term):
    res = requests.get(wiki_summary_url.format(term=term))
    return res.json()
