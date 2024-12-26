FROM base

ENV CONFIG_PATH todo_service/config/config.yaml

ENV SQLITE_DATABASE=sqlite:////data/tasks/data.db

CMD ["sh", "-c", "sqlite3 /data/tasks/data.db < /docker-entrypoint-initdb.d/init.sql && poetry run todo-service" ]