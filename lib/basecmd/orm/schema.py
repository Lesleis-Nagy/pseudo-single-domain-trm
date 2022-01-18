#
# Project-putz schema.
#

from sqlalchemy import Column, Integer, Float, String, DateTime, Boolean, Numeric
from sqlalchemy import ForeignKey
from sqlalchemy import UniqueConstraint, Index
from sqlalchemy import event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import column_property
from sqlalchemy.orm import relationship

Base = declarative_base()


class Setting(Base):
    r"""
    Settings class.

    Attributes:
        name (string)   : the attribute name (primary key).
        value (string)  : the attribute value.
    """
    __tablename__ = "setting"
    name = Column(String, primary_key=True)
    value = Column(String)
