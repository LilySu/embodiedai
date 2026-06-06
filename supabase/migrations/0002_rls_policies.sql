alter table public.identity_link enable row level security;
alter table public.profiles enable row level security;
alter table public.match_invitations enable row level security;
alter table public.mutual_matches enable row level security;
alter table public.messages enable row level security;

create policy "owner can read identity link"
  on public.identity_link for select
  using (clerk_user_id = auth.jwt() ->> 'sub');

create policy "owner can create identity link"
  on public.identity_link for insert
  with check (clerk_user_id = auth.jwt() ->> 'sub');

create policy "owner can read own profile"
  on public.profiles for select
  using (
    exists (
      select 1 from public.identity_link i
      where i.pseudo_id = profiles.pseudo_id
      and i.clerk_user_id = auth.jwt() ->> 'sub'
    )
  );

create policy "owner can create own profile"
  on public.profiles for insert
  with check (
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

create policy "participants can read invitations"
  on public.match_invitations for select
  using (
    exists (
      select 1 from public.identity_link i
      where i.clerk_user_id = auth.jwt() ->> 'sub'
      and i.pseudo_id in (match_invitations.sender_pseudo_id, match_invitations.recipient_pseudo_id)
    )
  );

create policy "owner can create sent invitations"
  on public.match_invitations for insert
  with check (
    exists (
      select 1 from public.identity_link i
      where i.pseudo_id = match_invitations.sender_pseudo_id
      and i.clerk_user_id = auth.jwt() ->> 'sub'
    )
  );

create policy "recipient can update invitation status"
  on public.match_invitations for update
  using (
    exists (
      select 1 from public.identity_link i
      where i.pseudo_id = match_invitations.recipient_pseudo_id
      and i.clerk_user_id = auth.jwt() ->> 'sub'
    )
  )
  with check (
    exists (
      select 1 from public.identity_link i
      where i.pseudo_id = match_invitations.recipient_pseudo_id
      and i.clerk_user_id = auth.jwt() ->> 'sub'
    )
  );

create policy "participants can read mutual matches"
  on public.mutual_matches for select
  using (
    exists (
      select 1 from public.identity_link i
      where i.clerk_user_id = auth.jwt() ->> 'sub'
      and i.pseudo_id in (mutual_matches.pseudo_id_a, mutual_matches.pseudo_id_b)
    )
  );

create policy "participants can create mutual matches"
  on public.mutual_matches for insert
  with check (
    exists (
      select 1 from public.identity_link i
      where i.clerk_user_id = auth.jwt() ->> 'sub'
      and i.pseudo_id in (mutual_matches.pseudo_id_a, mutual_matches.pseudo_id_b)
    )
  );

create policy "match participants can read messages"
  on public.messages for select
  using (
    exists (
      select 1
      from public.mutual_matches m
      join public.identity_link i
        on i.pseudo_id in (m.pseudo_id_a, m.pseudo_id_b)
      where m.id = messages.match_id
      and i.clerk_user_id = auth.jwt() ->> 'sub'
    )
  );

create policy "match participants can create messages"
  on public.messages for insert
  with check (
    exists (
      select 1
      from public.mutual_matches m
      join public.identity_link i
        on i.pseudo_id in (m.pseudo_id_a, m.pseudo_id_b)
      where m.id = messages.match_id
      and messages.sender_pseudo_id = i.pseudo_id
      and i.clerk_user_id = auth.jwt() ->> 'sub'
    )
  );
