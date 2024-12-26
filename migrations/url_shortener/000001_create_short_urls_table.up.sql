CREATE TABLE IF NOT EXISTS short_urls (
    id INTEGER PRIMARY KEY,
    original_url varchar(1024) NOT NULL,
    short_id varchar(1024) NOT NULL
);