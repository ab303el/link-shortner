# link-shortner

A Django-based web application for shortening long URLs into manageable links.

## **Features**
- Shorten long URLs into concise, user-friendly links.
- Custom link alias creation.
- URL click tracking (optional).
- Simple and responsive user interface.

## **Technologies Used**
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript (optional tailwind css for styling)
- **Database**: SQLite (default, can be replaced with PostgreSQL/MySQL)
- **Version Control**: Git

## **Setup Instructions**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ab303el/link-shortner.git
   cd link-shortner
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate   # Linux/Mac
   .\env\Scripts\activate    # Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Open your browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000).

## **Future Enhancements**
- User authentication for managing links.
- Analytics dashboard for tracking link performance.
- API for integration with third-party services.

## **Contributions**
Contributions, issues, and feature requests are welcome! Feel free to fork this repository and submit a pull request.

## **License**
This project is licensed under the [MIT License](LICENSE).

---

