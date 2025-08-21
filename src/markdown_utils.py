import re

from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
  result = []
  for o_n in old_nodes:
    print('o_n:',o_n)
    if o_n.text_type != TextType.PLAIN_TEXT:
      result.append(o_n)
      continue

    text_arr = o_n.text.split(delimiter)
    if len(text_arr) % 2 != 1:
      raise Exception(f'Error: Invalid Markdown detected! - {o_n.text}')
    is_text = True
    print('text_arr:', text_arr)
    for t in text_arr:
      if len(t.strip()) == 0:
        is_text = False
        continue
      if is_text:
        result.append(TextNode(t, TextType.PLAIN_TEXT))
      else:
        result.append(TextNode(t, text_type))
      is_text = not is_text
  return result

def extract_markdown_images(text):
  matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
  print('matches:', matches)
  return matches

def extract_markdown_links(text):
  matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
  print('matches:', matches)
  return matches

def split_nodes(old_nodes, text_type, helper_func):
  result = []
  for o_n in old_nodes:
    if o_n.text_type != TextType.PLAIN_TEXT:
      result.append(o_n)
      continue
    matches = helper_func(o_n.text)
    if len(matches) == 0:
      result.append(o_n)
      continue
    current_text = o_n.text
    split_nodes = []
    for i in range(len(matches)):
      first_part = matches[i][0]
      sec_part = matches[i][1]
      if text_type == TextType.IMAGE:
        sections = current_text.split(f"![{first_part}]({sec_part})", 1)
      elif text_type == TextType.LINK:
        sections = current_text.split(f"[{first_part}]({sec_part})", 1)
      print('sections:', sections)
      if sections[0].strip() is not "":
        split_nodes.append(TextNode(sections[0], TextType.PLAIN_TEXT))
      split_nodes.append(TextNode(first_part, text_type, sec_part))
      if i == len(matches) - 1:
        if sections[1].strip() is not "":
          split_nodes.append(TextNode(sections[1], TextType.PLAIN_TEXT))
      current_text = sections[1]
      print('current_text:', current_text)
    result.extend(split_nodes)
  return result

def text_to_textnodes(text):
  node = TextNode(text, TextType.PLAIN_TEXT)
  old_nodes = split_nodes_delimiter([node], '`', TextType.CODE)
  old_nodes = split_nodes_delimiter(old_nodes, '_', TextType.ITALIC_TEXT)
  old_nodes = split_nodes_delimiter(old_nodes, '**', TextType.BOLD_TEXT)
  old_nodes = split_nodes(old_nodes, TextType.LINK, extract_markdown_links)
  result = split_nodes(old_nodes, TextType.IMAGE, extract_markdown_images)
  return result
      