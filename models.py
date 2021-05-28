from tortoise import fields, models


class Files(models.Model):
    id = fields.IntField(pk=True)
    file = fields.CharField(max_length=255, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
    
    def __str__(self):
        return self.file
