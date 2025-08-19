import unittest

from textnode import TextNode, TextType
from utils import extract_markdown_images, extract_markdown_links

class TestMarkdown(unittest.TestCase):
  def test_extract_markdown_images(self):
    matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

  def test_extract_markdown_images_with_both(self):
    matches = extract_markdown_images(
        "This is text with a link [to boot dev](https://www.boot.dev) and ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

  def test_extract_markdown_images_with_none(self):
    matches = extract_markdown_images(
        "This is text with only text"
    )
    self.assertListEqual([], matches)

  def test_extract_markdown_links(self):
    matches = extract_markdown_links(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    )
    self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

  def test_extract_markdown_links_with_both(self):
    matches = extract_markdown_links(
        "This is text with a link [to boot dev](https://www.boot.dev) and ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)

  def test_extract_markdown_links_with_none(self):
    matches = extract_markdown_links(
        "This is text with only text"
    )
    self.assertListEqual([], matches)