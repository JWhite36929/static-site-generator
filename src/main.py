from textnode import TextNode, TextType
from page_generator import generate_pages_recursive
import sys

# prepare for github pages get the sys.argv inputs
def main():
    base_path = ""

    if len(sys.argv) > 1:
        base_path = sys.argv[1]

    generate_pages_recursive("content", "template.html", "docs", base_path)

if __name__ == "__main__":
    main()