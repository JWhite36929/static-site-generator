from enum import Enum
from htmlnode import LeafNode, ParentNode
from textnode import text_node_to_html_node, TextNode, TextType
from inline_markdown import text_to_textnodes
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


def markdown_to_html_node(markdown):

    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    
    if block_type == BlockType.UNORDERED_LIST:
        return unordered_list_to_html_node(block)
    
    if block_type == BlockType.ORDERED_LIST:
        return ordered_list_to_html_node(block)
    
    if block_type == BlockType.QUOTE:   
        return quote_to_html_node(block) 
    raise ValueError(f"Invalid block type")

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_children = []
    for text_node in text_nodes:
        html_children.append(text_node_to_html_node(text_node))
    return html_children

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level {level}")
    text = block[level+1:]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])

def ordered_list_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def unordered_list_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)