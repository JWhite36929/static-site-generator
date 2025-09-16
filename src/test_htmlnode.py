import unittest

from htmlnode import HTMLNode, LeafNode

class TestHtmlNode(unittest.TestCase):
    
    def test_values(self):
            node = HTMLNode(
                "div",
                "I wish I could read",
            )
            self.assertEqual(
                node.tag,
                "div",
            )
            self.assertEqual(
                node.value,
                "I wish I could read",
            )
            self.assertEqual(
                node.children,
                None,
            )
            self.assertEqual(
                node.props,
                None,
            )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    def test_props_to_html(self):
        props1 = {
            "href": "https://google.com",
            "target": "_blank"
                  }
        node1 = HTMLNode("a", "GOOGLE.COM", None, props1)
        self.assertEqual(node1.props_to_html(), ' href="https://google.com" target="_blank"')

    def test_props_empty(self):
        node1 = HTMLNode("p", "text in a paragraph", None, {})
        self.assertEqual(node1.props_to_html(), "")

    def test_props_none(self):
        node = HTMLNode("div", "hello", None, None)
        self.assertEqual(node.props_to_html(), "")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    
