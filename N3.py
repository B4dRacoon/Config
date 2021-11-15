note = open('civgraph.txt', 'r')

old_a = ""
arr_a = []
arr_b = []
out_line = ".PHONY: info all clean list\ninfo: all clean\n\t@echo *info about make*\n"
flag = 1


for line in note:
    if "->" in line:
        a, b = line.split(" -> ")
        if "];" in b:
            c, d = b.split()
            a = a.replace(" ", "")
            c = c.replace(" ", "")
            arr_b.append(c)
            if old_a != a:
                if flag != 1:
                    out_line += "\n\t@echo make " + old_a + "\n" + a + ": " + c
                else:
                    out_line += a + ": " + c
            else:
                out_line += " " + c
            old_a = a
            arr_a.append(a)

        else:
            b = b.replace(";", "")
            b = b.replace("\n", "")
            b = b.replace(" ", "")
            a = a.replace(" ", "")
            arr_b.append(b)
            if old_a != a:
                if flag != 1:
                    out_line += "\n\t@echo make " + old_a + "\n" + a + ": " + b
                else:
                    out_line += a + ": " + b
            else:
                out_line += " " + b
            old_a = a
            arr_a.append(a)
        flag += 1

note.close()
out_line += "\n\t@echo make " + old_a

for element in arr_b:
    if element + ":" not in out_line:
        out_line += "\n" + element + ":" + "\n\t@echo make " + element

out_line += "\nall: " + arr_a[0]

out_line += "\nclean:\n\t@echo *Files have been deleted*\nlist:\n\t@grep '^[^#[:space:]].*:' Makefile"



inp = open('makefile', 'w')
inp.write(out_line)
inp.close()