import unittest

from block_utils import markdown_to_blocks, block_to_block_type, BlockType

class TestBlocks(unittest.TestCase):
      def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

      def test_markdown_to_blocks_extra_newlines(self):
        md = """
This is **bolded** paragraph with tripple new lines after



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph with tripple new lines after",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

      def test_block_to_block_type_heading(self):
         block = "### Star Wars"
         block_type = block_to_block_type(block)
         self.assertEqual(block_type, BlockType.HEADING)

      def test_block_to_block_type_paragraph(self):
         block = "Star Wars is an excellent science fiction space adventure"
         block_type = block_to_block_type(block)
         self.assertEqual(block_type, BlockType.PARAGRAPH)

      def test_block_to_block_type_code(self):
         block = "```print('Hello World')```"
         block_type = block_to_block_type(block)
         self.assertEqual(block_type, BlockType.CODE)

      def test_block_to_block_type_code_with_newlines(self):
         block = "```\nprint('Hello World')\n```"
         block_type = block_to_block_type(block)
         self.assertEqual(block_type, BlockType.CODE)

      def test_block_to_block_type_code_incorrect(self):
         block = "```print('Hello World')``"
         block_type = block_to_block_type(block)
         self.assertEqual(block_type, BlockType.PARAGRAPH)

      def test_block_to_block_type_quote(self):
         block = """> This is a multi-line blockquote.
> You can add the '>' symbol at the beginning of each line
> to explicitly continue the blockquote."""
         block_type = block_to_block_type(block)
         self.assertEqual(block_type, BlockType.QUOTE)

      def test_block_to_block_type_quote_incorrect(self):
         block = """> This is a multi-line blockquote.
 You can add the '>' symbol at the beginning of each line
> to explicitly continue the blockquote."""
         block_type = block_to_block_type(block)
         self.assertEqual(block_type, BlockType.PARAGRAPH)

      def test_block_to_block_type_unordered(self):
         block = """- Item 1
- Item 2
- Item 3
- Item 4"""
         block_type = block_to_block_type(block)
         self.assertEqual(block_type, BlockType.UNORDERED)

      def test_block_to_block_type_unordered_incorrect(self):
         block = """- Item 1
- Item 2
-- Item 3
- Item 4"""
         block_type = block_to_block_type(block)
         self.assertEqual(block_type, BlockType.PARAGRAPH)

      def test_block_to_block_type_code_ordered(self):
         block = """1. First item
2. Second item
3. Third item"""
         block_type = block_to_block_type(block)
         self.assertEqual(block_type, BlockType.ORDERED)

      def test_block_to_block_type_ordered_incorrect(self):
         block = """1. First item
3. Second item
4. Third item"""
         block_type = block_to_block_type(block)
         self.assertEqual(block_type, BlockType.PARAGRAPH)