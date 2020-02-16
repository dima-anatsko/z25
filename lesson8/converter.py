import csv
import json
import os
import pickle
import sys
import xml.etree.ElementTree as eTree


def my_csv(path, action='r', obj=None):
    if action == 'r':
        file = open(path, action)
        obj = list(csv.DictReader(file))
        file.close()
    elif action == 'w':
        headers = obj[0].keys()
        file = open(path, action)
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(obj)
        file.close()
    return obj


def my_xml(path, action='r', obj=None):
    if action == 'r':
        file = open(path, action)
        tree = eTree.parse(file)
        file.close()
        root = tree.getroot()
        obj = [{child.tag: child.text for child in user} for user in root]
    elif action == 'w':
        temp = []
        for key in obj[0]:
            temp.append(f'\t<{key}>{{{key}}}</{key}>\n')
        string = '<person>\n' + ''.join(temp) + '</person>\n'
        result = []
        for item in obj:
            result.append(string.format(**item))
        result_str = ''.join(result)
        result_str = f'<root>\n{result_str}\n</root>'
        file = open(path, action)
        file.write(result_str)
        file.close()
    return obj


def my_json(path, action='r', obj=None):
    if action == 'r':
        file = open(path, action)
        obj = json.load(file)
        file.close()
    elif action == 'w':
        file = open(path, action)
        file.write(json.dumps(obj, indent=4))
        file.close()
    return obj


def my_pickle(path, action='r', obj=None):
    if action == 'r':
        file = open(path, 'rb')
        obj = pickle.load(file)
        file.close()
    elif action == 'w':
        file = open(path, 'wb')
        pickle.dump(obj, file)
        file.close()
    return obj


def check_arg(_ext):
    in_file, out_file = None, None
    in_ext, out_ext = None, None
    if len(sys.argv) > 1:
        in_file = sys.argv[1]
        try:
            in_ext = in_file.rsplit('.', 1)[1]
        except IndexError:
            raise SystemExit('Нет расширения у входного файла')
        if in_ext not in _ext:
            raise SystemExit('Неверное расширения у входного файла')
        if len(sys.argv) == 3:
            out_file = sys.argv[2]
            try:
                out_ext = out_file.rsplit('.', 1)[1]
            except IndexError:
                print('Нет расширения у выходного файла')
            if out_ext not in _ext:
                print('Неверное расширения у выходного файла')
                out_file, out_ext = None, None
    else:
        raise SystemExit('Для работы утилиты нужны 1 либо 2 аргумента')
    return in_file, in_ext, out_file, out_ext


if __name__ == "__main__":
    ext = {'csv': my_csv, 'json': my_json, 'xml': my_xml, 'bin': my_pickle}
    input_file, input_ext, output_file, output_ext = check_arg(ext.keys())
    if not os.path.exists(input_file):
        raise SystemExit('Входного файла по этому пути не существует')
    py_obj = ext[input_ext](input_file)
    if output_file is None:
        print(py_obj)
    else:
        ext[output_ext](output_file, 'w', py_obj)
