FROM base

ENV CONFIG_PATH url_shortener/config/config.yaml

ENV SQLITE_DATABASE=sqlite:////data/urls/data.db

CMD ["sh", "-c", "sqlite3 /data/urls/data.db < /docker-entrypoint-initdb.d/init.sql && poetry run url-shortener" ]
