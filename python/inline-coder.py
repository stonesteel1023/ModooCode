import os
import re

# Surround possible inline codes with ``.
class InlineCoder:
  def __init__(self, filename):
    self.in_table = False
    self.table_row = 0

    self.exceptions = {
      ".", "**", "__", "C++17", "C++ 17", "C++"
    }

    with open(filename, "r+") as f:
      data = f.read()
    
    with open("output", "w") as fw:
      fw.write(self.handle(data))

  def handle(self, data):
    result = []
    lines = data.split('\n')

    i = 0
    while i < len(lines):
      line = lines[i]

      # Remove '\n' at the end.
      line = line.rstrip()

      if len(line) >= 3 and line[:3] == '```':
        result.append(line)

        i += 1
        next_line = lines[i]
        result.append(next_line)

        while next_line[:3] != '```':
          i += 1
          next_line = lines[i]
          result.append(next_line)
        i += 1
        continue

      result.append(self.process_line(line))
      i += 1

    return '\n'.join(result)

  def process_line(self, line):
    if len(line) > 0 and line[0] == '|':
      if not self.in_table:
        self.in_table = True
        self.table_row = 0

        chunks = line.split('|')
        return '|'.join([self.process_chunk(chunk) for chunk in chunks])

      self.table_row += 1
      if self.in_table:
        # Second row is just ignored
        if self.table_row == 1:
          return line
        else:
          chunks = line.split('|')
          return '|'.join([self.process_chunk(chunk) for chunk in chunks])

    self.in_table = False
    if len(line) > 0 and line[0] == '*':
      right = self.process_chunk(line[1:])
      return '*' + right
    
    return self.process_chunk(line)

  def process_chunk(self, chunk):
    def check_char(c):
      if 'a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9':
        return True
      elif c in {
          '(', ')', '{', '}', ',', '.', '!', '+', '-', '*', '/', '=', '[', ']',
          '<', '>', '~', '_', '&', '%', '|', '?', ':'
      }:
        return True
      return False

    def check_inline_code_ok(code):
      if code in self.exceptions:
        return False
      if len(code) == 1:
        return False
      if len(code) > 4 and code[:2] == '**':
        return False
      return True

    def insert_c(s, index, c):
      return s[:index] + c + s[index:]

    i = 0
    while i < len(chunk):
      if chunk[i] == '`':
        # Ignore until next '`'
        i += 1
        while i < len(chunk) and chunk[i] != '`':
          i += 1

      if i == len(chunk):
        break

      if chunk[i] == '(':
        while i < len(chunk) and chunk[i] != ')':
          i += 1
        
        if i == len(chunk):
          break
      
      if check_char(chunk[i]) and chunk[i] != '.':
        inline_code_begin = i
        while i < len(chunk) and (check_char(chunk[i]) or chunk[i] == ' '):
          i += 1

        # Remove trailing spaces.
        inline_code_end = i
        while chunk[inline_code_end - 1] == ' ':
          inline_code_end -= 1
        
        inline_code = chunk[inline_code_begin:inline_code_end]
        if check_inline_code_ok(inline_code):
          # Now insert `` between (inline_code_begin, inline_code_end)
          chunk = insert_c(chunk, inline_code_end, '`')
          chunk = insert_c(chunk, inline_code_begin, '`')

          # Adjust the value of i.
          i += 2
      i += 1

    return chunk

if __name__ == "__main__":
  '''
  for filename in os.listdir("../md"):
    real_filename = "../md/" + filename
    with open(real_filename, "r+") as f:
      data = f.read()
      f.seek(0)
      f.write(handle(data))
  '''
  coder = InlineCoder("test")