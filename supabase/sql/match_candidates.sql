create or replace view public.match_candidates as
select
  viewer.pseudo_id as viewer_pseudo_id,
  candidate.pseudo_id as candidate_pseudo_id,
  case
    when viewer.metro_region = candidate.metro_region then 1.0
    else 0.0
  end as metro_score,
  jsonb_array_length(
    coalesce(viewer.activity_features -> 'preferred_activity_types', '[]'::jsonb)
  ) as viewer_activity_count
from public.profiles viewer
join public.profiles candidate
  on viewer.pseudo_id <> candidate.pseudo_id
 and viewer.metro_region = candidate.metro_region;
