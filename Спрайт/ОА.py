from zipfile import ZipFile


name = ZipFile('../СР2/input.zip')
for name in name.namelist():
    if name[-1] == '/':
        print(' ' * name.count('/') + name.split('/')[-2])
    else:
        print(' ' * name.count('/') + name.split('/')[-1])