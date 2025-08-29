import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        props1 = {
            "href": "https://google.com",
            "target": "_blank"
                  }
        node1 = HTMLNode("a", "GOOGLE.COM", None, props1)
        self.assertEqual(node1.props_to_html(), 'href="https://google.com" target="_blank"')

    def test_props_empty(self):
        node1 = HTMLNode("p", "text in a paragraph", None, {})
        self.assertEqual(node1.props_to_html(), "")

    def test_props_none(self):
        node = HTMLNode("div", "hello", None, None)
        self.assertEqual(node.props_to_html(), "")


