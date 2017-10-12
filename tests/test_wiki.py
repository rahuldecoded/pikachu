import unittest
from mock import Mock, patch

import wiki


class TestWiki(unittest.TestCase):
    def setUp(self):
        self.search_term = 'IRC'
        self.wiki_summary = {
            "title": "Internet Relay Chat",
            "displaytitle": "Internet Relay Chat",
            "pageid": 14730,
            "extract": "Internet Relay Chat (IRC) is an application layer protocol that facilitates communication in the form of text. The chat process works on a client/server networking model. IRC clients are computer programs that a user can install on their system. These clients communicate with chat servers to transfer messages to other clients. IRC is mainly designed for group communication in discussion forums, called channels, but also allows one-on-one communication via private messages as well as chat and data transfer, including file sharing.\nClient software is available for every major operating system that supports Internet access.",
            "extract_html": "<p><b>Internet Relay Chat</b> (<b>IRC</b>) is an application layer protocol that facilitates communication in the form of text. The chat process works on a client/server networking model. IRC clients are computer programs that a user can install on their system. These clients communicate with chat servers to transfer messages to other clients. IRC is mainly designed for group communication in discussion forums, called channels, but also allows one-on-one communication via private messages as well as chat and data transfer, including file sharing.</p>\n<p>Client software is available for every major operating system that supports Internet access.",
            "lang": "en",
            "dir": "ltr",
            "timestamp": "2017-10-11T02:02:27Z",
            "description": "protocol for real-time Internet chat and messaging"
        }

    def test_fetch_summary_return_summary_dict(self):
        self.maxDiff = None
        mock_get = Mock()
        mock_get.json = Mock(return_value=self.wiki_summary)
        with patch('requests.get', return_value=mock_get):
            self.assertEqual(wiki.fetch_summary(self.search_term), self.wiki_summary)

    def test_summary_return_description_field(self):
        mock_get = Mock()
        mock_get.json = Mock(return_value=self.wiki_summary)
        with patch('requests.get', return_value=mock_get):
            self.assertEqual(wiki.summary(self.search_term),
                             '{}: {}'.format(self.search_term, self.wiki_summary['description']))
