CREATE TABLE IF NOT EXISTS url_storage (
    url TEXT PRIMARY KEY CHECK (char_length(url) <= 256),
    ip INET,
    accessed BIGINT DEFAULT 1,
    last_updated TIMESTAMP DEFAULT now(),

    google_safe_browsing_result JSON
);
