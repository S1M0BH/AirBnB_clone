#!/usr/bin/python3
"""It initializes package """



from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()