from enum import Enum
import re
"""
Block markdown will refer to blocks of text separated by newlines

ex:
# This is a heading

This is a paragraph with **bolded text**

- This is a list item
- Another list item


This would be rendered as 3 blocks : a heading block, a paragraph block, and a list block.
"""

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    """
    It takes a raw Markdown string (representing a full document) as input and returns a list of "block" strings. The example above would be split into three strings
    """
    blocks = []
    current_block = []
    lines = markdown.splitlines()

    for line in lines:
        if line.strip() == "":
            if current_block:
                blocks.append("\n".join(current_block).strip())
                current_block = []
        else:
            current_block.append(line)

    if current_block:
        blocks.append("\n".join(current_block).strip())

    return blocks

def block_to_block_type(block):
    """
    Given a block of markdown text, determine its BlockType
    """
    heading_pattern = r'^\s*#{1,6}\s+'
    code_pattern = r'^\s*```'
    quote_pattern = r'^\s*>\s+'
    unordered_list_pattern = r'^\s*[-*+]\s+'
    ordered_list_pattern = r'^\s*\d+\.\s+'

    if re.match(heading_pattern, block):
        return BlockType.HEADING
    elif re.match(code_pattern, block):
        return BlockType.CODE
    elif re.match(quote_pattern, block):    
        return BlockType.QUOTE
    elif re.match(unordered_list_pattern, block):
        return BlockType.UNORDERED_LIST
    elif re.match(ordered_list_pattern, block):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH




    