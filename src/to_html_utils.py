import re

from block_utils import *
from parentnode import ParentNode
from markdown_utils import text_to_textnodes
from textnode import *

def format_text(text):
  return text.strip().replace('\n', ' ')

def format_code_block(block):
    # Remove opening backticks and newline if present
    if block.startswith('```\n'):
      content = block[4:]  # Remove '```\n'
    elif block.startswith('```'):
      content = block[3:]  # Remove '```'
    else:
      content = block
    # Remove closing backticks
    if content.endswith('```'):
      # this preserves trailing newline if present
      # an interesting convention of parsing markdown
      # apparently
      stripped_block = content[:-3]  # Remove '```'
    else:
      stripped_block = content
    return stripped_block

def format_multi_line_block(block, symbol):
  lead_char = ''
  if symbol != 'num':
    lead_char = symbol
  lines = block.split('\n')
  formatted_lines = ''
  for i in range(len(lines)):
    if symbol == 'num':
      lead_char = f'{i+1}.'
    formatted_line = lines[i].strip().lstrip(lead_char).strip()
    if not formatted_lines:
      formatted_lines = formatted_line
    else:
      formatted_lines = formatted_lines + '\n' +formatted_line
  return formatted_lines

def text_to_children(text):
    converted_nodes = []
    formatted_text = format_text(text)
    new_nodes = text_to_textnodes(formatted_text)
    for node in new_nodes:
      converted_nodes.append(text_node_to_html_node(node))
    return converted_nodes

def determine_heading_tag(heading_block):
    size = 0
    for char in heading_block:
      if char == '#':
        size += 1
      else:
        break
    return f'h{size}'

def format_list_lines(block):
  lines = block.split('\n')
  children = []
  for line in lines:
    grandchildren = text_to_children(line)
    child_node = ParentNode('li', grandchildren)
    children.append(child_node)
  return children

def create_html_node_from_block(block, block_type):
  match block_type:
    case BlockType.PARAGRAPH:
      children = text_to_children(block)
      # img and a tags should not be wrapped in a p if they make up their own block
      if len(children) == 1 and (children[0].tag == 'img' or children[0].tag == 'a'):
        return children[0]
      return ParentNode('p', children)
    case BlockType.HEADING:
      text = block.lstrip('#')
      children = text_to_children(text)
      tag = determine_heading_tag(block)
      return ParentNode(tag, children)
    case BlockType.CODE:
      formatted_block = format_code_block(block)
      node = TextNode(formatted_block, TextType.PLAIN_TEXT, None)
      content = text_node_to_html_node(node)
      child = ParentNode('code', [content])
      return ParentNode('pre', [child])
    case BlockType.QUOTE:
      formatted_block = format_multi_line_block(block, '>')
      grandchildren = text_to_children(formatted_block)
      child = ParentNode('p', grandchildren)
      return ParentNode('blockquote', [child])
    case BlockType.UNORDERED:
      formatted_block = format_multi_line_block(block, '-')
      children = format_list_lines(formatted_block)
      return ParentNode('ul', children)
    case BlockType.ORDERED:
      formatted_block = format_multi_line_block(block, 'num')
      children = format_list_lines(formatted_block)
      return ParentNode('ol', children)
    case _:
      raise Exception("Unknown block type")

def markdown_to_html_node(markdown):
  blocks = markdown_to_blocks(markdown)
  child_nodes = []
  for block in blocks:
    block_type = block_to_block_type(block)
    new_node = create_html_node_from_block(block, block_type)
    child_nodes.append(new_node)

  top_node = ParentNode('div', child_nodes)
  return top_node
  