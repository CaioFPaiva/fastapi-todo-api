from sqlalchemy.orm import Session
from . import models, schemas

def create_task(db: Session, task_in: schemas.TaskCreate) -> models.Task:
    task = models.Task(title=task_in.title, description=task_in.description, done=task_in.done)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_task(db: Session, task_id: int) -> models.Task | None:
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def list_tasks(db: Session, skip: int = 0, limit: int = 100) -> list[models.Task]:
    return db.query(models.Task).offset(skip).limit(limit).all()

def update_task(db: Session, task: models.Task, updates: schemas.TaskUpdate) -> models.Task:
    data = updates.model_dump(exclude_unset=True)
    for k, v in data.items():
        setattr(task, k, v)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task: models.Task) -> None:
    db.delete(task)
    db.commit()
