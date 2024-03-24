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

print(response) # Sonra \n  varsa ele

"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).<br>
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.


"""