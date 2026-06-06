alter table public.identity_link enable row level security;
alter table public.profiles enable row level security;
alter table public.match_invitations enable row level security;
alter table public.mutual_matches enable row level security;
alter table public.messages enable row level security;

create policy "owner can read identity link"
  on public.identity_link for select
  using (clerk_user_id = auth.jwt() ->> 'sub');

create policy "owner can read own profile"
  on public.profiles for select
  using (
    exists (
      select 1 from public.identity_link i
      where i.pseudo_id = profiles.pseudo_id
      and i.clerk_user_id = auth.jwt() ->> 'sub'
    )
  );

create policy "owner can update own profile"
  on public.profiles for update
  using (
    exists (
      select 1 from public.identity_link i
      where i.pseudo_id = profiles.pseudo_id
      and i.clerk_user_id = auth.jwt() ->> 'sub'
    )
  );
