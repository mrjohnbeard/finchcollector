from django.db import models

# Create your models here.

class Finch: 
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

finches = [
  Finch('Andy', '01Breed', 'kinda red', 20),
  Finch('Bandy', '02Breed', 'kinda blue', 25),
  Finch('Candy', '03Breed', 'kinda orange', 30),
  Finch('Dandy', '04Breed', 'kinda green', 35)
]