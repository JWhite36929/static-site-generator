from textnode import TextNode, TextType
from block_markdown import markdown_to_blocks
import unittest

class TestBlockMarkdown(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_markdown_to_blocks_single(self):
        md = "This is a single paragraph with no newlines"
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a single paragraph with no newlines",
            ],
        )
    
    def test_markdown_to_blocks_empty(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [],
        )
    
    def test_markdown_to_blocks_multiple_newlines(self):
        md = """
This is a paragraph after


multiple newlines

This is another paragraph
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a paragraph after",
                "multiple newlines",
                "This is another paragraph",
            ],
        )

    def test_markdown_to_blocks_only_newlines(self):
        md = """
        
        
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [],
        )
    