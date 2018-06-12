# PythonChallenge

- Questions: http://www.pythonchallenge.com/
- Solutions: https://the-python-challenge-solutions.hackingnote.com/

## Learnings

1.  using `if-else` in list comprehension.
    - syntax:
      `[ <true block> if <condition> else <false block> for element in array]`
2.  Loading data from the web

    - Method 1 : Copy the text and paste it in a `.txt` file.

      ```python
      <!-- Under index.txt -->
      hello

      <!-- To get the contents from index.txt -->
      data = open("index.txt).read()
      ```

    - Method 2 : using urllib.request

      ```python
      <!-- Used to make requests / fetching URLs -->
      import urllib.request
      html = urllib.request.urlopen(
      "http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()
      ```

      - `.urlopen(INSERT_URL)` :
        Returns a response object (in an array) for the URL requested
      - `.read()`:
        - This response by `.urlopen(INSERT_URL)` is a file-like object, which means you can for example call `.read()` on the response
        - Return in `bytes`
      - `.decode()`:
        - Will convert `bytes` to `str`

      https://docs.python.org/3/library/re.html#re.DOTALL

3.  `re.DOTALL`:

    - Make the `'.'` special character match any character at all, including a **newline**; without this flag, `'.'` will match anything **except a newline.**

    https://docs.python.org/3/library/re.html#re.DOTALL

4.  `re.findall(pattern, string, flags=0)`

    - Return all **non-overlapping** matches of pattern in string, as a **list of strings.**
    - Matches are returned in the order found.
    - If one or more groups are present in the pattern, return a list of groups; this will be a list of tuples if the pattern has more than one group.
    - Empty matches are included in the result.

    https://docs.python.org/3/library/re.html#re.findall
