--
-- PostgreSQL database dump
--

-- Dumped from database version 14.8 (Ubuntu 14.8-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.8 (Ubuntu 14.8-0ubuntu0.22.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: song; Type: TABLE; Schema: public; Owner: wsdpl
--

CREATE TABLE public.song (
    song_id character varying NOT NULL,
    title character varying NOT NULL,
    artist character varying NOT NULL,
    album character varying NOT NULL,
    release_date date NOT NULL,
    duration character varying NOT NULL,
    image character varying NOT NULL
);


ALTER TABLE public.song OWNER TO wsdpl;


--
-- Name: user; Type: TABLE; Schema: public; Owner: wsdpl
--

CREATE TABLE public."user" (
    user_id integer NOT NULL,
    username character varying(20) NOT NULL,
    email character varying NOT NULL,
    password character varying NOT NULL,
    created_at timestamp without time zone NOT NULL
);


ALTER TABLE public."user" OWNER TO wsdpl;


--
-- PostgreSQL database dump complete
--

