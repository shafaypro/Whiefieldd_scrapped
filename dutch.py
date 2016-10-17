file_read = open("Output2.csv", 'r')
file_write= open("TRANSLATEDOUTPUT.csv","w")
lines = file_read.readlines()
ls = ["accountant","consultant","managerial","tax advisor" ]
counter = 0
for line in lines:
    if counter == 0 :
        file_write.write(line)
        file_write.write("\n")
        counter += 1
        continue
    line=line.strip()
    line = line.split(",")
    if str(str(line[8]).strip()).lower() in ls:
        if str(str(line[8]).strip()).lower() == "accountant":
            line[8] = "Boekhouder"
        elif str(str(line[8]).strip()).lower() == "consultant":
            line[8] = "consultant"
        elif str(str(line[8]).strip()).lower() == "managerial":
            line[8] = "Administratiekantoor"
        elif str(str(line[8]).strip()).lower() == "tax advisor":
            line[8] = "Belastingadviseur"
    totalline=""
    for element in line:
        totalline += element + ","
    file_write.writelines(totalline)
    file_write.write("\n")