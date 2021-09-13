import sqlite3

class Database:
    def __init__(self, name):
        self.conn = sqlite3.connect("{}.db".format(name))
        self.conn.execute("CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title STRING, content STRING NOT NULL)")
    def add (self,note):
        values='"{}","{}"'.format(note.title,note.content)
        self.conn.execute("INSERT INTO note (title,content) VALUES ({});".format(values))
        self.conn.commit()
    def get_all (self):
        lista=[]
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        for linha in cursor:
            lista.append(Note(id=linha[0],title=linha[1], content=linha[2]))
        return lista
    def update (self,entry):
        self.conn.execute("UPDATE note SET title = '{}', content = '{}' WHERE id = {}".format(entry.title,entry.content,entry.id))
        self.conn.commit()
    def delete (self,note_id):
        self.conn.execute("DELETE FROM note WHERE id = {}".format(note_id))
        self.conn.commit()
        
class Note:
    def __init__(self, id=None, title=None, content=''):
        self.id = id
        self.title = title
        self.content = content