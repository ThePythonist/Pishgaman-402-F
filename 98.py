students = [
    {"name": "korosh", "age": 13, "job": "front-end dev"},
    {"name": "ali", "age": 16, "job": "back-end dev"},
    {"name": "zahra", "age": 22, "job": "back-end dev"},
    {"name": "amirali", "age": 14, "job": "back-end dev"},
    {"name": "shervin", "age": 14, "job": "database admin"},
]

html = """
<!DOCTYPE html>
<html>
<head>
<style>
#customers {
  font-family: Consolas;
  border-collapse: collapse;
  width: 100%;
}

h1 {
    font-family: Consolas;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #16736a;
  color: white;
}
</style>
</head>
<body>

<h1>Clas 402-F</h1>

<table id="customers">
  <tr>
    <th>Name</th>
    <th>Age</th>
    <th>Job</th>
  </tr>
  
"""

for i in students:
    html += f"""
  <tr>
    <td>{i['name']}</td>
    <td>{i['age']}</td>
    <td>{i['job']}</td>
  </tr>
    """

html += """
</table>
</body>
</html>
"""

open("Table.html", "w").write(html)
