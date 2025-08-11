use assignment_db; -- 사용할 스키마 지정

-- 직원 테이블에서 이름과 연봉을 조회
select name, salary from employees;

-- Frontend 직책을 가진 직원 중에서 연봉이 90000 이하인 직원의 이름과 연봉 조회
select name, salary from employees as e where e.position = 'Frontend'  and salary <= 90000;

-- 모든 직원을 position 별로 그룹화하여 각 직책의 평균 연봉을 계산
select position, avg(salary) as '평균 연봉' from employees group by position;