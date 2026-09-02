# To-Do Task Management Module for Odoo 18

A feature-rich Odoo 18 module designed to streamline task management, track working hours via timesheets, automate deadline monitoring, and generate printable PDF task reports.

---

## 🌟 Key Features

* **Task Workflow & Lifecycle:**
  * Track task states across multiple stages (`New`, `In Progress`, `Completed`, `Closed`).
  * Dynamic button visibility based on task progression.
  * Reset task status options.

* **Timesheet Tracking & Calculations:**
  * `One2many` relation linking multiple timesheet log lines to each task.
  * Automated calculation of total logged hours using `@api.depends`.
  * Real-time computed fields for tracking work duration.

* **Business Constraints & Data Integrity:**
  * `@api.constrains` validation preventing logged timesheet hours from exceeding the estimated task time.

* **Scheduled Automation (Cron Jobs):**
  * Automated Scheduled Action (`ir.cron`) running daily to detect overdue tasks.
  * Automatic state tracking with boolean flag `is_late` for non-completed overdue tasks.

* **Dynamic UI Customizations:**
  * Conditional row highlighting (`decoration-danger`) in List Views for overdue tasks.
  * Search view enhancements including custom filters (by status) and group-by options (assigned user, stage).
  * Server Action to perform batch closure on multiple tasks directly from the list view.

* **QWeb PDF Reports:**
  * Printable professional task documentation using QWeb reporting engine.
  * Dynamic rendering of task metadata, assigned users, due dates, descriptions, and detailed timesheet breakdowns.
  * Integrated company branding (logo, company details, header/footer layout).

---

## 🛠️ Technical Stack

* **ERP Platform:** Odoo 18 (Community / Enterprise)
* **Backend:** Python 3.12, Odoo ORM
* **Frontend / Views:** XML, QWeb Templates, XPath
* **Database:** PostgreSQL
* **Engine:** Wkhtmltopdf for PDF rendering

---

## 📂 Module Structure

```text
todo_management/
├── __init__.py
├── __manifest__.py
├── .gitignore
├── models/
│   ├── __init__.py
│   └── todo_task.py
├── reports/
│   └── todo_task_report_action.xml
├── security/
│   └── ir.model.access.csv
├── static/
│   ├── description/
│   └── src/
└── views/
    ├── base_menu.xml
    └── todo_task_view.xml

👨‍💻 Author
Developed by Nabil Atef