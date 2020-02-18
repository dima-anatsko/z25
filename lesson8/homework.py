"""
Написать !консольную! программу, которая на вход получает имя входного файла,
имя выходного и решает определенную задачу.
Задача программы:
1) По расширению файлов определить какой тип данных в них.
 - <file_name>.json - в файле лежит json
 - <file_name>.csv - лежит csv
 - <file_name>.xml - лежит xml
  - <file_name>.bin - лежит объект, упакованный при помощи pickle
2) Перегнать данные из одного файла в другой соблюдая тип данных
Пример:
python homework6.py data.json data.csv
из json который лежит в data.json сделать csv и положить в файл data.csv
PS: для проверки существования файла можно использовать os.path.exists(<path>)
PSS: для получения аргументов командной строки:
import sys
sys.argv
3) Второй файл в аргументе может быть не указан.
python homework6.py data.json
Если второй аргумент не указан, то данные из файла data.json вывести на экран в
виде питоновского объекта.
PS: глубина вложенности данных - 1
т.е. для xml не может быть вложености глубже тегов внутри тега <item>
<root>
   <item>
      <author>Gambardella, Matthew</author>
      <title>XML Developer's Guide</title>
      <genre>Computer</genre>
      <price>44.95</price>
      <publish_date>2000-10-01</publish_date>
      <description>An in-depth look at creating applications
      with XML.</description>
   </item>
   <item>
      <author>Ralls, Kim</author>
      <title>Midnight Rain</title>
      <genre>Fantasy</genre>
      <price>5.95</price>
      <publish_date>2000-12-16</publish_date>
      <description>A former architect battles corporate zombies,
      an evil sorceress, and her own childhood to become queen
      of the world.</description>
   </item>
</root>
для json не могут быть объекты внутри объектов
"""


import json
import sys

import xml.etree.ElementTree as eTree


def get_files(argv):
    argv = argv[1:]
    arg_len = len(argv)
    if arg_len > 2 or not arg_len:
        raise Exception("Invalid input")
    if arg_len == 2:
        input_file, output_file = argv
    else:
        input_file, output_file = argv[0], None
    return input_file, output_file


def get_extension(file_name):
    divided = file_name.rsplit('.', 1)
    if len(divided) != 2 or not divided[0]:
        raise Exception('Invalid file name')
    return divided[-1]


def read_json(file_name):
    file = open(file_name)
    data = file.read()
    file.close()
    return json.loads(data)


def write_json(file_name, data):
    file = open(file_name, 'w')
    file.write(json.dumps(data, indent=4))
    file.close()


def read_xml(file_name):
    file = open(file_name)
    tree = eTree.parse(file)
    root = tree.getroot()
    result = []
    for item in root:
        element = {}
        for child in item:
            element[child.tag] = child.text
        result.append(element)
    file.close()
    return result


def write_xml(file_name, data):
    root = ''
    tag_str = "<{tag}>{text}</{tag}>"
    for item in data:
        item_str = ''
        for tag, text in item.items():
            item_str += tag_str.format(
                tag=tag,
                text=text
            ) + '\n'
        root += f'\t<item>\n\t\t{item_str}\n\t</item>'
    file = open(file_name, 'w')
    file.write(f'<root>\n{root}\n</root>')
    file.close()


def write_console(file_name, data):
    print(data)


def get_functions(ext):
    functions = {
        'json': (read_json, write_json),
        'xml': (read_xml, write_xml),
        None: (None, write_console)
    }
    if ext not in functions:
        raise Exception('Invalid extension')
    return functions[ext]


if __name__ == '__main__':
    input_file, output_file = get_files(sys.argv)
    input_ext = get_extension(input_file)
    output_ext = None
    if output_file:
        output_ext = get_extension(output_file)

    read_function = get_functions(input_ext)[0]
    write_function = get_functions(output_ext)[1]

    data = read_function(input_file)
    write_function(output_file, data)
