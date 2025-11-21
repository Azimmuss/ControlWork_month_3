CREATE_JOBS = """
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        job TEXT NOT NULL,
        completed INTEGER DEFAULT 0
    )
"""

INSERT_JOB = "INSERT INTO jobs (job) VALUES (?)"

SELECT_JOBS = "SELECT id, job, completed FROM jobs"

SELECT_JOBS_COMPLETED = "SELECT id, job, completed FROM jobs WHERE completed = 1"

SELECT_JOBS_UNCOMPLETED = "SELECT id, job, completed FROM jobs WHERE completed = 0"

DELETE_JOB = "DELETE FROM jobs WHERE id = ?"