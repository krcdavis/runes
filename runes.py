def find_position(char):
  for set_num in range(len(table)):
    if char in table[set_num]:
      return set_num
  return False

def forge_offsets(string, direction, offset):
  if type(string) is str:
    return [((ord(x) - 96) + offset) * direction for x in string]
  else:
    return [(x + offset) * direction for x in string]

def frequency(text):
  return {letter: text.count(letter) for letter in 'abcdefghijklmnopqrstuvwxyz'.upper()}

######
#
#  Scroll down for the bits you should interact with
#
######

table = [
  ["ᚠ", "F"], 
  ["ᚢ", "V"],
  ["ᚦ", "TH"],
  ["ᚩ", "O"],
  ["ᚱ", "R"],
  ["ᚳ", "C"],
  ["ᚷ", "G"],
  ["ᚹ", "W"],
  ["ᚻ", "H"],
  ["ᚾ", "N"],
  ["ᛁ", "I"],
  ["ᛂ", "J"],
  ["ᛇ", "EO"],
  ["ᛈ", "P"],
  ["ᛉ", "X"],
  ["ᛋ", "S"],
  ["ᛏ", "T"],
  ["ᛒ", "B"],
  ["ᛖ", "E"],
  ["ᛗ", "M"],
  ["ᛚ", "L"],
  ["ᛝ", "ING"],
  ["ᛟ", "OE"],
  ["ᛞ", "D"],
  ["ᚪ", "A"],
  ["ᚫ", "AE"],
  ["ᚣ", "Y"],
  ["ᛡ", "IA"],
  ["ᛠ", "EA"]
]

# The following three blocks are pages 40-42
# Below them, called 'fiftysix' and 'fiftyseven' are pages 56 and 57
# Rename their variables to text if you want to test them as well
# If you want any more pages, copy the blocks from https://titanpad.com/hJ8pVQ5S43
#
# Note that in page 56, there is an 'F' in plaintext. The cipher skips over this completely.
# I have replaced it with three spaces. 
# If you want it back for sake of completeness, replace those three spaces with ᚠ

text = """ᚠᚾᛗ•ᚣᚷᛞᚫᚻ•ᚪᛈᛉᚣᚻ•ᛇᛠᚩᛖ•ᛏᛝ
ᛠ•ᛚᛁᛏᚦᚠ•ᛗᚪᚳᛖ•ᛞᚳ•ᛏᚱᛟᚷᛠᚾ
ᚫᛒᚢᛖᛒᚢ•ᚦᚠᛟ•ᚷᛋᛟ•ᛁᛈ•ᛟᛉᛋᛒ•ᚹᛂᛒ
ᚣᛗᚢᛠ•ᚱᛁᚢᛟᛂᛁ•ᛗᛖᚫ•ᚱᛋᛉᛝ•"ᛠᛈᛚ•
ᛞᚩᛚᛁᛉᛠᛝᛖᚱ"•ᚾᛈᛖᚹᛡ•ᚾᛂᛏᚣ•ᛋᚩᛋ
ᛏᛝ•ᚢᚾᛇᚪ•ᛖᛏᚪᛂᚳᚣ•ᛟᛒ•ᛚᛋ•ᛒᛞᛂ•ᛁᛝᚣᛖ
ᚳ•ᛂᚻᛚᚣ•ᚷᚫᛚᛞ•ᛚᚫᛚᚦᛉ•ᛚ•ᛖᛉᚩᛉᛁᚳᚢᛗ
ᚾᚢ•ᚩᚾᛇ•ᚻᛡᛚᛇᚩᚫᚪ•ᚩᛟᚩ•ᚣᚱ•ᛖᚠᚢ•ᛁᚻ•ᛟᛚ
ᚾᛏ•"ᚠᛞᚱᛠᚷ•ᛈᚩᛇᚩᛗᛠᛒ•ᛂᛡ•ᛋᛗᚠ•ᛏ
ᚠᚫᚩ•ᛟᚳᛚᛞᛡᛚ•ᚩᚳᛝᚢ•ᛈᚹᛏ•ᚷᚳᛋ•ᚢᛟᚷᚦ•
ᚠᛉᚠᛏ•ᚳᛋᛉᛟ•ᚷᚠᛉᚾᛞ•ᛒᛏᛠᛡ"•ᛈᛡ

ᛠᛁᚪ•ᛋᚣᛗᛞᚣᛋ•ᛒᛞᛂᛞ•ᚩᚾᛏᛚ•ᚳᚪᛝ•ᚱᚷ
ᚻᚷ•ᛂᚹᚠ•ᚪᚢᛇ•ᛞᛏᛗᛂᛁ•ᛝᚫ•ᛉᛈᚳᛈᛠ•ᛟᚪ
ᛒᛁᛁᛋ•ᛇᚷᚻᛋ•ᛇᛡᛒ•ᚠᚹᛝ•ᚫᚪᚠᚩᚣᛡᚪᚾᚻ•ᛒᚦᛟ
ᛇᚣᛟᛁᛒ•ᛟ•ᚩᛋᚹ•ᛞᚳᚠᚪᛁ•ᛉᛏᛟᚢᚩᛟᚦᛈᛋᚩ•
ᚻᛇᚦᛝ•ᛏᛠᚠᛝᛠ•ᚩᛗ•ᛏᚠᚣᛚᚣ•ᚹᛚᛞ•ᚪᛉ
ᛠ•ᚪᛂ•ᚩᛋᛒᛚ•ᚳᛖᚾᚪᚩᚱᛏᚦ•ᚱᛒᚳᚣ•ᛠᛗᚹᛚ•
ᚻᛈ•ᛇᛈᛖ•ᛚᛂᚩᛡᚪ•ᛖᛋᚫᚩ•ᛠᛉᛝᚣ•ᛖᚫᛒ
ᛗ•ᛖᚻᚱ•ᛈᚾᛗ•ᚹᛏᛟᚣᚢ•ᚠᛉᛈᛗᚩᚷᚾ•ᛡᛇᚳ
ᚠᛒᛈᛗ•ᛋᛇᛁ•ᛖᛈᚢᚱᛏᚳᚣ•ᛂᛚᚠ•ᚱᛚᚱᚫᛖᚻᛟ
•ᛇᚣᛡ•ᚩᛉ•ᚪᛋᚣᛁᛝ•ᛉᛚᛂ'ᚳ•ᛖᚣᚢᛝᚦᛇᚱ•
ᛠᛁᚫ•ᚦᚠᛟᚷᛠᛁ•ᛈᛋᛒ•ᛗᛒᛂᚠᚾᚳᛖ•ᚻᚫᚩᛂ•
ᛉᛂᛚᛈᚪᛁ•ᛟᚹᚱᛁᚱᚦᛖᛉ•ᚪᚾ•ᛞᛂᚷ•ᛟᛟᚳᛏᛂ

ᛞ•ᛉᚾᛗᚦ•ᛁᛂᚱ•ᛈᛉᚢᚫᚦᛒᚠᛂᚦ•ᚠᚪᛝᛖ•ᚹᚹᚣ
ᛚᛇ•ᚢᚣ•ᚾᚱᚪ•ᛈᚾᚹ•ᛚᚾᛏᛚᚢᛒᚱᛝᚪᛋ•ᚫᛈ•ᛂᛚ
ᚢᚳᚷ•ᛚᛏᛂᚹᛈ•ᚫᛗᛚ•ᛉᛚᛗᛏᛞᚠᛈᛁ•"ᚠᚳᚦ
ᛗᛂᚹᚱᚪᛚ•ᚩᛝᚱᚢᛈᚱᛟᛡ•ᚳᛉᚱ•ᛇᛏᚦᚾ•ᚱᛇᚫ
ᛞᛟᚻ•ᛒᚾᚣ•ᚠᛡᚪᛡᛖᚫᛞᛂᚢᛖ•ᚦᚱ•ᚩᛇᚱᛡ•
ᚣᛁᛉᛇᚻᚩᛠ•ᚫᚻᛡᛝᛠᚦ•ᚾᚣ•ᚾᚠᛁᛝ"•"ᛏ
ᚻᚹᚫ•ᛒᛇ•ᛡᚻᛉᛒ•ᛞᛝᚱᛂᚦᚻ•ᚪᚷᚣᛁᚠᚷ•ᛁᛏᛞ
ᛠᛒᚠᚩᛈ•ᛇᛡᛟᚹᚱᚾᚩᛏ•ᛋᚹᚢ•ᛖᛡᛖᛡᚦ•ᛉ
ᚪᚷᛈᚾ•ᛋᚱᚠᛞᛝᚻᛖᛂᛞ•ᛂᛡ•ᚱᚹ•ᚷᛝᚪᛒ•ᛂᛈ
ᛂ•ᛏᚠᛉ•ᚪᛂ•ᛁᚠᛉᚢᚩᚣᚻᚦ•ᚻᚾᛁᛒ•ᛡᛟᛡᛋᛈᚣ
ᛉ•ᛠᚢᛠᛚ•ᚠᛝᛗᚻ•ᚦᛒᚩ•ᛗᛚ•ᚩᛠᛋᚦᛠ•ᛇ
ᛋᛉ•ᚠᛗᛒ•ᚫᛋᛇᚾᛡᚾ•ᚢᚫᚹ•ᛞᛠᚢᚾᛝᚠᚾᛖᚫ"""

fiftysix = """ᚫᛂ•ᛟᛋᚱ•ᛗᚣᛚᚩᚻ•ᚩᚫ•ᚳᚦᚷᚹ•ᚹᛚᚫ•ᛚ
ᚩᚪᛈ•ᛗᛞᛞᚢᚷᚹ•ᛚ•ᛞᚾᚣᛂ•ᚳᚠᛡ•ᚫᛏ
ᛈᛇᚪᚦ•ᚳᚫ
ᚳᛞ•ᚠᚾ•ᛡᛖ•ᚠᚾᚳᛝ•ᚱ   •ᚫᛁᚱᛞᛖ•ᛋᚣᛂᛠᚢ
ᛝᚹ•ᛉᚩ•ᛗᛠᚹᚠ•ᚱᚷᛡ•ᛝᚱᛒ•ᚫᚾᚢᛋ•"""

fiftyseven = """ᛈᚪᚱᚪᛒᛚᛖ• ᛚᛁᚳᛖ•ᚦᛖ•ᛁᚾᛋᛏᚪᚱ•ᛏ
ᚢᚾᚾᛖᛚᛝ•ᛏᚩ•ᚦᛖ•ᛋᚢᚱᚠᚪᚳᛖ•
ᚹᛖ•ᛗᚢᛋᛏ•ᛋᚻᛖᛞ•ᚩᚢᚱ•ᚩᚹᚾ•ᚳ
ᛁᚱᚳᚢᛗᚠᛖᚱᛖᚾᚳᛖᛋ• ᚠᛁᚾᛞ•ᚦ
ᛖ•ᛞᛁᚢᛁᚾᛁᛏᚣ•ᚹᛁᚦᛁᚾ•ᚪᚾᛞ•ᛖᛗᛖᚱᚷᛖ•"""

output = ""

# Subtract is for skipping spaces and •s in the text, so that our offsets stay on track
# There's probably a cleaer way to do it but CBF

subtract = 0

# forge_offset() makes a list of offsets to be *added* to the corresponding rune when shifting
# i.e. If your offset list is [3, 4, 28, 4, 6, 9] you'll shift the first offset by 3, the second by 4, etc
# It takes three arguments: A base list, a 'direction' and another offset
#
# Base list: What your basic offset looks like, say a list of primes as in the example below
# Direction: Either -1 or 1, this is will be multiplied to the final number so you can add or subtract offsets
# Offset: Offset every number in your list by this
#
# This is because, for page 56, the offsets are a list of prime numbers
# To that list you subtract 1 from every value
# And multiply it by negative 1, or just *subtract* the offsets from your runes
#
# Special note: Instead of a list, you can supply a piece of alphabetical text to the function
# We work out what number of the alphabet it is and return a list based on that instead
#
# If it doesn't make sense your best shot is to either read the code or just go with it
# The first instance of 'offsets' below will work on page 56
# The second instance works on page 57, and also any runes that are in plaintext

offsets = forge_offsets([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987], -1, -1)
offsets = [0 for x in range(1000)]

# The stuff below is a little more confusing
# We pull each rune from the text supplied
# If it's a •, add a space to the output
# If it's a rune (i.e. searching for it returns true), then we find the corresponding letter after applying the offset
# If it's not a rune (• or anything else), then we also maintain our subtract value
#
# Just trust me this works

for rune_num in range(len(text)):
  rune = text[rune_num]
  offset = offsets[rune_num - subtract]

  if rune == "•":
    output+=" "
    subtract += 1
  elif type(find_position(rune)) is int:
    output+=table[(find_position(rune) + offset) % 29][1]
  else:
    subtract += 1

# We then print the output of our stuff
# All the frequency() function does is return frequencies in numbers
# So here we format it to look a little nicer

print(output)

freq = frequency(output)

for entry in freq:
  print(entry + ": " + str(round(freq[entry] / len(output) * 100, 4)))