from enum import Enum

class BlockType(Enum):
  PARAGRAPH = "paragraph"
  HEADING = "heading"
  CODE = "code"
  QUOTE = "quote"
  UNORDERED = "unordered"
  ORDERED = "ordered"

def markdown_to_blocks(markdown):
  blocks = markdown.split('\n\n')
  new_list = []
  for block in blocks:
    if block:
      new_list.append(block.strip())
  return new_list

def block_to_block_type(block):
  if block.startswith(('# ', '## ', '### ', '#### ', '##### ', '###### ')):
    return BlockType.HEADING
  if block.startswith("```") and block.endswith("```"):
    return BlockType.CODE
  lines = block.split('\n')
  stripped_lines = []
  for line in lines:
    stripped_lines.append(line.strip())

  is_quote = True
  for line in stripped_lines:
    if not line.startswith('>'):
      is_quote = False
  if is_quote:
    return BlockType.QUOTE
  
  is_unordered = True
  for line in stripped_lines:
    if not line.startswith('- '):
      is_unordered = False
  if is_unordered:
    return BlockType.UNORDERED
  
  is_ordered = True
  for i in range(len(stripped_lines)):
    if not stripped_lines[i].startswith(f'{i+1}. '):
      is_ordered = False
  if is_ordered:
    return BlockType.ORDERED
  return BlockType.PARAGRAPH