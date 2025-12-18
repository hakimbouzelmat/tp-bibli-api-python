from enum import Enum


class CategoryEnum(str, Enum):
    fiction = "Fiction"
    science = "Science"
    histoire = "Histoire"
    philosophie = "Philosophie"
    autre = "Autre"
