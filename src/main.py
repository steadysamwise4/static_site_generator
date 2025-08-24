import os
import shutil
from textnode import *

from copystatic import copy_static

def main():
  # new_text_node = TextNode("This is some anchor text", TextType.LINK, "https://boot.dev")
  # print(new_text_node)
  dir_path_static = "./static"
  dir_path_public = "./public"
  # 1. Remove everything currently in the destination directory (dst)
  if os.path.exists(dir_path_public):
      shutil.rmtree(dir_path_public)
      print(f"Contents of {dir_path_public} removed.")

  copy_static("static", dir_path_public)

main()