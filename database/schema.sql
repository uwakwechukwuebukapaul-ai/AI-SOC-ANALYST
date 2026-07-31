-- ==========================================
-- Sentinel DNA Production Database Schema
-- ==========================================


PRAGMA foreign_keys = ON;



-- ==========================================
-- CASE MANAGEMENT
-- ==========================================

CREATE TABLE IF NOT EXISTS cases (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    case_id TEXT UNIQUE NOT NULL,

    title TEXT NOT NULL,

    severity TEXT NOT NULL,

    description TEXT DEFAULT '',

    status TEXT DEFAULT 'OPEN',

    analyst TEXT DEFAULT '',

    created TEXT NOT NULL

);



-- ==========================================
-- CASE NOTES
-- ==========================================

CREATE TABLE IF NOT EXISTS case_notes (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    case_id TEXT NOT NULL,

    note TEXT NOT NULL,

    analyst TEXT DEFAULT '',

    created TEXT NOT NULL,


    FOREIGN KEY(case_id)

    REFERENCES cases(case_id)

    ON DELETE CASCADE

);



-- ==========================================
-- DIGITAL EVIDENCE
-- ==========================================

CREATE TABLE IF NOT EXISTS evidence (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    case_id TEXT NOT NULL,

    type TEXT NOT NULL,

    data TEXT NOT NULL,

    sha256 TEXT NOT NULL,

    collected_by TEXT DEFAULT 'SYSTEM',

    created TEXT NOT NULL,


    FOREIGN KEY(case_id)

    REFERENCES cases(case_id)

    ON DELETE CASCADE

);



-- ==========================================
-- INVESTIGATION TIMELINE
-- ==========================================

CREATE TABLE IF NOT EXISTS timeline (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    case_id TEXT NOT NULL,

    event_type TEXT NOT NULL,

    description TEXT NOT NULL,

    actor TEXT DEFAULT 'SYSTEM',

    created TEXT NOT NULL,


    FOREIGN KEY(case_id)

    REFERENCES cases(case_id)

    ON DELETE CASCADE

);



-- ==========================================
-- PERFORMANCE INDEXES
-- ==========================================


CREATE INDEX IF NOT EXISTS idx_cases_status

ON cases(status);



CREATE INDEX IF NOT EXISTS idx_cases_severity

ON cases(severity);



CREATE INDEX IF NOT EXISTS idx_timeline_case

ON timeline(case_id);



CREATE INDEX IF NOT EXISTS idx_evidence_case

ON evidence(case_id);



CREATE INDEX IF NOT EXISTS idx_notes_case

ON case_notes(case_id);