import mechanize
from PIL import Image
awbf = 0
url = "https://nacionalidade.justica.gov.pt"

br = mechanize.Browser()
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Firefox')]
response = br.open(url)

br.form = list(br.forms())[0]

control1 = br.form.find_control("SenhaAcesso")

br["SenhaAcesso"]= "0206-4272-1862"
# br["SenhaAcesso"]= "0000-0000-0000"
# control1.value= "0206-4272-1862"

content = br.submit().read()

with open('novo.txt','wb') as f:
    f.write(content)

f1 = open("novo.txt", "r")
f2 = open("original.txt", "r")

f1_line = f1.readline()
f2_line = f2.readline()

line_no = 1

# Loop if either file1 or file2 has not reached EOF
while f1_line != '' or f2_line != '':
    # Strip the leading whitespaces
    f1_line = f1_line.rstrip()
    f2_line = f2_line.rstrip()
    # Compare the lines from both file
    if f1_line != f2_line:
        # If a line does not exist on file2 then mark the output with + sign
        awbf = 1
        if f2_line == '' and f1_line != '':
            print(">+", "Line-%d" % line_no, f1_line)
        # otherwise output the line on file1 and mark it with > sign
        elif f1_line != '':
            print(">", "Line-%d" % line_no, f1_line)

        # If a line does not exist on file1 then mark the output with + sign
        if f1_line == '' and f2_line != '':
            print("<+", "Line-%d" % line_no, f2_line)
        # otherwise output the line on file2 and mark it with < sign
        elif f2_line != '':
            print("<", "Line-%d" % line_no, f2_line)

        # Print a blank line
        print()

    # Read the next line from the file
    f1_line = f1.readline()
    f2_line = f2.readline()

    # Increment line counter
    line_no += 1

# Close the files
f1.close()
f2.close()


if awbf == 1:
    img = Image.open("a.png")
    img.show()