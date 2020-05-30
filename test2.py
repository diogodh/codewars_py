from twill.commands import *
import twill.commands as twill

go("https://nacionalidade.justica.gov.pt/")
# username= "0206-4272-1862"
username = "0000-0000-0000-0000"
fv("1", "SenhaAcesso", username)
a = submit()
print(a)
go("https://nacionalidade.justica.gov.pt/")

save_html result.txt

# twill.showforms()
