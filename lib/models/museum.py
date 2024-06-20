from models.__init__ import CONN, CURSOR

class Museum:

################################################################
# Classmethod to create table in db
################################################################
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

################################################################
# Classmethod to drop/ delete table from db
################################################################  
    @classmethod
    def drop_table(cls):
        sql="""
            DROP TABLE IF EXISTS museum;
        """
        CURSOR.execute(sql)

################################################################
# Classmethod to create instances
################################################################
    @classmethod
    def create(cls, name, address, status, open_hours):
        museum= cls(name, address, status, open_hours)
        museum.save()
        return museum

################################################################
# Classmethod to get one instance
################################################################
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

################################################################
# Classmethod to get all instances
################################################################

    @classmethod
    def get_all(cls):
        sql="SELECT * FROM museum;"
        return [cls.instance_from_db(row) for row in CURSOR.execute(sql).fetchall()]

################################################################
# Classmethod to get an instance by name
################################################################
    # @classmethod
    # def find_by_name(cls, name):
    #     sql = """
    #         SELECT * FROM museum
    #         WHERE name = ? 
    #         LIMIT 1;
    #     """
    #     row = CURSOR.execute(sql, (name,)).fetchone()
    #     if not row:
    #         return None
    #     return cls.instance_from_db(row)

################################################################
# Classmethod to get an instance by ID
################################################################
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

################################################################
# __init__ function
################################################################
    def __init__(self, name, address, status, open_hours, id= None):
        self.id= id
        self.name = name
        self.address= address
        self.status= status
        self.open_hours= open_hours

################################################################
# Property setter
################################################################
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 3 <= len(name):
            self._name = name
        else:
            return Exception("Must be a string")   
################################################################
# Save instance method
################################################################
    def save(self):
        sql= """
            INSERT INTO museum(name, address, status, open_hours)
            VALUES(?,?,?,?)
        """
        CURSOR.execute(
            sql, (self.name, self.address, self.status, self.open_hours)
        )
        self.id= (
            CURSOR.lastrowid
        )
        CONN.commit()

################################################################
# Update instance method
################################################################
    def update(self):
        sql = """
            UPDATE museum
            SET name = ?, address = ?, status = ?, open_hours = ?
            WHERE id = ?;
        """
        CURSOR.execute(sql, (self.name, self.address, self.status, self.open_hours, self.id))
        CONN.commit()

################################################################
# Delete instance method
################################################################
    def delete(self):
        sql = """
            DELETE FROM museum WHERE id = ?;
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

################################################################
# join instance method
################################################################
    def join(self):
        sql = """
            SELECT exhibit.name
            FROM exhibit
            INNER JOIN museum ON exhibit.museum_id = museum.id
            WHERE exhibit.museum_id = ?;
        """
        
        return [{"exhibit_name": row[0]} for row in CURSOR.execute(sql,(self.id,)).fetchall()]

################################################################
# __repr__
################################################################
    def __repr__(self):
        return f"<Museum {self.id}: {self.name} | {self.address} | {self.status} | {self.open_hours}>"
    pass
