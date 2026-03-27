WITH FISH_INFO_NEW AS (
    -- 10cm 이하(NULL)를 10으로 치환하여 전처리
    SELECT 
        FISH_TYPE, 
        IFNULL(LENGTH, 10) AS LENGTH
    FROM FISH_INFO
)

SELECT 
    COUNT(*) AS FISH_COUNT,    -- 잡은 수
    MAX(LENGTH) AS MAX_LENGTH, -- 최대 길이
    FISH_TYPE                  -- 물고기 종류
FROM FISH_INFO_NEW
GROUP BY FISH_TYPE
HAVING AVG(LENGTH) >= 33       -- 평균 길이가 33cm 이상인 그룹만 필터링
ORDER BY FISH_TYPE ASC;