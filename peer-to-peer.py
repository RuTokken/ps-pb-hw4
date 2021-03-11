def get_absolute_url(url, *args, **kwargs):
    # Добавляем позиционные аргументы к url
    for i in args:
        url += f'/{i}'
    # После добавления позиционных аргументов добавляем знак вопроса
    url += '?'
    # Добавляем именованные аргументы к url
    for k, v in kwargs.items():
        url += f'{k}={v}&'
    # Убираем из url лишний '&' в конце строки
    url = url[0:-1]
    return url


print(get_absolute_url('www.yandex.ru', 'posts', 'news', id='24', author='admin'))
print(get_absolute_url('www.google.com', 'images', id='24', category='auto', color='red', size='small'))