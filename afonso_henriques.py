import mechanize
import re
url = "https://nacionalidade.justica.gov.pt"

br = mechanize.Browser()
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Firefox')]
response = br.open(url)
br.form = list(br.forms())[0]
control1 = br.form.find_control("SenhaAcesso")
br["SenhaAcesso"] = "0000-0000-0000-0000"

response = br.submit()
content = response.read()
print(content)
#
# result = re.findall(r"Prob_Heavy.csv", content)
# print result