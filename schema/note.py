## this function is used to convert mongo db type object into python dictionary
def noteEntity(item)->dict:
    return {
        "_id":str(item["_id"]),
        "author":item["author"],
        "text":item["text"],
        

    }
def notesEntity(items)->list:
    return [noteEntity(item) for item in items]