# Qns: Find One small letter, surrounded by <b>EXACTLY</b> three big bodyguards on each of its sides.
import re
import urllib.request

# input = """
# kAewtloYgcFQaAJNhHVGxXDiQmzjfcpYbzxlWrVcqsmUbCunkfxZWDZjUZMiGqhRRiUvGmYmvnJIHEmbT
# kAewtloYgcFQaAJNhHVGxXDiQmzjfcpYbzxlWrVcqsmUbCunkfxZWDZjUZMiGqhRRiUvGmYmvnJIHEmbT
# """

#  Make requests to the page and read (bytes) and convert to str using `.decode()`
html = urllib.request.urlopen(
    "http://www.pythonchallenge.com/pc/def/equality.html").read().decode()
# Extract the data
raw_data = re.findall("<!--(.*?)-->", html, re.DOTALL)
data = raw_data[-1]


def reExercise(input):
    pattern = re.compile("[A-Z]{3}[a-z]{1}[A-Z]{3}", re.MULTILINE)
    results = pattern.findall(input)
    return results


results = reExercise(data)
print(results)
