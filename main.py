import os
import pandas as pd
search_path = input("Enter directory path to search : ")
file_type = input("File Extension (Case sensitive ) : ")
search_word = input("Enter what you're searching for (Case sensitive ) : ")

if not (search_path.endswith("/") or search_path.endswith("\\")):
    search_path = search_path + "/"
    f = open("file.txt", "w")
Search_Filename=[]
results = []
for fname in os.listdir(path=search_path):
    if fname.endswith(file_type):
        fo = open(search_path + fname)
        line = fo.readline()
        line_no = 1
        while line != '':
            index = line.find(search_word)
            if (index != -1):
             results.append(line)
             Search_Filename.append(fname)
            line = fo.readline()
            line_no += 1
        fo.close()
#print(*results, sep='\n')
#print(*Search_Filename, sep='\n')
col1 = "File name"
col2 = "Search Word"
data = pd.DataFrame({col1:Search_Filename, col2:results})
data.to_excel('Result.xlsx', sheet_name='sheet1', index=False)

###Feras