# CAPSTONE PROJECT : STUDENT GRADES DATA

# Python CRUD Application for Student Score Management
A comprehensive Python application for managing student grade records using Create, Read, Update, and Delete (CRUD) operations in a simple CLI (Command Line Interface) environment.
_____________________________________________________________________________________________________________________________________________________________
# Business Understanding
This project is designed for the education domain, specifically to assist in managing student academic performance. Monitoring and maintaining student scores plays a vital role in evaluating learning outcomes, identifying at-risk students, and supporting academic decision-making.

# Benefits
•	Improved data accuracy and consistency in student score tracking.
•	Streamlined manual record-keeping for educators.
•	Enhanced visibility for performance analysis.
•	Easier classification of pass/fail students.
•	Enables fast report generation and ranking.

# Target Users
This application is designed for:
•	Teachers and academic coordinators managing student performance.
•	Tutoring centers needing a lightweight, offline solution.
•	Bootcamp instructors who need to manage module-level exam scores efficiently.

# Features :
**Create:**
- Add new student entries with:
  Student ID (NIS)
  Full name
  Exam scores (Modul 1, 2, and 3)
  Validate numeric input and prevent duplicates.

**Read :**
- Search students by name or NIS.
- Filter:
  Only passed students (average ≥ 80).
  Only failed students.
- View:
  Sorted lists by name or average score.
  Highest-ranking students based on average.

**Update :**
- Edit student records by searching using NIS.
- Modify scores and auto-update averages and pass/fail status.

**Delete :**
- Remove student records by NIS.
- Confirmation required before deletion.

**Security (Basic) :**
- Simple CLI confirmation and validation before critical changes.

**Reporting :**
- Show number of passed, failed, and total students.
- Display students with the highest average score.

________________________________________

**Installation**
- Prerequisites
-	Python 3.6 or higher
-	No external packages required

python main.py
No database or file storage is required in this version. All data is stored in memory.
________________________________________
**Data Model (List-Based)**
The project uses parallel lists to store student data:
- nis = []            # Student ID (string/integer)
- nama_siswa = []     # Full Name (string)
- nilai_modul1 = []   # Exam Score Module 1 (int)
- nilai_modul2 = []   # Exam Score Module 2 (int)
- nilai_modul3 = []   # Exam Score Module 3 (int)
- avg_nilai = []      # Average Score (float)
- keterangan = []     # Status: 'Lulus' or 'Tidak Lulus' (string)
________________________________________
**Usage Example**
- Create: Input NIS, name, and 3 exam scores.
- Read: Display all data or filtered views.
- Update: Change score of a specific student using NIS.
- Delete: Remove student using NIS.
________________________________________
**Contributing**

Contributions are welcome!
- Open an issue for bugs or improvements
- Submit a pull request
- Or email: siskatho17@gmail.com
