import re

path = "/etc/hosts"

file = open(path, "rt")
data = file.read()

data = re.sub(r"###---------- free-spotify ----------###([\s\S]*)###---------- made by @harrytran103 ----------###", "", data)
data = data.strip("\n")

file.close()
file = open(path, "wt")
file.write(data)
file.close()

print("uninstall free-spotify successfully")
