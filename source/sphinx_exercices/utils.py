class ExerciceNumbering:
    def __init__(self):
        self.current_exercice_number = 0

    def get_next_exercice_number(self):
        self.current_exercice_number += 1
        return self.current_exercice_number
