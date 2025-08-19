import unittest

from textnode import TextNode, TextType
from utils import split_nodes_delimiter


class TestUtils(unittest.TestCase):
  def test_split_nodes_delimiter_code(self):
    node = TextNode("This is text with a `code block` word", TextType.PLAIN_TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    self.assertEqual(new_nodes, [
        TextNode("This is text with a ", TextType.PLAIN_TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" word", TextType.PLAIN_TEXT),
      ])
    
  def test_split_nodes_delimiter_italic(self):
    node = TextNode("This is text with a _italic_ word", TextType.PLAIN_TEXT)
    new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)
    self.assertEqual(new_nodes, [
        TextNode("This is text with a ", TextType.PLAIN_TEXT),
        TextNode("italic", TextType.ITALIC_TEXT),
        TextNode(" word", TextType.PLAIN_TEXT),
      ])
    
  def test_split_nodes_delimiter_bold(self):
    node = TextNode("This is text with a **bold** word", TextType.PLAIN_TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
    self.assertEqual(new_nodes, [
        TextNode("This is text with a ", TextType.PLAIN_TEXT),
        TextNode("bold", TextType.BOLD_TEXT),
        TextNode(" word", TextType.PLAIN_TEXT),
      ])
    
  def test_split_nodes_delimiter_multiple(self):
    node = TextNode("This is **text** with two **bold** words", TextType.PLAIN_TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
    self.assertEqual(new_nodes, [
        TextNode("This is ", TextType.PLAIN_TEXT),
        TextNode("text", TextType.BOLD_TEXT),
        TextNode(" with two ", TextType.PLAIN_TEXT),
        TextNode("bold", TextType.BOLD_TEXT),
        TextNode(" words", TextType.PLAIN_TEXT),
      ])
    
  def test_split_nodes_delimiter_first(self):
    node = TextNode("**This** is text with a **bold** word", TextType.PLAIN_TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
    self.assertEqual(new_nodes, [
        TextNode("This", TextType.BOLD_TEXT),
        TextNode(" is text with a ", TextType.PLAIN_TEXT),
        TextNode("bold", TextType.BOLD_TEXT),
        TextNode(" word", TextType.PLAIN_TEXT),
      ])
    
  def test_split_nodes_delimiter_first_and_last(self):
    node = TextNode("**This** is text with a bold **word**", TextType.PLAIN_TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
    self.assertEqual(new_nodes, [
        TextNode("This", TextType.BOLD_TEXT),
        TextNode(" is text with a bold ", TextType.PLAIN_TEXT),
        TextNode("word", TextType.BOLD_TEXT),
      ])
    
  def test_split_nodes_delimiter_two_consecutive(self):
    node = TextNode("**This** **is** text with a bold **word**", TextType.PLAIN_TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
    self.assertEqual(new_nodes, [
        TextNode("This", TextType.BOLD_TEXT),
        TextNode("is", TextType.BOLD_TEXT),
        TextNode(" text with a bold ", TextType.PLAIN_TEXT),
        TextNode("word", TextType.BOLD_TEXT),
      ])
  
  def test_split_nodes_delimiter_none(self):
    node = TextNode("This is text with no affected words", TextType.PLAIN_TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
    self.assertEqual(new_nodes, [
        TextNode("This is text with no affected words", TextType.PLAIN_TEXT),
      ])
    
  def test_split_nodes_delimiter_input_list(self):
    node_list = [
      TextNode("This is text with an ", TextType.PLAIN_TEXT),
      TextNode("italic", TextType.ITALIC_TEXT),
      TextNode(" and a **bold** word", TextType.PLAIN_TEXT)
    ] 
    new_nodes = split_nodes_delimiter(node_list, "**", TextType.BOLD_TEXT)
    self.assertEqual(new_nodes, [
      TextNode("This is text with an ", TextType.PLAIN_TEXT),
      TextNode("italic", TextType.ITALIC_TEXT),
      TextNode(" and a ", TextType.PLAIN_TEXT),
      TextNode("bold", TextType.BOLD_TEXT),
      TextNode(" word", TextType.PLAIN_TEXT)
      ])
    
  def test_split_nodes_delimiter_invalid_markdown(self):
    node = TextNode("This is text with **invalid markdown", TextType.PLAIN_TEXT)
    self.assertRaises(Exception, split_nodes_delimiter, [node], "**", TextType.BOLD_TEXT)

  def test_split_nodes_delimiter_single_delimited_word(self):
    node = TextNode("`code`", TextType.PLAIN_TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    self.assertEqual(new_nodes, [
        TextNode("code", TextType.CODE),
      ])