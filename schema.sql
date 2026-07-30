-- APEX — early access requests (D1)
CREATE TABLE IF NOT EXISTS early_access_requests (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  name        TEXT NOT NULL,
  email       TEXT NOT NULL,
  pack        TEXT NOT NULL,
  bike        TEXT,
  usage       TEXT,
  lang        TEXT,
  consent     INTEGER NOT NULL DEFAULT 0,
  created_at  TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_ea_created ON early_access_requests (created_at);
