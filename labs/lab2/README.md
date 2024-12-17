# Лабораторна робота №2: Функції у мові Python

## Опис проекту

Додаток демонструє роботу з пошуком елемента у випадково згенерованому списку цілих чисел.

## Функціональність

### Основні можливості
- Генерація випадкового списку цілих чисел
- Пошук елемента у списку
- Виведення індексу знайденого елемента
- Обробка різних сценаріїв введення

### Компоненти проекту
- `function.py`: Модуль з функцією пошуку елемента
- `lab2.py`: Основний скрипт з логікою роботи

## Технічні деталі

### Функція пошуку `find_element()`
- Приймає список та число для пошуку
- Повертає індекс елемента, якщо знайдено
- Повертає `-200`, якщо елемент не знайдено

### Логіка роботи
1. Генерація випадкового списку цілих чисел
2. Введення числа для пошуку
3. Виконання пошуку
4. Виведення результату

## Вимоги

- Python 3.x
- Бібліотека FreeSimpleGUI
- Модуль random

## Запуск програми

Запуск здійснюється через головний графічний інтерфейс:

```bash
python gui.py
```

Після цього:
- Оберіть лабораторну роботу №2 у списку
- Натисніть кнопку "Запустити"

## Обробка помилок
- Перевірка коректності введення чисел
- Повідомлення про помилки введення
- Можливість безпечного виходу з програми

## Особливості інтерфейсу
- Тема оформлення "DarkTeal9"
- Шрифт "Comic Sans"
- Діалогові вікна для введення та виведення інформації