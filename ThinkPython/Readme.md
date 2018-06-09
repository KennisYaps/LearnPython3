# ThinkPython

This is a consolidation of what I have learned and the mistakes I made

## Learnings

### Strings

`string_name.<SOME_METHODS>`

1.  `.lower()`: To convert string to lower case
2.  `.replace(" ","")`: To remove all the whitespace found in the string

### Dictionaries

1.  `dict()`: Declare an empty dictionaries
2.  `dict_name.get(key, default=None)`:

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
