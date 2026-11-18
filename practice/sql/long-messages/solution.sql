with message_size as 
(select 
  author,
  trim(message) as message,
  length(trim(message)) as message_length,
  avg(length(trim(message))) over() as avg_message
from repo_commits
where message is not null
and message !='')
select 
  author, 
  message,
  message_length
from message_size
where message_length> avg_message
order by message_length desc
