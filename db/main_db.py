import sqlite3
from db import queries
from config import path_db


def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.CREATE_JOBS)
    print('База данных подключена!')
    conn.commit()
    conn.close()


def add_job(job):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.INSERT_JOB, (job,))
    conn.commit()
    job_id = cursor.lastrowid
    conn.close()
    return job_id


def get_jobs(filter_type):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()

    if filter_type == 'completed':
        cursor.execute(queries.SELECT_JOBS_COMPLETED)
    elif filter_type == 'uncompleted':
        cursor.execute(queries.SELECT_JOBS_UNCOMPLETED)
    else:
        cursor.execute(queries.SELECT_JOBS)

    jobs = cursor.fetchall()
    conn.close()
    return jobs


def update_job(job_id, completed=None):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()

    if completed is not None:
        cursor.execute(
            "UPDATE jobs SET completed = ? WHERE id = ?",
            (completed, job_id)
        )

    conn.commit()
    conn.close()


def delete_job(job_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.DELETE_JOBS, (job_id,))
    conn.commit()
    conn.close()