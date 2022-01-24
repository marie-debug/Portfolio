CREATE TABLE IF NOT EXISTS public.sociallinks
(
    icon character varying(36) COLLATE pg_catalog."default" NOT NULL,
    type character varying(36) COLLATE pg_catalog."default" NOT NULL,
    url  text COLLATE pg_catalog."default"                  NOT NULL,
    id   SERIAL,
    CONSTRAINT sociallinks_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.projects
(
    image       text COLLATE pg_catalog."default" NOT NULL,
    thumbnail   text COLLATE pg_catalog."default" NOT NULL,
    name        text COLLATE pg_catalog."default" NOT NULL,
    summary     text COLLATE pg_catalog."default" NOT NULL,
    id          text COLLATE pg_catalog."default" NOT NULL,
    description text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT projects_pkey PRIMARY KEY (id)
);