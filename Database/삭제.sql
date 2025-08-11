use assignment_db; -- 사용할 스키마 지정

-- 민혁 사원의 데이터 삭제
delete from employees
where name = '민혁';

-- employees 테이블을 삭제
drop table employees;