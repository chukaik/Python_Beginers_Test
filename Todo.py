import psycopg2

# Function to connect to PostgreSQL
def connect_db():
    return psycopg2.connect(
        dbname="todolist_db",
        user="postgres",
        password="123456",
        host="localhost",
        port="5432"
    )

# Function to add tasks
def add_task(title, description):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (title, description) VALUES (%s, %s)", (title, description))
    conn.commit()
    cur.close()
    conn.close()
    print("Task added successfully!")

# Function to View tasks
def view_tasks():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()
    cur.close()
    conn.close()
    
    for task in tasks:
        print(f"{task[0]} - {task[1]} ({task[3]})")

# Function to update task status
def update_task(task_id, status):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET status = %s WHERE id = %s", (status, task_id))
    conn.commit()
    cur.close()
    conn.close()
    print("Task updated successfully!")

# Function to delete a task
def delete_task(task_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    conn.commit()
    cur.close()
    conn.close()
    print("Task deleted successfully!")

# Function to Create CLI Menu
def main():
    while True:
        print("\n📌 To-Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task Status")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            title = input("Task title: ")
            description = input("Task description: ")
            add_task(title, description)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_id = input("Enter Task ID: ")
            status = input("Enter new status (pending/done): ")
            update_task(task_id, status)
        elif choice == "4":
            task_id = input("Enter Task ID: ")
            delete_task(task_id)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
