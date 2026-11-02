class Student:
    def __init__(self, name, group): #Кожен виклик __init__ створює НОВИЙ порожній список для конкретного студента
        self.name = name
        self.group = group
        self.scores = []
    def add_score(self, score):
        if not 0 <= score <= 100:
            raise ValueError("score має бути від 0 до 100")
        self.scores.append(score)
    def average(self):
        if not self.scores:
            return None
        return sum(self.scores) / len(self.scores)
olena = Student("Олена", "КН-11")
olena.add_score(84)

"""self — посилання на поточний об’єкт. 
self.name належить екземпляру; 
локальне name існує лише під час __init__. 
"""

def __repr__(self):
    return f"Student(name={self.name!r}, group={self.group!r})"
"""__repr__допомагає діагностиці.Не повертайте з нього пароль або інші чутливі дані."""