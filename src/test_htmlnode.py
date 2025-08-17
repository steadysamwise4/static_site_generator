import unittest

from htmlnode import HTMLNode


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

if __name__ == "__main__":
    unittest.main()