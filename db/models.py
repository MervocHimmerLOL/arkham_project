from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, String

class Base(DeclarativeBase):
    pass

class Location(Base):
    __tablename__ = "Location"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    next_id: Mapped[int | None] = mapped_column(ForeignKey("Location.id"))
    next: Mapped["Location | None"] = relationship(remote_side="Location.id")

class Detective(Base):
    __tablename__ = "Detective"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    clues_count: Mapped[int] = mapped_column(Integer, default=0)

    current_location_id: Mapped[int] = mapped_column(ForeignKey("Location.id"))
    current_location: Mapped[Location] = relationship()