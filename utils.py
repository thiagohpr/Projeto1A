from database import Database,Note


def extract_route(request):
    lista=request.split()
    return lista[1][1:]


def read_file(path):
    strings=['txt,html,css,js']
    file=""
    partes=path.parts
    tipo=partes[-1]
    
    if tipo in strings:
        with open (path,'r') as f:
            file=f.read()
            
    else:
        with open (path,'rb') as f:
            file=f.read()

    return file



def load_data():
    # path="data/{}".format(notes)
    # with open (path,'r') as f:
    #     file=f.read()

    # notas=json.loads(file)
    # return notas
    db=Database('banco')
    notes = db.get_all()
    return notes

def load_template(arquivo):
    path="templates/{}".format(arquivo)
    with open (path,'r') as f:
        string=f.read()
    return string

def adiciona_note(title,detail):
    db=Database('banco')
    db.add(Note(title=title, content=detail))

