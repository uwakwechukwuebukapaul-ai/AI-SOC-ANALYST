-- Sentinel DNA Database Schema

CREATE TABLE IF NOT EXISTS incidents (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    time TEXT NOT NULL,

    threat TEXT NOT NULL,

    severity TEXT NOT NULL,

    risk_score INTEGER DEFAULT 0,

    mitre TEXT DEFAULT 'N/A',

    response_status TEXT DEFAULT 'INVESTIGATION REQUIRED',

    status TEXT DEFAULT 'OPEN',

    evidence TEXT DEFAULT '',

    actions TEXT DEFAULT '[]',

    analyst TEXT DEFAULT '',

    notes TEXT DEFAULT ''

);