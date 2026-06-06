create table if not exists public.identity_link (
  pseudo_id uuid primary key default gen_random_uuid(),
  clerk_user_id text not null unique,
  created_at timestamptz not null default now()
);

create table if not exists public.profiles (
  pseudo_id uuid primary key references public.identity_link(pseudo_id) on delete cascade,
  metro_region text not null,
  age_bucket text not null check (age_bucket in ('60_64', '65_69', '70_74', '75_79', '80_plus')),
  activity_features jsonb not null,
  bio text not null default '',
  interests text[] not null default '{}',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.match_invitations (
  id uuid primary key default gen_random_uuid(),
  sender_pseudo_id uuid not null references public.identity_link(pseudo_id) on delete cascade,
  recipient_pseudo_id uuid not null references public.identity_link(pseudo_id) on delete cascade,
  status text not null check (status in ('pending', 'accepted', 'declined', 'expired')),
  created_at timestamptz not null default now(),
  unique (sender_pseudo_id, recipient_pseudo_id)
);

create table if not exists public.mutual_matches (
  id uuid primary key default gen_random_uuid(),
  pseudo_id_a uuid not null references public.identity_link(pseudo_id) on delete cascade,
  pseudo_id_b uuid not null references public.identity_link(pseudo_id) on delete cascade,
  created_at timestamptz not null default now(),
  check (pseudo_id_a < pseudo_id_b),
  unique (pseudo_id_a, pseudo_id_b)
);

create table if not exists public.messages (
  id uuid primary key default gen_random_uuid(),
  match_id uuid not null references public.mutual_matches(id) on delete cascade,
  sender_pseudo_id uuid not null references public.identity_link(pseudo_id) on delete cascade,
  scrubbed_text text not null,
  removed jsonb not null default '[]'::jsonb,
  created_at timestamptz not null default now()
);
