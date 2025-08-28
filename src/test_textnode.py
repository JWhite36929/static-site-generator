import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_no_url(self):
        node = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node.url, None)

    def test_diff(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node_italic = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node_italic)

    def test_diff_text(self):
        node = TextNode("This is text", TextType.LINK, "https://omarchy.org")
        node2 = TextNode("this is a link", TextType.LINK, "https://omarchy.org")
        self.assertNotEqual(node, node2)






if __name__ == "__main__":
    unittest.main()
