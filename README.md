# Не баг, а фича

Единый учебный репозиторий бригады № 1 по дисциплине «Введение в профессиональную деятельность» в РГРТУ имени В. Ф. Уткина. Текущий этап: самостоятельная работа № 2, организация репозитория и совместной работы с Git.

## Назначение проекта

**Тема проекта:** № 16. «Помощник по выбору ноутбука для обучения».

Назначение проекта: подготовка учебного прототипа веб-сайта, который помогает выбирать ноутбук для обучения. На текущем этапе организованы командный репозиторий, документация и распределение ответственности в Git.

## Состав команды

| Участник | Роль | GitHub |
| --- | --- | --- |
| Двойных Никита Константинович | Лидер команды | [karasik115](https://github.com/karasik115) |
| Алиева Софья Эльдаровна | Менеджер | [soniikaka](https://github.com/soniikaka) |
| Аванесова Анастасия Денисовна | Дизайнер UI/UX | [NASSS1E](https://github.com/NASSS1E) |
| Гришин Андрей Александрович | Программист | [1Andrey0](https://github.com/1Andrey0) |
| Аляпкин Никита Игоревич | Специалист по БД | [N1kr0man](https://github.com/N1kr0man) |
| Шушкин Артем Олегович | Тестировщик QA | [artiomshushkin-lang](https://github.com/artiomshushkin-lang) |

## Основные документы

- [Правила взаимодействия команды](docs/team-contract.md).
- [Роли, обоснования выбора, профессиональные стандарты и эссе](docs/roles-and-responsibilities.md).
- [Матрица RACI первого этапа и обязанностей в Git](docs/raci-matrix.md).

## Практические работы

| Работа | Тема | Отчёт | Материалы |
| --- | --- | --- | --- |
| 01 | Профессиональные роли и формирование команды | [report.md](practical-works/practical-work-01/report.md) | [assets](practical-works/practical-work-01/assets/) |
| 02 | Организация работы с репозиторием и распределение ответственности в Git | [report.md](practical-works/practical-work-02/report.md) | [assets](practical-works/practical-work-02/assets/) |
| 03 | Определение целевой аудитории | [report.md](practical-works/practical-work-03/report.md) | [src](practical-works/practical-work-03/src/) |
| 04 | Выявление функциональных требований методом мозгового штурма | [report.md](practical-works/practical-work-04/report.md) | [src](practical-works/practical-work-04/src/) |
| 05 | Разработка интерфейса | [report.md](practical-works/practical-work-05/report.md) | [src](practical-works/practical-work-05/src/) |
| 06 | Разработка прототипа | [report.md](practical-works/practical-work-06/report.md) | [src](practical-works/practical-work-06/src/) |
| 07 | Проверка прототипа и доработка | [report.md](practical-works/practical-work-07/report.md) | [src](practical-works/practical-work-07/src/) |
| 08 | Подготовка и защита итогового решения | [report.md](practical-works/practical-work-08/report.md) | [src](practical-works/practical-work-08/src/) |

Работа № 1 содержит материалы формирования команды. Работа № 2 содержит отчёт об организации репозитория; личная работа участников с ветками, коммитами и ревью продолжается. Для работ № 3–8 оставлены только папки и файлы-заготовки по структуре СР2.

## Порядок совместной работы

1. Каждый участник регистрируется на GitHub и сообщает свой точный логин лидеру для добавления доступа к приватному репозиторию.
2. Клонирует репозиторий на свой компьютер: `git clone https://github.com/karasik115/team-ne-bag-a-ficha-project.git`.
3. Создаёт свою ветку `feature/<имя_участника>` или `role/<название_роли>`.
4. Вносит изменения в материалы своей роли, делает осмысленный коммит и отправляет ветку на GitHub.
5. Создаёт Pull Request в `main`, получает ревью другого участника и передаёт изменения на слияние лидеру.

Команды и рекомендуемые ветки для каждого участника приведены в [отчёте № 2](practical-works/practical-work-02/report.md).

## Структура и проверка

Структура соответствует образцу СР2: `README.md`, `docs/`, восемь папок в `practical-works/`, `scripts/` и `.gitignore`. В каждой работе есть `report.md`; в работах № 1–2 предусмотрены `assets/`, в работах № 3–8 `src/`. Пустые папки сохраняются в Git с помощью `.gitkeep`. Скриншоты СР2 размещены в `practical-works/practical-work-02/assets/`.

Из корня репозитория можно выполнить проверку:

```sh
python scripts/check_structure.py
```
