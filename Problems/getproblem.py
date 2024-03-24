import requests
url = input("url: ")
if "problem" in url: url = "https://projecteuler.net/minimal=" + url.split("=")[1]
if "problem" not in url and "minimal" not in url: url = "https://projecteuler.net/minimal=" + url

response = requests.get(url).text

response = response.replace("</p>", "")
response = response.replace("<p>", "")
response = response.replace("$", "")
response = response.replace("\dots", "...")
response = response.replace("cdots", "...")
response = response.replace(r"\times", "X")
response = response.replace(r"\ne", "!=")
response = response.replace("<br>", "\n")
response = response.replace("&amp;", "")
response = response.replace("\\", "")
response = response.replace("<blockquote>", "")
response = response.replace("</blockquote>", "")
response = response.replace("begin{align}", "")
response = response.replace("end{align}", "")
response = response.replace("&lt;", "<")
response = response.replace("<div>", "")
response = response.replace("</div>", "")

print(response)
