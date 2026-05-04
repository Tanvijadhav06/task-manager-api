from transformers import pipeline

# Add summarizer model
summarizer = pipeline("summarization")

def summarize_tasks(task_list):
    if not task_list:
        return "No tasks available."

    text = " ".join([task["description"] for task in task_list if task.get("description")])

    if not text:
        return "No descriptions to summarize."

    summary = summarizer(text, max_length=50, min_length=10, do_sample=False)

    return summary[0]["summary_text"]