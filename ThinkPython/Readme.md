# ThinkPython

This is a consolidation of what I have learned and the mistakes I made

## Learnings

### Strings

`string_name.<SOME_METHODS>`

1.  `.lower()`: To convert string to lower case
2.  `.replace(" ","")`: To remove all the whitespace found in the string

### Dictionaries

`dict_name.<SOME_METHODS>`

1.  `dict()`: Declare an empty dictionaries
2.  `get(key, default=None)`:

- `key` − This is the Key to be searched in the dictionary
- `default` − This is the Value to be returned in case key does not exist.
- **Use case**: When you want to find the no.of occurance of the letter in an text

  Example:
  `text = "hellohellohello"` to return this `{'h': 3, 'e': 3, 'l': 6, 'o': 3}`

  ```python
  text = "hellohellohello"
  tabulate = dict()
  for letter in text:
      tabulate[letter] = tabulate.get(letter, 0)+1  
  ```

  `.get()` is finding the _key_ `letter` in the dict, `tabulate`. If the _key_ doesnt exist, the value will be `0`. Else, if it exist, the _key_'s value will `+= 1`
  https://www.tutorialspoint.com/python3/dictionary_get.htm

3.  Sorting a dict by its Value / Key
    https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value

    - By `Value`:
      Example:

      ```python
      import operator
      unsorted_dict={'h': 3, 'e': 3, 'l': 6, 'o': 3}
      sort = sorted(unsorted_dict.items(), key=operator.itemgetter(1))
      ```

      return
      `[('h', 3), ('e', 3), ('o', 3), ('l', 6)]`

      - Syntax for `sorted()`:
        `sorted(iterable, *, key=None, reverse=False)`

        - Return a new sorted list from the items in iterable.
        - Has two optional arguments which must be specified as keyword arguments.
        - `key`= used as a comparison key from each list element. Default value will be `key = None`, which will compare the elements directly.
        - `reverse` is a boolean value. If set to True, then the list elements are sorted in reversed order.
          https://docs.python.org/3/library/functions.html#sorted

      - `unsorted_dict.items()` will return `dict_items([('h', 3), ('e', 3), ('l', 6), ('o', 3)])`
      - `operator.itemgetter(1)` will get element in index 1 and set it to be the comparison `key`
        https://docs.python.org/3/library/operator.html#operator.itemgetter

    - By `Key`:
      - replace `1` to `0` to get the `key` value. `operator.itemgetter(0)`
