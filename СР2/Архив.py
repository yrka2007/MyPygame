from zipfile import ZipFile


def human_read_format(size):
    val = ['Б', "КБ", "МБ", "ГБ", "ТБ", "ПБ", "ЭБ", "ЗБ", "ЙБ", "РБ", "КВБ", "РОБ"]
    sz = size
    count = 0
    while True:
        sz //= 1024
        if sz == 0:
            break
        count += 1
    return f'{round(size / 1024 ** count)}{val[count]}'


zipf = ZipFile('input.zip')
for file in zipf.filelist:
    name = file.filename
    if name[-1] == '/':
        print('  ' * (name.count('/') - 1) + name.split('/')[-2])
    else:
        print('  ' * name.count('/') + name.split('/')[-1], human_read_format(file.file_size))
