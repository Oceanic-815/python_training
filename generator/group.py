import random
import string
from model.group import Group
import os.path
import json
import getopt
import sys

# чтение из командной строки
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"]) # n - кол-во генерируемых данных, f - файл, в который данные записываются; ["",""] - подсказки
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

# генерация случайных тестовых данных
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")]+[
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

# запись данных в файл
with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
