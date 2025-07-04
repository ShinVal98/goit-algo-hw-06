# Завдання: Порівняння DFS і BFS у графі метро

У цьому завданні я реалізувала алгоритми **DFS** (пошук у глибину) та **BFS** (пошук у ширину), щоб знайти шлях у змодельованому мною графі транспортної мережі метро.

## Ціль

Знайти маршрут між станціями **Park** та **Airport** за допомогою обох алгоритмів і порівняти їхні результати.

## Результати

- **DFS шлях**:  
  `Park → Museum → Central → North → Library → Airport`

- **BFS шлях**:  
  `Park → Museum → Central → East → Airport`

## Порівняння алгоритмів

| Критерій                | DFS                                   | BFS                                    |
|-------------------------|---------------------------------------|----------------------------------------|
| Принцип обходу          | Переходить якомога глибше             | Обходить граф пошарово                 |
| Знайдений шлях          | Не обов’язково найкоротший            | Найкоротший за кількістю кроків        |
| Шлях у графі метро      | Через Library                         | Через East                             |
| Пам’яттєва ефективність | Вищий ризик переповнення стека        | Більше пам’яті, але стабільніше        |

## Висновок

- **DFS** може бути корисним для повного обходу або в задачах, де не критично знайти найкоротший шлях.
- **BFS** ідеально підходить для знаходження **найкоротших маршрутів** у невагомих графах, таких як транспортні або соціальні мережі.

> У моєму графі метро **BFS виявився ефективнішим**, оскільки одразу привів до коротшого шляху до станції Airport.

---
