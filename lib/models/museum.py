from models.__init__ import CONN, CURSOR

class Museum:

    @classmethod
    def create_table(cls):
        sql="""
            CREATE TABLE IF NOT EXISTS museum
                (id INTEGER PRIMARY KEY,
                name TEXT,
                address TEXT,
                status BOOL,
                open_hours TEXT);
        """
        CURSOR.execute(sql)
    
    @classmethod
    def drop_table(cls):
        sql="""
            DROP TABLE IF EXISTS museum;
        """
        CURSOR.execute(sql)

    @classmethod
    def create(cls, name, address, status, open_hours):
        museum= cls(name, address, status, open_hours)
        museum.save()
        return museum
    
############ get 1 thing from db  
    @classmethod
    def instance_from_db(cls, row):
        museum = cls(
            id=row[0],
            name=row[1], 
            address=row[2],
            status=row[3],
            open_hours=row[4],
        )
        return museum

############## get everything from db
    @classmethod
    def get_all(cls):
        sql="SELECT * FROM museum;"
        return [cls.instance_from_db(row) for row in CURSOR.execute(sql).fetchall()]
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM museum
            WHERE name = ? 
            LIMIT 1;
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        if not row:
            return None
        return cls.instance_from_db(row)
    
    @classmethod
    def find_museum_by_id(cls, id):
        sql = """
            SELECT * FROM museum
            WHERE id = ? 
            LIMIT 1;
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        if not row:
            return None
        return cls.instance_from_db(row)

    def __init__(self, name, address, status, open_hours, id= None):
        self.id= id
        self.name = name
        self.address= address
        self.status= status
        self.open_hours= open_hours

    def save(self):
        sql= """
            INSERT INTO museum(name, address, status, open_hours)
            VALUES(?,?,?,?)
        """
        CURSOR.execute(
            sql, (self.name, self.address, self.status, self.open_hours)
        )
        CONN.commit()
        self.id= (
            CURSOR.lastrowid
        )

    def update(self):
        sql = """
            UPDATE museum
            SET name = ?, address = ?, status = ?, open_hours = ?
            WHERE id = ?;
        """
        CURSOR.execute(sql, (self.name, self.address, self.status, self.open_hours, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM museum WHERE id = ?;
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()


    def __repr__(self):
        return f"<Museum {self.id}: {self.name} | {self.address} | {self.status} | {self.open_hours}>"
    pass