{
 "cells": [
  {
   "cell_type": "code",
   "execution_count":2,
   "id": "ab229c37-2871-4d3d-938d-f5cf1e92f659",
   "metadata": {},
   "outputs": [],
   "source": [
    "# db_setup.py\n",
    "from sqlalchemy import create_engine, Column, Integer, String, Text\n",
    "from sqlalchemy.ext.declarative import declarative_base\n",
    "from sqlalchemy.orm import sessionmaker\n",
    "\n",
    "DATABASE_URL = \"postgresql://postgres:postgres@localhost:5432/redactdb\"\n",
    "\n",
    "engine = create_engine(DATABASE_URL)\n",
    "SessionLocal = sessionmaker(bind=engine)\n",
    "Base = declarative_base()\n",
    "\n",
    "class Document(Base):\n",
    "    __tablename__ = \"documents\"\n",
    "    id = Column(Integer, primary_key=True, index=True)\n",
    "    original_text = Column(Text)\n",
    "    redacted_text = Column(Text)\n",
    "\n",
    "Base.metadata.create_all(bind=engine)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
