import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a plain text node", TextType.PLAIN_TEXT)
        node2 = TextNode("This is a bold text node", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)

    def test_default_url(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)
    
    def test_is_instance(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, "https://www.boot.dev")
        self.assertIsInstance(node, TextNode, "Not a TextNode Instance")
        
    def test_repr(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, plain, https://www.boot.dev)", repr(node)
        )

if __name__ == "__main__":
    unittest.main()