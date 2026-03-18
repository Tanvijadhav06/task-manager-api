from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route ('/tasks', methods = ['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods = ['POST'])
def ad_task():
    data = request.json
    task = {
        "id": len(tasks) + 1,
        "title":data.get("title"),
        "completed": False
    }
    tasks.append(task)
    return jsonify(task)

@app.route('/tasks/<int:id>', methods = ['PUT'])
def update_task(id):
    for task in tasks:
        if task["id"] == id:
            task["completed"] = True
            return jsonify(task)
    return jsonify({"error":"Task not found"}), 404

@app.route('/tasks/<int:id>', methods = ['DELETE'])
def delete_task(id):
    global tasks
    tasks = [task for task in tasks if task["id"] != id]
    return jsonify({"message": "Task deleted"})

if __name__ == '__main__':
    app.run(debug=True)


