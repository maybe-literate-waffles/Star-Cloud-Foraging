import psycopg as psyg


def insert_location(cur, latitude, longitude):
    cur.execute(
        t"INSERT INTO location (latitude, longitude) VALUES ({latitude}, {longitude});"
    )


# def insert_weather(cur, latitude, longitude):
#     cur.execute(t"INSERT INTO weather_data () VALUES;")

# def insert_location(cur, latitude, longitude):
#     cur.execute(t"INSERT INTO location (latitude, longitude) VALUES ({latitude}, {longitude});")


with psyg.connect("dbname=testdb user=literate-waffle") as conn:
    with conn.cursor() as cur:
        cur.execute("""
                CREATE TABLE IF NOT EXISTS location(
                    l_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                    latitude REAL,
                    longitude REAL
                    );

                CREATE TABLE IF NOT EXISTS t_timezone(
                    tz_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                    timezone TEXT 
                    );

                CREATE TABLE IF NOT EXISTS weather_data(
                    w_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                    l_id BIGINT,
                    tz_id BIGINT,
                    temp REAL,
                    time TEXT,
                    unit TEXT,

                    CONSTRAINT fk_location
                        FOREIGN KEY (l_id)
                        REFERENCES location(l_id)
                        ON DELETE CASCADE,
                    
                    CONSTRAINT fk_timezone
                        FOREIGN KEY (tz_id)
                        REFERENCES t_timezone(tz_id)
                        ON DELETE CASCADE
                    );
        """)

        conn.commit()
