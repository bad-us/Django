Lesson_1
1. Ознакомиться с версткой сайта, над которой будете работать.
2. Подгоовить проект:
a) Создать папку geekshop-server;
б) В папке geekshop-server создать виртуальное окружение;
в) Установить Django версии LTS;
г) Создать проект geekshop (в папке geekshop-server должно быть виртуальное окружение venv и сам проект geekshop);
д) Запустить сервер и убедться, что все работает.
3. Создать приложение products (в методичке = mainapp).
4. Разместить шаблоны и статические файлы в соответствующих папках. Настроить проект – файл settings.py. Отредактировать файл диспетчера URL-адресов urls.py.
5. Написать контроллер для всех страниц (главная и страница с продуктами) – файл views.py в приложении mainapp. Проверить работу всех страниц проекта в черновом режиме (без стилей и изображений).
6. Откорректировать пути к статическим файлам и адреса гиперссылок в меню. Проверить, что все работает как положено (стили и изображения грузятся, гиперссылки работают).
7. Подготовить проект для сдачи на GitHub:
a) Сделать инициализацию гита;
б) Добавить в проект файлы .gitignore (в этот файл добавить .idea, __pycache__/, db.sqlite3) и README.md
в) Связать проект с репозиторием;
г) Создать ветку lesson1;
д) Сделать commit и push (см. статьи, приложенные к уроку);
е) Добавить меня (Vokler) в контребюторы вашего проекта и сделать New Pull Request на меня, чтобы я мог проверить ДЗ.
   
Lesson_2
1. Организовать вывод динамического контента на страницах index и products (список товаров, заголовок страницы).
2. Поработать с шаблонными тегами и placeholder'ами (заглавные буквы, вывод текущей даты в шаблоне).
3. Реализовать в проекте механизмы работы c URL-адресами.
4. Реализовать наследование шаблонов в проекте.
5. Поработать со статическими файлами (убрать статическое объявление статики, переделав на динамическое отображение).
6*. Организовать загрузку динамического контента в контроллер products из json файла (добавив json файл в папку products/fixtures).

Lesson_3
1. Создать модели в проекте (обязательно должно быть поле с изображениями) и выполнить миграции.
2. Поработать с моделями в консоли.
3. Создать суперпользователя. Настроить админку и поработать в ней.
4. Организовать работу с моделями в контроллерах и шаблонах.
5. Настроить проект для работы с медиафайлами (добавить media в .gitignore).
6*. Создать диспетчер URL в приложении. Скорректировать динамические URL-адреса в шаблонах.
7*. Организовать загрузку данных в базу из файла (Django fixtures).
   
Lesson_4
1. Создать модель пользователя в проекте. Обязательно добавить поле с изображением. Выполнить настройки в файле конфигурации.
2. Реализовать механизм аутентификации и авторизации в проекте.
3. Реализовать механизм регистрации пользователя. И не забыть добавить logout.
4*. Создать base.html для login.html и register.html в templates папке приложения users.
5*. Разобраться с механизмом валидации данных формы. Создать свои валидаторы.
   
   
Lesson_5
1. Реализовать механизм редактирования информации о пользователе (личный кабинет) в проекте. Обязательно реализовать механизм загрузки аватара пользователя.
2. Добавиь обработку ошибок для страниц авторизации и регистрации. И добавить сообщения об успешних действиях.
3. Создать приложение корзины. Создать новую модель для корзины.
4. Добавить включенный шаблон basket.html в profile.html. Реализовать вывод товаров корзины.
5. Реализовать механизм добавления и удаление товара корзины.
6. Создать метод sum(), который будет отвечать за вывод итоговой стоимости для товара.
7*. Написать в модели корзины методы для определения общего количества и стоимости добавленных товаров. Вывести эти величины в шаблоне.
8*. Добавить обработку ошибок для страницы профиля (личного кабинета). И добавить сообщения об успешних действиях.
   
Lesson_6
1. Добавить к модели корзины методы total_sum,() и total_quantity() и вывести в меню количество товара и их полную стоимость.
2. Защитить доступ к корзине и личному кабинету декоратором @login_required.
3. Реализовать асинхронное редактирование количества товаров в корзине при помощи AJAX.

Lesson_7
1. Создать приложение админки и интегрировать его в проект.
2. Реализовать механизм CRUD админки на выбор: пользователи, продукты, категории.
3. Защитить доступ к админке декоратором @user_passes_test.
4. Реализовать удаление через свойство is_active.
5*. Преобразовать админку Django (так же на выбор: пользователи, продукты, категории или корзина).

Lesson_8   
1. Организовать фильтрацию продуктов по категориям.
2. Организовать постраничный вывод в каталоге.
3. Перевести как можно больше контроллеров в проекте на CBV.
Обязательно выполнение 3его задания. Это необходимо для следующего уровня!