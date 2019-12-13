# Code Institute Christmas Challenge

_Name: **John Lynch**_

_Challenge Details:_  https://drive.google.com/file/d/1NkaNnGjKdxp1fvp6m9aCT2D-Rc3XKdD-/view

## Task

Write a function to print the following Christmas Tree to the console.

```
              |
             / \
            /   \
           /_   _\
           /     \
          /       \
         /_       _\
         /         \
        /           \
       /_           _\
       /             \
      /               \
     /_               _\
     /                 \
    /                   \
   /_                   _\
   /                     \
  /                       \
 /                         \
|___________________________|
           \_______/
```

## Implementation

As a lover of patterns, and someone who can get a great thrill out of representing a pattern as a mathematical structure or an algorithm, I decided to find the patterns in the distributions of spaces in the image.   I also decided to use Python for the job, merely because I am hoping to get a Python job, so am temporarily eschewing other languages.   In particular I am using Python 3.8, but any Python 3 version should run this little print statement fine, certainly <= 3.7.

First, I divided the image into three sections, to be considered separately: 
1. The top line, containing the tree fairy `|`.
2. The central foliage section, whose lines always start with `/`.
3. The bottom two lines, representing the base.

### Let's deal with the central section first:

We have two classes of whitespace strings:  leading spaces (before the first `/`) and central spaces (between `/` and `\`)

First, list the numbers of central spaces:
       Central spaces:
         1,  3,  5, 5,  7,  9,  9, 11, 13, 13, 15, 17, 17, 19, 21, 21, 23, 25
        
We can represent this by using `range()`:
`[range(i, i + 5, 2) for i in range(1, 22, 4)]` gives
`[[1, 3, 5], [5, 7, 9], [9, 11, 13], [13, 15, 17], [17, 19, 21], [21, 23, 25]]`
We can flatten a list like this with a list comprehension:
```
>>> a = [[1, 3, 5], [5, 7, 9], [9, 11, 13], [13, 15, 17], [17, 19, 21], [21, 23, 25]]
>>> [n for t in a for n in t]
[1, 3, 5, 5, 7, 9, 9, 11, 13, 13, 15, 17, 17, 19, 21, 21, 23, 25]
>>> 
```
So now we can represent this by
`[n for t in [range(i, i + 5, 2) for i in range(1, 22, 4)] for n in t]`.

### Similarly for the leading spaces:

```
>>> [n for t in [range(i, i + 3)[::-1] for i in range(7, 18, 2)[::-1]] for n in t]
[19, 18, 17, 17, 16, 15, 15, 14, 13, 13, 12, 11, 11, 10, 9, 9, 8, 7]
>>> 
```
Note that in this case we have to reverse the ranges, because the count of leading spaces is decreasing as we go down the tree.

### Putting it together to create art!

Let's analyse what we need.   We can simplify things a bit by ignoring the underscore `_` characters on every third line.   Let's just try to build the outer canopy of the tree, which contains only spaces, slashes `/`, backslashes `\` and carriage returns `\n`.

Notice the structure for each line is:

`<leading spaces> / <central spaces> \\ <carriage return>`,

and there are 18 lines.   We worked out the numbers of spaces, so let's set references to these:

```
>>> cs = [n for t in [range(i, i + 5, 2) for i in range(1, 22, 4)] for n in t]
>>> ls = [n for t in [range(i, i + 3)[::-1] for i in range(7, 18, 2)[::-1]] for n in t]
>>> ls # leading spaces
[19, 18, 17, 17, 16, 15, 15, 14, 13, 13, 12, 11, 11, 10, 9, 9, 8, 7]
>>> cs # central spaces
[1, 3, 5, 5, 7, 9, 9, 11, 13, 13, 15, 17, 17, 19, 21, 21, 23, 25]
>>> 
```
Now we can construct a call to the `print() function`:

In pseudo-code:

For each line `i` from `0` to `17`:
    print `ls[i]` spaces + `/` + `cs[i]` spaces + `\` + return.

So, in Python, we can make a list comprehension as the line index goes from 0 to 17, and then join all the lines we get:

```
>>> print(''.join([f'{" "*ls[i]}/{" "*cs[i]}\\\n' for i in range(18)]))
                   / \
                  /   \
                 /     \
                 /     \
                /       \
               /         \
               /         \
              /           \
             /             \
             /             \
            /               \
           /                 \
           /                 \
          /                   \
         /                     \
         /                     \
        /                       \
       /                         \

>>> 
```

Hurray!   We have the beginnings of our Christmas tree!

Now let's add the fairy!

First make a fairy:
`" " * 20 + '|\n'`

then add it to the tree:

```
>>> print(" " * 20 + '|\n' + ''.join([f'{" " * ls[i]}/{" " * cs[i]}\\\n' for i in range(18)]))
                    |
                   / \
                  /   \
                 /     \
                 /     \
                /       \
               /         \
               /         \
              /           \
             /             \
             /             \
            /               \
           /                 \
           /                 \
          /                   \
         /                     \
         /                     \
        /                       \
       /                         \

>>>
```

Now we need a base, and this is a simple matter of counting spaces and underscore characters:
```
>>> print(f'{" " * 6}|{"_" * 27}|\n{" " * 17}\\{"_" * 7}/\n')
      |___________________________|
                 \_______/

>>>
```

Let's add the base to the tree:

```
>>> print(" " * 20 + '|\n' + ''.join([f'{" " * ls[i]}/{" " * cs[i]}\\\n' for i in range(18)]) + f'{" " * 6}|{"_" * 27}|\n{" " * 17}\\{"_" * 7}/\n')
                    |
                   / \
                  /   \
                 /     \
                 /     \
                /       \
               /         \
               /         \
              /           \
             /             \
             /             \
            /               \
           /                 \
           /                 \
          /                   \
         /                     \
         /                     \
        /                       \
       /                         \
      |___________________________|
                 \_______/

>>>
```

Now, if we substitute in the list comprehensions we made for our lists of spaces, we get 

```
>>> print(" " * 20 + '|\n' + ''.join([f'{" " * [n for t in [range(i, i + 3)[::-1] for i in range(7, 18, 2)[::-1]] for n in t][i]}/{" " * [n for t in [range(i, i + 5, 2) for i in range(1, 22, 4)] for n in t][i]}\\\n' for i in range(18)]) + f'{" " * 6}|{"_" * 27}|\n{" " * 17}\\{"_" * 7}/\n')
                    |
                   / \
                  /   \
                 /     \
                 /     \
                /       \
               /         \
               /         \
              /           \
             /             \
             /             \
            /               \
           /                 \
           /                 \
          /                   \
         /                     \
         /                     \
        /                       \
       /                         \
      |___________________________|
                 \_______/

>>>
```

Now let's think about those extra underscore characters.   We notice they occur on every third line, in fact on lines 2, 5, 8, 11 and 14. We can create a `range()` object for this set: `range(2, 15, 3)`.

We can see that whenever we're on one of these lines, a `/` should become `/_`, the central space count should decrease by two, and `\` should become `_\`.

So `/` becomes `{'/_' if i in range(2, 15, 3) else '/'}`, and 
`\` becomes `{'_\\' if i in range(2, 15, 3) else '\\'}`.

For the spaces, let's add in two fewer spaces in the first place, then just add two more spaces if we're not on one of these special lines:

```
>>> print(" " * 20 + '|\n' + ''.join([f'{" " * [n for t in [range(i, i + 3)[::-1] for i in range(7, 18, 2)[::-1]] for n in t][i]}{"/_" if i in range(2, 15, 3) else "/"}{" " * ([n for t in [range(i, i + 5, 2) for i in range(1, 22, 4)] for n in t][i] - 2) + ("" if i in range(2, 15, 3) else "  ")}{"_" + chr(92) if i in range(2, 15, 3) else chr(92)}\n' for i in range(18)]) + f'{" " * 6}|{"_" * 27}|\n{" " * 17}\\{"_" * 7}/\n')
                    |
                   /  \
                  /   \
                 /_   _\
                 /     \
                /       \
               /_       _\
               /         \
              /           \
             /_           _\
             /             \
            /               \
           /_               _\
           /                 \
          /                   \
         /_                   _\
         /                     \
        /                       \
       /                         \
      |___________________________|
                 \_______/

>>>
```

Almost there.   But we seem to have a problem at the very top of the tree: a leaf on the right-hand side seems to be falling off!

Why?   Because we're trying to print `-1` spaces.   It would be nice if this acted as a backspace, but it doesn't, so we'll have to compensate for it:

```
>>> print(" " * 20 + '|\n' + ''.join([f'{" " * [n for t in [range(i, i + 3)[::-1] for i in range(7, 18, 2)[::-1]] for n in t][i]}{"/_" if i in range(2, 15, 3) else "/"}{" " * ([n for t in [range(i, i + 5, 2) for i in range(1, 22, 4)] for n in t][i] - 2) + (" " if not i else "" if i in range(2, 15, 3) else "  ")}{"_" + chr(92) if i in range(2, 15, 3) else chr(92)}\n' for i in range(18)]) + f'{" " * 6}|{"_" * 27}|\n{" " * 17}\\{"_" * 7}/\n')
                    |
                   / \
                  /   \
                 /_   _\
                 /     \
                /       \
               /_       _\
               /         \
              /           \
             /_           _\
             /             \
            /               \
           /_               _\
           /                 \
          /                   \
         /_                   _\
         /                     \
        /                       \
       /                         \
      |___________________________|
                 \_______/

>>>
```
### Hey presto!

Finally, we can change the single quotes for our main f-string into triple quotes, so that we can break the statement over a few lines:

```
Python 3.8.0 (default, Oct 28 2019, 16:14:01) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print(" " * 20 + '|\n' + ''.join([
...       f"""{" " * [n for t in [range(i, i + 3)[::-1] for i in range(7, 18, 2)[::-1]]
...       for n in t][i]}{"/_" if i in range(2, 15, 3) else "/"}{" " * ([n for t in [range(i, i + 5, 2)
...       for i in range(1, 22, 4)] for n in t][i] - 2) + (" " if not i else "" if i in range(2, 15, 3)
...       else "  ")}{"_" + chr(92) if i in range(2, 15, 3) else chr(92)}\n"""
...       for i in range(18)]) + f'{" " * 6}|{"_" * 27}|\n{" " * 17}\\{"_" * 7}/\n')
                    |
                   / \
                  /   \
                 /_   _\
                 /     \
                /       \
               /_       _\
               /         \
              /           \
             /_           _\
             /             \
            /               \
           /_               _\
           /                 \
          /                   \
         /_                   _\
         /                     \
        /                       \
       /                         \
      |___________________________|
                 \_______/

>>>
```

## Season's greetings to you all and happy coding!












