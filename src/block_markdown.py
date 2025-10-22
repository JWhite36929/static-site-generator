"""
Block markdown will refer to blocks of text separated by newlines

ex:
# This is a heading

This is a paragraph with **bolded text**

- This is a list item
- Another list item


This would be rendered as 3 blocks : a heading block, a paragraph block, and a list block.
"""

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