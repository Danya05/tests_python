import sys
import zipfile, os
from io import StringIO


class QuadraticPolynomial:    # ЗДЕСЬ ПИСАТЬ ТЕСТИРУЕМУЮ ФУНКЦИЮ ИЛИ КЛАСС
    pass



with zipfile.ZipFile('15.zip', 'r') as zp:  # с новым заданием меняется имя архива (АРХИВ В ПАПКЕ С ФАЙЛОМ ЭТОГО КОДА)
    extract_dir = zp.filename.split('.')[0]
    if not os.path.isdir(extract_dir):
        zp.extractall(extract_dir)
    os.chdir(extract_dir)
    count = 0
    answers = []
    for file in os.listdir(os.getcwd()):
        if os.path.splitext(file)[1] == '.clue':

            with open(file, 'r', encoding='utf-8') as f:
                ans = f.read()

                print(*ans, sep='')
                if res:
                    print('\033[32m OK' if res.rstrip() == ans else '\033[31m FALSE')
                    answers.append('\033[32m OK' if res.rstrip() == ans else '\033[31m FALSE')
            print(f'\033[30m ')

        else:
            count += 1
            print(f'\033[30m test {count}')
            with open(file, 'r', encoding='utf-8') as f:
                r = f.readlines()
                print(r)
                tmp_stdout = sys.stdout
                tmp = StringIO()
                sys.stdout = tmp
                exec(''.join(r))
                sys.stdout = tmp_stdout
                res = tmp.getvalue()
                print(f'\033[30m{res}', end='')


print('Результаты тестов:', *answers)
