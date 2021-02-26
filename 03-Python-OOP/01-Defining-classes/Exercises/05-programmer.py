class Programmer:
    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = skills

    def is_known(self, language):
        return language == self.language

    def has_skills(self, skills_needed):
        return self.skills >= skills_needed

    def watch_course(self, course_name, language, skills_earned):
        if not self.is_known(language):
            return f"{self.name} does not know {language}"
        self.skills += skills_earned
        return f"{self.name} watched {course_name}"

    def change_language(self, new_language, skills_needed):
        if not self.has_skills(skills_needed):
            needed_skills = skills_needed - self.skills
            return f"{self.name} needs {needed_skills} more skills"
        if self.is_known(new_language):
            return f"{self.name} already knows {self.language}"
        previous_language = self.language
        self.language = new_language
        return f"{self.name} switched from " \
               f"{previous_language} to {new_language}"


programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
