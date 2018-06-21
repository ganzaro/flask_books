
# from django.db import models

# class Publisher(models.Model):
#     name = models.CharField(max_length=30)
#     address = models.CharField(max_length=50)
#     city = models.CharField(max_length=60)
#     state_province = models.CharField(max_length=30)
#     country = models.CharField(max_length=50)
#     website = models.URLField()

# class Author(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=40)
#     email = models.EmailField()

# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     authors = models.ManyToManyField(Author)
#     publisher = models.ForeignKey(Publisher)
#     publication_date = models.DateField()



# class Person(Base):
#     __tablename__ = 'people'
#     id = Column(Integer, primary_key=True)
#     mobile_phone = relationship("MobilePhone", uselist=False, back_populates="person")

# class MobilePhone(Base):
#     __tablename__ = 'mobile_phones'
#     id = Column(Integer, primary_key=True)
#     person_id = Column(Integer, ForeignKey('people.id'))
#     person = relationship("Person", back_populates="mobile_phone")



# # ------------------------------------
# students_classes_association = Table('students_classes', Base.metadata,
#     Column('student_id', Integer, ForeignKey('students.id')),
#     Column('class_id', Integer, ForeignKey('classes.id'))
# )

# class Student(Base):
#     __tablename__ = 'students'
#     id = Column(Integer, primary_key=True)
#     classes = relationship("Class", secondary=students_classes_association)

# class Class(Base):
#     __tablename__ = 'classes'
#     id = Column(Integer, primary_key=True)

