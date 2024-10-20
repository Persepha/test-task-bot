
# Тестовое задание




## Built in

- SQLAlchemy - orm
- Alembic for migrations
- Pydantic for data validation
- SQLite db



## Env

Add TOKEN in env file

Poetry is used to manage dependencies, Python 3.11 is required.


```bash
  poetry install
  poetry run python -m tasks_ptb
```
## Bot commands

- /start — приветственное сообщение
- /help — справка
- /tasks — список задач
- /add Название задачи, Срок выполнения, Статус — добавить задачу
- /del Id задачи <br>
- /upd ID Задачи, Название задачи, Срок выполнения, Статус — добавить задачу<br>



