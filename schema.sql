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

CREATE TABLE IF NOT EXISTS public.pages
(
    is_section boolean NOT NULL DEFAULT false,
    url character varying(50) COLLATE pg_catalog."default" NOT NULL,
    title character varying(50) COLLATE pg_catalog."default" NOT NULL,
    content text COLLATE pg_catalog."default" NOT NULL,
    name character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT pages_pkey PRIMARY KEY (url)
);

ALTER TABLE IF EXISTS public.projects
    ADD COLUMN published date;

ALTER TABLE IF EXISTS public.projects
    ADD COLUMN image_alt_text character varying;


ALTER TABLE IF EXISTS public.sociallinks
    ADD COLUMN link_alt_text character varying;