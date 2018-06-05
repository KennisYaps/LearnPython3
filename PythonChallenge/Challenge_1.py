""" The image lists 3 pairs:
K->M
O->Q
E->G
everybody thinks twice before solving this.
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. """


s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
# 1st method: using ord() and chr()
# [Learnt] ord(): character to integer ;  chr(): integer to character;


def encrypt(input):
    splitWords = input.split(" ")
    # [Learnt] using if else in list comprehension. syntax: [ <true block> if <condition> else <false block> for element in array]
    encryption = [([chr(((ord(letter)+2) - ord('a')) % 26 + ord('a')) if letter >= "a" and letter <= "z" else letter for letter in word])
                  for word in splitWords]
    toString = [''.join(word) for word in encryption]
    result = ' '.join(toString)
    print(result)
    return result


encrypt(s)
encrypt("map")


# 2nd Method: using str.maketrans()
table = str.maketrans("abcdefghijklmnopqrstuvwxyz",
                      "cdefghijklmnopqrstuvwxyzab")
result = s.translate(table)
print(result)
