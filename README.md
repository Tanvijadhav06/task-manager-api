# Task Manager API 

A REST API built using Flask to manage tasks, enhanced with AI-based features for smarter task handling.

 Features

- Add new tasks
- View all tasks
- Update task status
- Delete tasks
- AI-based task priority detection (High / Medium / Low)
- AI-generated summary of all tasks

Tech Stack

- Python
- Flask
- Hugging Face Transformers (NLP)
- REST API

API Endpoints

- `GET /tasks` → Get all tasks  
- `POST /tasks` → Create a new task (with AI priority detection)  
- `PUT /tasks/<id>` → Update task status  
- `DELETE /tasks/<id>` → Delete a task  
- `GET /tasks/summary` → Get AI-generated summary of tasks  

# Example Request (POST /tasks)

```json
{
  "title": "Fix bug",
  "description": "Fix critical payment issue urgently"
}
Example Response
{
  "id": 1,
  "title": "Fix bug",
  "description": "Fix critical payment issue urgently",
  "priority": "HIGH",
  "completed": false
}

Overview

This project demonstrates how AI (Natural Language Processing) can be integrated into backend systems to automate task prioritization and generate insights from task data.

Author

Tanvi Jadhav
