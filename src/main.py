from textnode import *

def main():
  new_text_node = TextNode("This is some anchor text", TextType.LINK, "https://boot.dev")
  print(new_text_node)

main()