from models.__init__ import CONN, CURSOR


class Exhibit:

    @classmethod
    def create_table(cls):
        sql="""
            CREATE TABLE IF NOT EXISTS exhibit
                (id INTEGER PRIMARY KEY,
                name TEXT,
                status BOOL,
                museum_id INTEGER);
        """
        CURSOR.execute(sql)
    
    @classmethod
    def drop_table(cls):
        sql="""
            DROP TABLE IF EXISTS exhibit;
        """
        CURSOR.execute(sql)

    @classmethod
    def create(cls, name, status, museum_id):
        exhibit= cls(name, status, museum_id)
        exhibit.save()
        return exhibit

    ########### get 1 thing from db  
    @classmethod
    def instance_from_db(cls, row):
        exhibit = cls(
            id=row[0],
            name=row[1], 
            status=row[2],
            museum_id=row[3],
        )
        return exhibit

############## get everything from db
    @classmethod
    def get_all(cls):
        sql="SELECT * FROM exhibit;"
        return [cls.instance_from_db(row) for row in CURSOR.execute(sql).fetchall()]

    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM exhibit
            WHERE name = ? 
            LIMIT 1;
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        if not row:
            return None
        return cls.instance_from_db(row)
    
    @classmethod
    def find_exhibit_by_id(cls, id):
        sql = """
            SELECT * FROM exhibit
            WHERE id = ? 
            LIMIT 1;
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        if not row:
            return None
        return cls.instance_from_db(row)

    def __init__(self, name, status, museum_id, id= None):
        self.id= id
        self.name = name 
        self.status= status
        self.museum_id= museum_id #foreign key

    def save(self):
        sql= """
            INSERT INTO exhibit(name, status, museum_id)
            VALUES(?,?,?)
        """
        CURSOR.execute(
            sql, (self.name, self.status, self.museum_id)
        )
        CONN.commit()
        self.id= (
            CURSOR.lastrowid
        )
    
    def update(self):
        sql = """
            UPDATE exhibit
            SET name = ?, status = ?, museum_id = ?
            WHERE id = ?;
        """
        CURSOR.execute(sql, (self.name, self.status, self.museum_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM exhibit WHERE id = ?;
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    def __repr__(self):
        return f"<Exhibit {self.id}: {self.name} | {self.museum_id}>"
    pass