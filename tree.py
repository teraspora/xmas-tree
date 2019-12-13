# Code Institute Christmas Coding Challenge 2019
# Author:  John Lynch
# December 13th, 2019
# 

def xmas_tree():
    print(" " * 20 + '|\n' + ''.join([
      f"""{" " * [n for t in [range(i, i + 3)[::-1] for i in range(7, 18, 2)[::-1]]
      for n in t][i]}{"/_" if i in range(2, 15, 3) else "/"}{" " * ([n for t in [range(i, i + 5, 2)
      for i in range(1, 22, 4)] for n in t][i] - 2) + (" " if not i else "" if i in range(2, 15, 3)
      else "  ")}{"_" + chr(92) if i in range(2, 15, 3) else chr(92)}\n"""
      for i in range(18)]) + f'{" " * 6}|{"_" * 27}|\n{" " * 17}\\{"_" * 7}/\n')

if __name__ == '__main__':
  xmas_tree()