import os
programms = []
os.chdir("C:/Users")
print(os.getcwd())
# распечатать все файлы и папки рекурсивно
for dirpath, dirnames, filenames in os.walk("."):
    # перебрать каталоги
    for dirname in dirnames:
        os.path.join(dirpath, dirname)
    # перебрать файлы
    for filename in filenames:
        if filename[-3::] in ['lnk','exe'] and filename[::-4] not in ['unins000','Update'] and filename[0:1] not in 'ms' and filename[0] != 'j':
        
            programms.append(os.path.join(filename))
for i in range(len(programms)):
    print(programms[i])