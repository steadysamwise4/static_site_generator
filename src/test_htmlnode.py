import unittest

from htmlnode import HTMLNode
from textnode import *


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(tag="a", value="Google", props={"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(
            "HTMLNode(a, Google, children: None, {'href': 'https://www.google.com', 'target': '_blank'})", repr(node)
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )
    
    def test_is_instance(self):
        node = HTMLNode(tag="a", value="Google", props={"href": "https://www.google.com", "target": "_blank",})
        self.assertIsInstance(node, HTMLNode, "Not an HTMLNode Instance")
        
    def test_props_to_html(self):
        node = HTMLNode(tag="a", value="Google", props={"href": "https://www.google.com", "target": "_blank",})
        attributes = node.props_to_html()
        self.assertEqual(
            ' href="https://www.google.com" target="_blank"', attributes
        )

    def test_plain(self):
      node = TextNode("This is a text node", TextType.PLAIN_TEXT)
      html_node = text_node_to_html_node(node)
      self.assertEqual(html_node.tag, None)
      self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
      node = TextNode("This is a bold text node", TextType.BOLD_TEXT)
      html_node = text_node_to_html_node(node)
      self.assertEqual(html_node.tag, 'b')
      self.assertEqual(html_node.to_html(), "<b>This is a bold text node</b>")

    def test_italic(self):
      node = TextNode("This is an italic text node", TextType.ITALIC_TEXT)
      html_node = text_node_to_html_node(node)
      self.assertEqual(html_node.tag, 'i')
      self.assertEqual(html_node.to_html(), "<i>This is an italic text node</i>")

    def test_code(self):
      node = TextNode("This is a code node", TextType.CODE)
      html_node = text_node_to_html_node(node)
      self.assertEqual(html_node.tag, 'code')
      self.assertEqual(html_node.to_html(), "<code>This is a code node</code>")

    def test_link(self):
      node = TextNode("Learn to code at this link node", TextType.LINK, "https://www.boot.dev")
      html_node = text_node_to_html_node(node)
      self.assertEqual(html_node.tag, 'a')
      self.assertEqual(html_node.to_html(), '<a href="https://www.boot.dev">Learn to code at this link node</a>')

    def test_img(self):
      node = TextNode("stuff", TextType.IMAGE, "https://media.istockphoto.com/id/623194152/photo/free-stuff.jpg?s=612x612&w=0&k=20&c=98LtAqgIh25rz0HUJusCCT6Pf-uYG6ufN1SDwAji3Zk=")
      html_node = text_node_to_html_node(node)
      self.assertEqual(html_node.tag, 'img')
      self.assertEqual(html_node.to_html(), '<img src="https://media.istockphoto.com/id/623194152/photo/free-stuff.jpg?s=612x612&w=0&k=20&c=98LtAqgIh25rz0HUJusCCT6Pf-uYG6ufN1SDwAji3Zk=" alt="stuff" />')

    def test_unkown_type(self):
      node = TextNode("This is a text node", "wierd")
      self.assertRaises(Exception, text_node_to_html_node, node)

if __name__ == "__main__":
    unittest.main()