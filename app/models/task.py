from sqlalchemy.orm import Mapped, mapped_column
from ..db import db
from datetime import datetime

#from sqlalchemy import DateTime
from typing import Optional


class Task(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
    completed_at: Mapped[Optional[datetime]]

    #completed_at: Mapped[Optional[datetime]] = mapped_column(default=None)