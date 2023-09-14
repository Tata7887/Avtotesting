"""
Задание 2. (повышенной сложности). Доработать функцию из предыдущего задания таким образом,
чтобы у нее появился дополнительный режим работы, в котором вывод разбивается на слова
с удалением всех знаков пунктуации (их можно взять из списка string.punctuation модуля string).
В этом режиме должно проверяться наличие слова в выводе.
"""

import subprocess
import string


def check_output(cmd, txt):
    out = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    print(out.stdout)
    check_str = out.stdout.translate(str.maketrans('', '', string.punctuation)).split("\n")
    if out.returncode == 0:
        for el in check_str:
            print(el)
            if txt in el:
                return True
        return False
    else:
        return f'error command: {cmd}'


cmd = "cat /etc/os-release"
txt = "ubuntu"

print(check_output(cmd, txt))