def proggs():
    import os
    programms = []
    '''print('Здравствуйте,уважаемый пользователь.Выберете ваш остновной диск,на котором у вас установаленна Win11')
    a = input()
    os.chdir(f'{}:/AppData/Roaming/Microsoft/Windows/Start Menu')'''
    a = 'C:/Users/ssfs9/AppData/Roaming/Microsoft/Windows/Start Menu'
    os.chdir(a)
    # распечатать все файлы и папки рекурсивно
    for root, dirs, filenames in os.walk("."):
        # перебрать каталоги
        path = root.split(os.sep)
        global_way = a+root[1::].replace('\\','/')
        for dirname in dirs:
            os.path.join(dirname)
        os.path.basename(root)
        for file in filenames: 
                programms.append(file)
        return global_way
print(proggs())