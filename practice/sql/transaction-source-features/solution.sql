select 
 distinct feat_name
from ml_features
where avg_val is null
and source = 'user_sessions'
order by feat_name
