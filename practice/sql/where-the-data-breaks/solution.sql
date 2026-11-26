select 
  tbl_name,
  count(distinct case when passed = 0 then check_id end) as failing_checks,
  count(distinct case when lower(severity) in ('high', 'critical') and passed = 0 then check_id end) as high_severity_failures
from dq_checks
group by tbl_name
order by failing_checks desc
