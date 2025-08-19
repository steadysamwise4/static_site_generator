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
      