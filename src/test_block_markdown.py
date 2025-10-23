from textnode import TextNode, TextType
from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    BlockType,
)
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
    
    def test_block_to_block_type(self):
        self.assertEqual(
            block_to_block_type("# This is a heading"),
            BlockType.HEADING,
        )
        self.assertEqual(
            block_to_block_type("```python\nprint('Hello World')\n```"),
            BlockType.CODE,
        )
        self.assertEqual(
            block_to_block_type("> This is a quote"),
            BlockType.QUOTE,
        )
        self.assertEqual(
            block_to_block_type("- This is an unordered list item"),
            BlockType.UNORDERED_LIST,
        )
        self.assertEqual(
            block_to_block_type("1. This is an ordered list item"),
            BlockType.ORDERED_LIST,
        )
        self.assertEqual(
            block_to_block_type("This is a regular paragraph."),
            BlockType.PARAGRAPH,
        )