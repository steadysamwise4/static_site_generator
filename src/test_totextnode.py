import unittest

from textnode import TextNode, TextType
from markdown_utils import text_to_textnodes

class TestToTextnode(unittest.TestCase):
  def test_text_to_textnodes_basic(self):
    text = 'This is **text** with an _italic_ word ' \
           'and a `code block` and an ' \
           '![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) ' \
           'and a [link](https://boot.dev)'
    new_nodes = text_to_textnodes(text)
    self.assertListEqual(
      [
        TextNode("This is ", TextType.PLAIN_TEXT),
        TextNode("text", TextType.BOLD_TEXT),
        TextNode(" with an ", TextType.PLAIN_TEXT),
        TextNode("italic", TextType.ITALIC_TEXT),
        TextNode(" word and a ", TextType.PLAIN_TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" and an ", TextType.PLAIN_TEXT),
        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.PLAIN_TEXT),
        TextNode("link", TextType.LINK, "https://boot.dev"),
      ],
      new_nodes
    )

  def test_text_to_textnodes_error(self):
    text = 'This is **text with an _italic_ word ' \
           'and a `code block` and an ' \
           '![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) ' \
           'and a [link](https://boot.dev)'
    self.assertRaises(Exception, text_to_textnodes, text)

  def test_text_to_textnodes_just_text(self):
    text = 'This is text with an italic word ' \
           'and a code block and an ' \
           'obi wan image with a url of https://i.imgur.com/fJRm4Vk.jpeg ' \
           'and a link a url of https://boot.dev'
    new_nodes = text_to_textnodes(text)
    # print('new_nodes:', new_nodes)
    self.assertListEqual(
      [
        TextNode(text, TextType.PLAIN_TEXT),
      ],
      new_nodes
    )

  def test_text_to_textnodes_single_link(self):
    text = 'This is text with an italic word ' \
           'and a code block and an ' \
           'obi wan image with a url of https://i.imgur.com/fJRm4Vk.jpeg ' \
           'and a [link](https://boot.dev)'
    new_nodes = text_to_textnodes(text)
    # print('new_nodes:', new_nodes)
    self.assertListEqual(
      [
        TextNode('This is text with an italic word ' \
           'and a code block and an ' \
           'obi wan image with a url of https://i.imgur.com/fJRm4Vk.jpeg ' \
           'and a ', TextType.PLAIN_TEXT),
        TextNode("link", TextType.LINK, "https://boot.dev"),
      ],
      new_nodes
    )