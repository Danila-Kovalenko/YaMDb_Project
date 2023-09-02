# infra_sp2
API для получения информации и обсуждения наиболее интересных произведений

### Документация:
Для просмотра документации используйте эндпойнт `redoc/`

### Запуск:

- Склонируйте репозитрий на свой компьютер
- Создайте `.env` файл в директории `infra/`
- Из папки `infra/` соберите образ при помощи docker-compose
`$ docker-compose up -d --build`
- Примените миграции
`$ docker-compose exec web python manage.py migrate`
- Соберите статику
`$ docker-compose exec web python manage.py collectstatic --no-input`
- Для доступа к админке не забудьте создать суперюзера
`$ docker-compose exec web python manage.py createsuperuser`
