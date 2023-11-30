import psycopg2

postgres_db = psycopg2.connect(database="postgres",
                               host="localhost",
                               user="postgres",
                               password="pass123",
                               port="5432")