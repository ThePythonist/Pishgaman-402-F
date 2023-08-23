header = input("Type header : ")
par = input("Type paragraph : ")
html = f"""
<h1> {header} </h1>
<p> {par} </p>
"""

open("index.html", "w").write(html)
