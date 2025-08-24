import unittest

from to_html_utils import markdown_to_html_node
from block_utils import markdown_to_blocks, block_to_block_type

class TestMD_To_HTML(unittest.TestCase):
  def test_paragraphs(self):
    md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

  def test_codeblock(self):
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )

  def test_codeblock_malformed(self):
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff```
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff</code></pre></div>",
    )

  def test_heading_basic(self):
    md = "## Second Heading"

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><h2>Second Heading</h2></div>",
    )

  def test_heading_with_bold(self):
    md = "## Second **Heading**"

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><h2>Second <b>Heading</b></h2></div>",
    )

  def test_heading_bad_format(self):
    md = "###Second Heading with bad format"

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><p>###Second Heading with bad format</p></div>",
    )

  def test_quote_basic(self):
    md = "> This is a quote"

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><blockquote><p>This is a quote</p></blockquote></div>",
    )

  def test_quote_multi_line(self):
    md = """
    > This is a quote
    > that is on multiple lines
    > for some odd reason
    """

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><blockquote><p>This is a quote that is on multiple lines for some odd reason</p></blockquote></div>",
    )

  def test_unordered_list(self):
    md = """
    - This is a list
    - of stuff
    - that is unordered
    """

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><ul><li>This is a list</li><li>of stuff</li><li>that is unordered</li></ul></div>",
    )

  def test_ordered_list(self):
    md = """
    1. This is a list
    2. of stuff
    3. that is ordered
    """

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><ol><li>This is a list</li><li>of stuff</li><li>that is ordered</li></ol></div>",
    )

  def test_mixed_blocks(self):
    md = """
    # Heading

    This is a basic paragraph with **bold** text.

    > This is a quote
    > on multiple lines

    ```
print("Hello World")
print("My test works!")
```

    ![bears](https://www.wildnatureimages.com/photo/grizzly-bear-14/)

    [learn to code!](https://boot.dev)

    1. This is a list
    2. of stuff
    3. that is ordered

    ...the _end_.
    """

    expected = (
      "<div>"
      "<h1>Heading</h1>"
      "<p>This is a basic paragraph with <b>bold</b> text.</p>"
      "<blockquote><p>This is a quote on multiple lines</p></blockquote>"
      '<pre><code>print("Hello World")\nprint("My test works!")\n</code></pre>'
      '<img src="https://www.wildnatureimages.com/photo/grizzly-bear-14/" alt="bears" />'
      '<a href="https://boot.dev">learn to code!</a>'
      "<ol><li>This is a list</li><li>of stuff</li><li>that is ordered</li></ol>"
      "<p>...the <i>end</i>.</p>"
      "</div>"
    )

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        expected,
    )

  def test_blocks_to_markdown(self):
    block = "```inline code```"
    block_type = block_to_block_type(block)
    # print(f"block_type: {block_type}")