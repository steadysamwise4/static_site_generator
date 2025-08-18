import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
  def test_leaf_to_html_p(self):
    node = LeafNode("p", "Hello, world!")
    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

  def test_leaf_to_html_a(self):
    node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

  def test_is_instance(self):
    node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    self.assertIsInstance(node, LeafNode, "Not an HTMLNode Instance")

  def test_no_value(self):
    node = LeafNode("a", None, {"href": "https://www.google.com"})
    self.assertRaises(ValueError, node.to_html)

  def test_leaf_to_html_no_tag(self):
    node = LeafNode(None, "Hello, world!")
    self.assertEqual(node.to_html(), "Hello, world!")