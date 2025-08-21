def markdown_to_blocks(markdown):
  blocks = markdown.split('\n\n')
  new_list = []
  for block in blocks:
    if block:
      new_list.append(block.strip())
  return new_list