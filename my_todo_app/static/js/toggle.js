document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll(".toggle-task").forEach(checkbox => {
        checkbox.addEventListener("change", function() {
            let taskId = this.dataset.id;
            let isChecked = this.checked;

            fetch(`/toggle/${taskId}/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": "{{ csrf_token }}",
                    "Content-Type": "application/json"
                }
            })
            .then(response => response.json())
            .then(data => {
                let taskTitle = document.getElementById(`task-title-${taskId}`);
                if (taskTitle) {
                    taskTitle.style.textDecoration = data.completed ? "line-through" : "none";
                }
            })
            .catch(error => console.error("Помилка:", error));
        });
    });
});