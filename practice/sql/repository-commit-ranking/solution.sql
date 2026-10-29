select repo_name,
       sum(added) as total_added,
       dense_rank() over(order by sum(added) desc) as rank
 from repo_commits
group by repo_name
