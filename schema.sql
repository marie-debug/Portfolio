-- Table: public.sociallinks

-- DROP TABLE IF EXISTS public.sociallinks;

CREATE TABLE IF NOT EXISTS public.sociallinks
(
    icon character varying(36) COLLATE pg_catalog."default" NOT NULL,
    type character varying(36) COLLATE pg_catalog."default" NOT NULL,
    url  text COLLATE pg_catalog."default"                  NOT NULL,
    id   SERIAL,
    CONSTRAINT sociallinks_pkey PRIMARY KEY (id)
);

