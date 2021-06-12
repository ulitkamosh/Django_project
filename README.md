# Веб-приложение на Django

Проект представляет собой клиент-серверное веб-приложения, на котором можно размещать продукты или товары магазина, вести блог и представлять интресы компании, а так же есть возможность создавать аккаунты и администрировать веб-сайт, в том числе и продукции компании, размещенной в приложении.

Веб-приложение спроектированно по структуре MTV (аналогичной MVC). Логика доступа к данным, бизнес-логика и логика отображения — составляют концепцию, которую называют шаблоном Модель-Представление-Управление (Model-View-Controller, MVC) архитектуры программного обеспечения. В этой концепции термин «Модель» относится к логике доступа к данным; термин «Представление» относится к той части системы, которая определяет, что показать и как; а термин «Управление» относится к той части системы, которая определяет какое представление надо использовать, в зависимости от пользовательского ввода, по необходимости получая доступ к модели.
____
## Структура веб-приложения

Методика MVC позволяет функционально разделить приложение на составляющие:
 - [Блог;](https://github.com/ulitkamosh/Django_project/tree/master/blog)
 - [Комментарии;](https://github.com/ulitkamosh/Django_project/tree/master/comments)
 - [Продукты;](https://github.com/ulitkamosh/Django_project/tree/master/products)
 - [Пользователи;](https://github.com/ulitkamosh/Django_project/tree/master/users)
 - [Главный пакет с настройками проэкта.](https://github.com/ulitkamosh/Django_project/tree/master/zavod_mojaysk)
 
### Структура пакетов
- [Слой доступа к данным (Model);](https://github.com/ulitkamosh/Django_project/blob/master/blog/models.py)
- [Слой представления к данным (Template);](https://github.com/ulitkamosh/Django_project/tree/master/blog/templates/blog)
- [Слой бизнес логики (View);](https://github.com/ulitkamosh/Django_project/blob/master/blog/views.py)
    - [Файл URL адресации.](https://github.com/ulitkamosh/Django_project/blob/master/blog/urls.py)

