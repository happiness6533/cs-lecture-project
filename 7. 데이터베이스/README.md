## 데이터베이스

```mysql
-- 조인 x --
SELECT 
    DISTINCT 
    애트리뷰트 AS 별명
    AVG(애트리뷰트) AS 별명, 
    COUNT(애트리뷰트) AS 별명, 
    MAX(애트리뷰트) AS 별명, 
    MIN(애트리뷰트) AS 별명,
    SUM(애트리뷰트) AS 별명,
    CASE WHEN 
        애트리뷰트1 조건 THEN 값 변경
        애트리뷰트2 조건 THEN 값 변경
        END AS 별명 => CASE는 추가 정리가 필요함
FROM 
    테이블 이름 AS 별명
WHERE 
    애트리뷰트 BETWEEN LIKE IN (AND/OR) (IS NULL / IS NOT NULL) (등호/부등호)
    애트리뷰트 = IN ANY EXISTS ALL (중첩질의) => 중첩 질의 구조는 조인으로 바꿔 할 수 있다
GROUP BY 
    애트리뷰트 => 이렇게 되면 해당 애트리뷰트로 행들이 합쳐지므로 SELECT 절에 반드시 그룹화 애트리뷰트 혹은 집단함수만 쓸 수 있다
HAVING
    애트리뷰트에 대한 조건 => 그룹화 애트리뷰트 또는 집단함수에 대해서만 조건 적용 가능
ORDER BY 
    애트리뷰트1 (ASC/DESC), 애트리뷰트2(ASC/DESC)        

-- 조인 o --
SELECT 
    DISTINCT  
    애트리뷰트 AS 별명
    AVG(애트리뷰트) AS 별명, 
    COUNT(애트리뷰트) AS 별명, 
    MAX(애트리뷰트) AS 별명, 
    MIN(애트리뷰트) AS 별명,
    SUM(애트리뷰트) AS 별명,
FROM 
    테이블1 이름 AS 별명
    테이블2 이름 AS 별명
    (중첩질의) 테이블3별명
WHERE 
    테이블1.애트리뷰트 = 테이블2.애트리뷰트 => 동등조인
    테이블1.애트리뷰트 = 테이블1.애트리뷰트 => 내부조인(거의 안씀)
GROUP BY 
    애트리뷰트 => 이렇게 되면 해당 애트리뷰트로 행들이 합쳐지므로 SELECT 절에 반드시 그룹화 애트리뷰트 혹은 집단함수만 쓸 수 있다
HAVING
    애트리뷰트에 대한 조건 => 그룹화 애트리뷰트 또는 집단함수에 대해서만 조건 적용 가능
ORDER BY 
    애트리뷰트 (ASC/DESC)

-- 기타 --
INSERT INTO 릴레이션(애트리뷰트1, ..., 애트리뷰트n) VALUES (값1, ..., 값n)
INSERT INTO 릴레이션(애트리뷰트1, ..., 애트리뷰트n) 셀렉션 연산으로
DELETE FROM 릴레이션 WHERE 조건
UPDATE 릴레이션 SET 애트리뷰트 = 값 또는 식[, …] WHERE 조건
DATE => 시간만 추출 => HOUR(DATE)
```