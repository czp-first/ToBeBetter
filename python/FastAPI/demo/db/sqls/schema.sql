create sequence person_id_seq;

create table person(
    id bigint not null default nextval('person_id_seq') primary key,
    created_at timestamp with time zone default now(),
    updated_at timestamp with time zone default now(),
    name character varying(64) not null,
    age int not null
);

alter sequence person_id_seq owned by person.id;
