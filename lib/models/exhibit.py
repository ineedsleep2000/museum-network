from models.__init__ import CONN, CURSOR

class Exhibit:

################################################################
# Classmethod to create table in db
################################################################
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

################################################################
# Classmethod to drop/ delete table from db
################################################################  
    @classmethod
    def drop_table(cls):
        sql="""
            DROP TABLE IF EXISTS exhibit;
        """
        CURSOR.execute(sql)

################################################################
# Classmethod to create instances
################################################################
    @classmethod
    def create(cls, name, status, museum_id):
        exhibit= cls(name, status, museum_id)
        exhibit.save()
        return exhibit

################################################################
# Classmethod to get one instance
################################################################ 
    @classmethod
    def instance_from_db(cls, row):
        exhibit = cls(
            id=row[0],
            name=row[1], 
            status=row[2],
            museum_id=row[3],
        )
        return exhibit

################################################################
# Classmethod to get all instances
################################################################
    @classmethod
    def get_all(cls):
        sql="SELECT * FROM exhibit;"
        return [cls.instance_from_db(row) for row in CURSOR.execute(sql).fetchall()]

################################################################
# Classmethod to get an instance by name
################################################################   
    # @classmethod
    # def find_by_name(cls, name):
    #     sql = """
    #         SELECT * FROM exhibit
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

################################################################
# __init__ function
################################################################
    def __init__(self, name, status, museum_id, id= None):
        self.id= id
        self.name = name 
        self.status= status
        self.museum_id= museum_id #foreign key

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

################################################################
# Update instance method
################################################################   
    def update(self):
        sql = """
            UPDATE exhibit
            SET name = ?, status = ?, museum_id = ?
            WHERE id = ?;
        """
        CURSOR.execute(sql, (self.name, self.status, self.museum_id, self.id))
        CONN.commit()

################################################################
# Delete instance method
################################################################
    def delete(self):
        sql = """
            DELETE FROM exhibit WHERE id = ?;
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

################################################################
# __repr__
################################################################
    def __repr__(self):
        return f"<Exhibit {self.id}: {self.name} | {self.museum_id}>"
    pass