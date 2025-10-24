from textnode import TextNode, TextType
from page_generator import copy_files_from_to, generate_page, generate_pages_recursive

def main():
    print("welcome to the static site generator!")
 
    
    copy_files_from_to("static", "public")

    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()