import unittest

from textnode import TextNode, TextType
from markdown_utils import extract_markdown_images, extract_markdown_links, split_nodes

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

  def test_split_images(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.PLAIN_TEXT,
    )
    new_nodes = split_nodes([node], TextType.IMAGE, extract_markdown_images)
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.PLAIN_TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.PLAIN_TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )

  def test_split_link(self):
    node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.PLAIN_TEXT,
    )
    new_nodes = split_nodes([node], TextType.LINK, extract_markdown_links)
    self.assertListEqual(
        [
            TextNode("This is text with a link ", TextType.PLAIN_TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.PLAIN_TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ],
        new_nodes,
    )

  def test_split_text_with_both(self):
    node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and an image ![image](https://i.imgur.com/zjjcJKZ.png)",
        TextType.PLAIN_TEXT,
    )
    new_nodes = split_nodes([node], TextType.LINK, extract_markdown_links)
    new_nodes = split_nodes(new_nodes, TextType.IMAGE, extract_markdown_images)
    self.assertListEqual(
        [
            TextNode("This is text with a link ", TextType.PLAIN_TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and an image ", TextType.PLAIN_TEXT),
            TextNode(
                "image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"
            ),
        ],
        new_nodes,
    )

  def test_split_text_with_neither(self):
    node_list = [
      TextNode("This is text with an ", TextType.PLAIN_TEXT),
      TextNode("italic", TextType.ITALIC_TEXT),
      TextNode(" and a ", TextType.PLAIN_TEXT),
      TextNode("bold", TextType.BOLD_TEXT),
      TextNode(" word", TextType.PLAIN_TEXT)
      ]
    new_nodes = split_nodes(node_list, TextType.LINK, extract_markdown_links)
    new_nodes = split_nodes(new_nodes, TextType.IMAGE, extract_markdown_images)
    self.assertListEqual(
        node_list,
        new_nodes,
    )