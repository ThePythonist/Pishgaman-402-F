lines = open("words.txt").read().split("\n")
output = "".join(lines)
open("oneline.txt", "w").write(output)
