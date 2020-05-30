import os
import twill
from twill.commands import *
url = "https://nacionalidade.justica.gov.pt/"
out = open(os.devnull,"w")
twill.set_output(out)
go(url)
formvalue("1", "username", "avi")
# formvalue("1", "password", "stackoverflow")
# submit()
# go(url2) #some protected page
# content = show()
# print ('content is',content[:100])