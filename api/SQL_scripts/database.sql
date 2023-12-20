CREATE DATABASE myDacia WITH OWNER = postgres;

GRANT ALL PRIVILEGES ON DATABASE myDacia TO postgres;

CREATE TABLE mobile_user (
    login_id varchar PRIMARY KEY,
    password varchar NOT NULL,
    account_id varchar NOT NULL,
    vin varchar NOT NULL
);

-- logs_actions(action,created_at,success,login_id,informations)
CREATE TABLE logs_actions (
    id serial PRIMARY KEY,
    action varchar NOT NULL,
    created_at timestamp NOT NULL,
    success boolean NOT NULL,
    login_id varchar NOT NULL,
    informations varchar NOT NULL
);
