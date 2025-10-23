from textnode import TextNode, TextType
from copystatic import copy_files_from_to

def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

    copy_files_from_to("static", "public")


if __name__ == "__main__":
    main()