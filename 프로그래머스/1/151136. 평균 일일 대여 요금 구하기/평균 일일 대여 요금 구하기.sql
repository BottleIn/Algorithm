SELECT
  DATEDIFF(
    STR_TO_DATE('2021-06-04 07:48:52', '%Y-%m-%d %T'),
    STR_TO_DATE('2021-06-01 12:30:05', '%Y-%m-%d %T')
  ),
  TIMEDIFF(
    STR_TO_DATE('2021-06-04 07:48:52', '%Y-%m-%d %T'),
    STR_TO_DATE('2021-06-01 12:30:05', '%Y-%m-%d %T')
  );