import xlrd
import json
import collections
import io

book = xlrd.open_workbook("localization.xlsx")
sh = book.sheet_by_index(0)
f = ['en', 'fr', 'it', 'de', 'es', 'pt', 'ru', 'ja', 'zh', 'pt-brasil', 'ko']

with open ("TextIds.h", 'w') as file:
	file.write("#ifndef __TEXT_IDS_H__\n")
	file.write("#define __TEXT_IDS_H__\n")
	file.write("\n")
	file.write("enum TextId{\n")
	for rx in range(sh.nrows):
		if (rx == 0):
			continue
		ID = sh.cell_value(rx, 0)
		file.write('    ' + ID.upper())
		if (rx < sh.nrows - 1):
			file.write(",")
		file.write("\n")
	file.write("};\n")
	file.write("\n")

	file.write("const char* textIds[] = {\n")
	for rx in range(sh.nrows):
		if (rx == 0):
			continue
		ID = sh.cell_value(rx, 0)
		file.write('    ' + "\"" + ID + "\"")
		if (rx < sh.nrows - 1):
			file.write(",")
		file.write("\n")
	file.write("};\n")
	file.write("\n")
	file.write("#endif /* defined(__TEXT_IDS_H__) */")
	file.close

#starting column for localization
column = 2
for lang in f:
	with open(lang + '.json', 'w', encoding='utf-8') as file:
		file.write("{\n")
		for rx in range(sh.nrows):
			if (rx == 0):
				continue
			ID = sh.cell_value(rx, 0)
			value = sh.cell_value(rx, column)
			entry = "    \"" + ID + "\" :" + "\"" + value + "\""
			if (rx < sh.nrows - 1):
				entry += ","
			entry += "\n" 
			file.write(entry)
		file.write("}\n")
		file.close()
	column += 1