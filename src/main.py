from textnode import TextNode 
from textnode import TextType

def main():
    example1 = TextNode("Hello", TextType.BOLD, "https://omarchy.org")
    example2 = TextNode("oops", TextType.ITALIC)

    print(example2)
    print(example1)


if __name__ == "__main__":
    main()
