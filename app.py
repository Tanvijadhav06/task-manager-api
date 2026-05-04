from flask import Flask, request, jsonify
from ai_utils import classify_priority, summarize_tasks

app = Flask(__name__)

tasks = []

#  GET ALL TASKS 
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

#  CREATE TASK 
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json

    title = data.get("title")
    description = data.get("description", "")

    # 🔥 AI priority detection
    priority = classify_priority(description)

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "priority": priority,
        "completed": False
    }

    tasks.append(task)
    return jsonify(task)

#  UPDATE TASK    
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    for task in tasks:
        if task["id"] == id:
            task["completed"] = True
            return jsonify(task)

    return jsonify({"error": "Task not found"}), 404

# DELETE TASK 
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    global tasks
    tasks = [task for task in tasks if task["id"] != id]
    return jsonify({"message": "Task deleted"})

@app.route('/tasks/summary', methods=['GET'])
def get_task_summary():
    summary = summarize_tasks(tasks)
    return jsonify({"summary": summary}) 

#  RUN 
if __name__ == '__main__':
    app.run(debug=True)