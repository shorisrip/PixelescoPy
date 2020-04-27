import models

models.db.connect()
models.db.create_tables([models.Image])
