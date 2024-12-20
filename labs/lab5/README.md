# Лабораторна робота №5: Аналіз Рядка

## Опис проекту
Додаток для аналізу рядка, який перевіряє наявність паліндрому та повторів слів, реалізований з використанням графічного інтерфейсу FreeSimpleGUI.

## Функціональність
### Основні можливості
- Перевірка рядка на паліндром
- Виявлення повторів слів довжиною більше 3 символів
- Зручний графічний інтерфейс для введення та аналізу

### Особливості реалізації
- Використання власного класу `Povtory`, що успадковується від `str`
- Методи перевірки:
  - `palindrome()`: Перевірка на паліндром
  - `povtory_sliv()`: Пошук повторів слів

## Технічні деталі
### Клас `Povtory`
- Успадкований від базового класу `str`
- Додаткові методи для аналізу рядка
- Робота з регістром незалежно від введення

### Методи класу
- `palindrome()`: 
  - Перетворює рядок до нижнього регістру
  - Перевіряє читання рядка з кінця до початку
- `povtory_sliv()`:
  - Розділяє рядок на слова
  - Фільтрує слова довжиною більше 3 символів
  - Перевіряє наявність повторів

## Вимоги
- Python 3.x
- Бібліотека FreeSimpleGUI

## Запуск програми
Запуск здійснюється через головний графічний інтерфейс:

```bash
python gui.py
```

Після цього:
- Оберіть лабораторну роботу №5 у списку
- Натисніть кнопку "Запустити"

### Кроки використання
1. Введіть рядок у текстове поле
2. Натисніть кнопку "Перевірити"
3. Перегляньте результати аналізу

## Обробка помилок
- Перевірка на порожній рядок
- Інформативні повідомлення про результати аналізу

## Особливості інтерфейсу
- Тема оформлення "DarkTeal9"
- Шрифт "Comic Sans"
- Проста та зрозуміла навігація



