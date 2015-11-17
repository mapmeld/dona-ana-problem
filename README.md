# Doña Ana Problem

For many English-speaking programmers, the first issue they encounter with character
encoding, especially in Python, is US census data. One county in the
US, (Doña Ana County, New Mexico) uses a Latin-1 character ñ

This repo has some examples of how to deal with it in Python 2 and 3.

There are also official Python HOWTOs:

<a href="https://docs.python.org/2/howto/unicode.html">Python 2 Unicode HOWTO</a>

<a href="https://docs.python.org/3/howto/unicode.html">Python 3 Unicode HOWTO</a>

Generally, Python 3 is easier to work with:

<img src="http://i.imgur.com/h2wyWHw.png"/>

## In Python 2

Take a look at ```script-p2.py```

#### writing Unicode in your Python strings

To use a non-ASCII character in a string written directly into
the Python source code, the first or second line of your file should be this comment:

```python
# -*- coding: utf-8 -*-
```

#### using Unicode as Python variable names

Not allowed in Python 2 😭

#### writing Unicode character codes

You can also use Unicode character codes such as \u6728 to represent the character 木

These should be inside a special Unicode string:

```python
tree_kanji = u"\u6728"
```

#### JSON stringify

If you want to show the contents of a Python object using JSON

```python
import json
json.dumps(data_object, ensure_ascii=False)
```

## In Python 3

Take a look at ```script-p3.py```

#### writing Unicode in your Python strings

Allowed by default in Python 3

#### using Unicode as Python variable names

This is allowed except for multi-byte Unicode characters, such as Emoji and
other recently-added letters.

#### writing Unicode character codes

You can also use Unicode character codes such as \u6728 to represent the character 木

These should be inside a special Unicode string:

```python
tree_kanji = u"\u6728"
```

#### JSON stringify

If you want to show the contents of a Python object using JSON

```python
import json
json.dumps(data_object, ensure_ascii=False)
```

## License

Creative Commons Zero
