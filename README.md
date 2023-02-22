Запуск дистрибутива с гитхаб:
    зайти в терминале в папку StripeAPItask
    запустить переменные окружения: .\env\Scripts\activate.bat
                                    либо для Windows PS:
                                    ./env/Scripts/Activate.ps1
    запустить приложение: python manage.py runserver
    перейти по указанному адресу. 
    superuser Django admin: yury, пароль 12 - можно добавить единицы товара



В приложении реализованы бонусные задачи:

    Запуск используя Docker
    Использование environment variables
    Просмотр Django Моделей в Django Admin панели
    Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items
