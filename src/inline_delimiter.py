from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    #old_nodes is a list of nodes

    """
    returns a list of nodes where any text_type nodes are split
    into multiple nodes based on the syntax. 

    ex:
    node = TextNode("This is text with `code block` words", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

    new_nodes then becomes
    [
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" word", TextType.TEXT),
    ]
    """
    
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes
    
def extract_markdown_images(text):
    """
    returns a list of tuples (alt_text, url) for each markdown image in the text

    ex:
    text = "This is an image ![alt text](http://example.com/image.png) in the text"
    images = extract_markdown_images(text)

    images then becomes
    [("alt text", "http://example.com/image.png")]
    """
    pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    """
    returns a list of tuples (link_text, url) for each markdown link in the text

    ex:
    text = "This is a link [link text](http://example.com) in the text"
    links = extract_markdown_links(text)

    links then becomes
    [("link text", "http://example.com")]
    """
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    """
    returns a list of nodes where any text_type nodes are split into multiple nodes
    based on markdown image syntax. 
    
    ex:
    node = TextNode("This is an image ![alt text](http://example.com/image.png) in the text", TextType.TEXT)
    new_nodes = split_nodes_image([node])
    new_nodes then becomes
    
    [
        TextNode("This is an image ", TextType.TEXT),
        TextNode("alt text", TextType.IMAGE, "http://example.com/image.png"),
        TextNode(" in the text", TextType.TEXT),
    ]

    """
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections  = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    """
    returns a list of nodes where any text_type nodes are split into multiple nodes
    based on markdown link syntax.
    ex:
    node = TextNode("This is a link [link text](http://example.com) in the text", TextType.TEXT)
    new_nodes = split_nodes_link([node])
    new_nodes then becomes
    
    [
        TextNode("This is a link ", TextType.TEXT),
        TextNode("link text", TextType.LINK, "http://example.com"),
        TextNode(" in the text", TextType.TEXT),
    ]
    """
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes