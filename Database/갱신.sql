use assignment_db; -- 스키마 지정

-- PM 직책을 가진 모든 직원의 연봉을 10% 인상한 후 결과 확인
update employees
set salary = salary * 1.1
where position = 'PM';
select * from employees;

-- 모든 Backend 직책을 가진 직원의 연봉을 5% 인상
update employees
set salary = salary * 1.05
where position = 'Backend';