"""Вводится строка. Вывести последние два символа этой строки в обратном порядке. Пример: Ввод: “ДОМ”; Вывод: “МО”. Решить не более, чем в две строки."""

s=input('Введите слово ')
print(s[-1], s[-2], sep='')
