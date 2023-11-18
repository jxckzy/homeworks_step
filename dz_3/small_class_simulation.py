class Job:
    def __init__(self, title, salary):
        self.title = title
        self.salary = salary


class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def get_job_description(self):
        if self.job:
            return f"{self.name} is a {self.job.title} earning {self.job.salary} per month."
        else:
            return f"{self.name} currently doesn't have a job."

    def change_job(self, new_job):
        self.job = new_job
        return f"{self.name} has a new job as a {self.job.title}."


job1 = Job("Software Developer", 5000)
job2 = Job("Data Scientist", 6000)

person1 = Person("Masha", job1)
person2 = Person("Ivan", job2)

print(person1.get_job_description())
print(person2.get_job_description())

new_job = Job("Product Manager", 7000)
print(person1.change_job(new_job))
print(person1.get_job_description())
