# 🎓 Smart Campus Assistant System - Project Report

## 1. Abstract
The **Smart Campus Assistant System** is a python-based application designed to help students manage their academic activities efficiently. It integrates task management, attendance tracking, grade calculation, and a smart reminder system into a single user-friendly web interface built with Streamlit.

## 2. System Architecture (Flowchart)

```mermaid
graph TD
    A[Start] --> B[Login/Register]
    B --> |Success| C[Dashboard]
    B --> |Failure| B
    
    C --> D{Features}
    D --> E[Task Manager]
    D --> F[Attendance Tracker]
    D --> G[Grade Calculator]
    D --> H[AI Assistant]
    
    E --> |Add/View Tasks| DB[(SQLite Database)]
    F --> |Mark/View Attendance| DB
    G --> |Add/View Grades| DB
    H --> |Query| I[Rule-Based Logic]
    
    C --> J[Notifications (Reminders)]
    J --> |Check Deadlines| DB
```

## 3. Features Implemented
1.  **User Authentication**: Secure Login and Registration system using hashed passwords.
2.  **Task Manager**: Add, edit, delete, and view academic assignments with deadlines.
3.  **Attendance Tracker**: Mark attendance (Present/Absent) and view percentage calculation with graphical charts.
4.  **Grade Calculator**: Input subject marks and calculate the Estimated GPA based on performance.
5.  **Smart Reminders**: Automatic notifications on the dashboard for tasks due within 3 days.
6.  **AI Assistant**: A chatbot interface to answer common student queries.

## 4. Technology Stack
-   **Language**: Python 3.x
-   **Frontend**: Streamlit (Web Framework)
-   **Database**: SQLite
-   **Data Analysis**: Pandas
-   **Visualization**: Plotly

## 5. Sample Test Cases

| Test Case ID | Feature | Input Data | Expected Output | Status |
| :--- | :--- | :--- | :--- | :--- |
| TC01 | Registration | User: `student1`, Pwd: `123` | "Registration successful" | ✅ Pass |
| TC02 | Login | User: `student1`, Pwd: `123` | Redirect to Dashboard | ✅ Pass |
| TC03 | Add Task | Title: `Math HW`, Date: `Tomorrow` | Task added to list | ✅ Pass |
| TC04 | Mark Attendance | Subject: `Physics`, Status: `Present` | Record saved, % updates | ✅ Pass |
| TC05 | Calculate GPA | Math: 90, Physics: 85 | GPA: ~3.75 | ✅ Pass |
| TC06 | Reminders | Task due in 2 days | "⚠️ Math HW is due..." | ✅ Pass |

## 6. Conclusion
The system successfully meets all the objectives set out in the requirements. It demonstrates the use of core programming concepts, data structures, database handling, and GUI development, providing a practical solution for students.
