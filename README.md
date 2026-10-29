# 🎓 Student Registration App Using Python

## 📌 Project Overview

The **Student Registration App** is a Python desktop application developed using CustomTkinter. It provides a simple graphical interface where users can enter student details, including name, email, and phone number, and register their information.

The application stores registration details in a text file named `users.txt` and displays the saved records in the application window.

It also includes a course selection dropdown where users can choose from available courses.

## ✨ Features

- 📝 **Student Registration:** Enter student name, email, and phone number.
- 📧 **Email Input:** Collect student email addresses.
- 📱 **Phone Number Input:** Store student phone numbers.
- 📚 **Course Selection:** Choose a course from a dropdown menu.
- 💾 **File Storage:** Save registration details in `users.txt`.
- 📋 **Display Registered Students:** Load and display saved records.
- 🖥️ **Graphical User Interface:** Built using CustomTkinter.
- 🖼️ **Background Image:** Uses a custom image to improve the interface.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| CustomTkinter | Creates the graphical user interface |
| Pillow (PIL) | Loads and displays the background image |
| File Handling | Stores and reads student records |
| Text Files | Saves registration details in `users.txt` |

## 📋 Requirements

- Python installed on your computer.
- Visual Studio Code or another Python editor.
- The required Python libraries.
- The image file `student app.png`.

## ⚙️ Installation

### Step 1: Install the required libraries

Open the VS Code terminal and run:

```bash
py -3.12 -m pip install customtkinter pillow
```

### Step 2: Create the project files

Create a folder named `StudentRegistrationApp` and add the following files:

```text
StudentRegistrationApp/
│
├── StudentRegistrationApp.py
├── student app.png
├── users.txt
└── README.md
```

The `users.txt` file can be created automatically by Python when the registration code opens it in append mode, provided the file-opening code is corrected.

Keep `student app.png` in the appropriate working directory so the application can load the image.

### Step 3: Run the application

Open the terminal in your project folder and execute:

```bash
py -3.12 StudentRegistrationApp.py
```

The Student Registration App window should open.

## 🚀 How to Use

1. Run the application.
2. Enter the student's name.
3. Enter the student's email address.
4. Enter the student's phone number.
5. Select a course from the dropdown menu.
6. Click the **Register** button.
7. The registration details are intended to be saved in `users.txt`.
8. Previously saved student records are intended to appear in the application window.

## 📚 Available Courses

The application provides the following course options:

- Python
- Java
- Data Science
- Web Development

## 💾 Data Storage

Student information is intended to be stored in a text file named `users.txt`.

Each record is designed to contain the student's name, email, and phone number, separated by commas.

Example:

```text
Rahul,rahul@example.com,9876543210
Priya,priya@example.com,9123456780
```

These are sample records for demonstration purposes only.

## 🔍 How It Works

1. CustomTkinter creates the registration window and input fields.
2. Pillow loads the background image.
3. The user enters registration details.
4. The registration function reads the values from the input fields.
5. Python file handling saves the data in `users.txt`.
6. The status label displays a registration message.
7. The `LoadData()` function reads the saved records and displays them in the window.

## ⚠️ Important Notes

The current code needs a few corrections before all features will work as intended:

- The file-opening mode `"+r"` is not valid for the intended read-and-append operations. Use `"r"` for reading and `"a+"` for appending and reading.
- The string formatting in `LoadData()` contains quotation and formatting errors.
- Use `"\t"` for tab spacing and `"\n"` for a new line.
- The selected course is not currently included in the saved registration record.
- Each call to `LoadData()` creates additional labels, so previously displayed records may appear more than once after multiple registrations.
- Input validation for empty fields and invalid email addresses has not been implemented.

## 🔮 Future Improvements

- Add input validation for name, email, and phone number.
- Save the selected course along with student details.
- Add a Clear Form button.
- Add a Search Student feature.
- Add an Update and Delete Student feature.
- Use SQLite for more structured student data management.
- Improve the user interface with a table to display registrations.
- Add a success message only after the data has been saved successfully.

## 👩‍💻 Project Information

- **Project Name:** Student Registration App
- **Programming Language:** Python
- **GUI Framework:** CustomTkinter
- **Storage:** Text File
- **Project Type:** Desktop Application
- **Purpose:** To demonstrate GUI development, input handling, dropdown menus, and file operations in Python.

---

⭐ If you find this project useful, consider giving the repository a star on GitHub.
