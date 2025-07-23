🧪 Remaining Shelf-Life Estimation

A Django-based web application for predicting the remaining shelf life of items using machine learning. This project includes two user roles: **Remote User** and **Service Provider**, with separate interfaces and functionalities.

---

🚀 Features

- 🔒 Remote User registration & login
- 📊 Upload and process shelf-life datasets
- 📈 Predict remaining shelf life using trained models
- 📂 Download trained models
- 📉 View prediction results and analysis charts
- 📋 Admin panel for managing users and data

---

 🛠️ Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML, CSS
- **Database**: MySQL
- **ML Model**: Integrated within Django views using Pandas/Sklearn (check `Service_Provider/views.py`)

---

⚙️ Setup Instructions

1. Clone the repository
git clone https://github.com/Hemanth-Kumar-Yadlapalli/Remaining_Shelf_Life_Estimation.git
 
2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

3. Install dependencies
pip install -r requirements.txt

4. Set up the database
Make sure MySQL is running. Update settings.py with your own DB credentials.

Then run:python manage.py makemigrations
python manage.py migrate

5. Run the server
python manage.py runserver

📁 Project Structure
remaining_shelf_life_estimation/
├── Remote_User/           # Remote user app
├── Service_Provider/      # Service provider app
├── Template/htmls/        # HTML templates
├── manage.py
├── requirements.txt
├── Datasets.csv
├── labeled_data.csv
└── remaining_shelf_life_estimation/  # Main Django project folder

🙌 Credits
Developed by Hemanth Kumar Yadlapalli, Venkata Sri Karthik Bokka, Satya Siva Anurag Varma Mudunuri, Binli Gona
(Django + ML Final Year Project)

