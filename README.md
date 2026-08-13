# 🎉 Automated WhatsApp Birthday Wisher

An automated Python script designed to generate personalized birthday greetings and send them directly to a specific WhatsApp group using **Green API** and **GitHub Actions**.

## 🚀 Features
* **Dynamic Image Generation:** Automatically crops student photos and overlays them perfectly onto a custom birthday template using the `Pillow` library.
* **Automated Messaging:** Sends the generated image along with a customized greeting caption to a WhatsApp group via **Green API**.
* **Fully Automated Scheduling:** Runs daily at midnight (Sri Lanka time) using a **GitHub Actions** Cron job. 
* **Secure Configurations:** API keys and sensitive group IDs are securely managed using GitHub Environment Secrets.

## 🛠️ Technologies Used
* **Python 3.10**
* **Pillow (PIL)** - For dynamic image processing and text rendering
* **Requests** - For handling HTTP requests
* **Green API** - For seamless WhatsApp integration
* **GitHub Actions** - For CI/CD and automated task scheduling

## 📂 Repository Structure
* `main.py`: The core script that handles data parsing, image generation, and API communication.
* `data.json`: Contains the local database of student details (Names, Birthdays, Photo file names).
* `Templates/`: Stores the base graphic templates for the birthday posts.
* `student_photos/`: Contains the raw, unedited photos of the students.
* `.github/workflows/`: Contains the YAML configuration file for GitHub Actions automation.

## ⚙️ Setup & Execution
This project is configured to run automatically in the cloud via GitHub Actions. To run or test it locally:
1. Clone this repository.
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up local environment variables for `ID_INSTANCE`, `API_TOKEN`, and `GROUP_ID`.
4. Run the main script: `python main.py`

---
*Developed by Nirmala Sandaruwan*
