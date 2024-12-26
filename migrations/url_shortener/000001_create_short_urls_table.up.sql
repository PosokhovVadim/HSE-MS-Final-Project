CREATE TABLE short_urls IF NOT EXISTS (
    id INTEGER PRIMARY KEY,
    original_url varchar(1024) NOT NULL,
    short_url varchar(1024) NOT NULL
);