from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    
    def __init__(self, text: str, text_type: TextType, url: str=None):
        if not isinstance(text_type, TextType):
            raise ValueError(f"text_type must be a TextType enum, got {type(text_type)}")
        
        if text_type in (TextType.LINK, TextType.IMAGE) and not url:
            raise ValueError(f"url is required for {text_type.value}")

        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text 
            and self.text_type == other.text_type 
            and self.url == other.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.TextType == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.TextType == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.TextType == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.TextType == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.TextType == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.TextType == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError("Not a valid TextType")

