create database assignment_db;
use assignment_db; -- 사용할 스키마 지정

-- employees 테이블 생성
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(100),
    salary DECIMAL(10, 2)
);
-- employees 정보 삽입
INSERT INTO employees (name, position, salary) 
VALUES  ('혜린', 'PM', 90000),
		('은우', 'Frontend', 80000),
		('가을', 'Backend', 92000),
        ('지수', 'Frontend', 78000),
        ('민혁', 'Frontend', 96000),
        ('하온', 'Backend', 130000);