-- SQLite

-- 테이블 생성
-- 정호,유,40,전라북도,016-7280-2855,370
CREATE TABLE user (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);
