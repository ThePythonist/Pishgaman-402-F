lines = open("words.txt").readlines()
lines = lines[::-1]
output = "".join(lines)
open("reversedwords.txt", "w").write(output)
