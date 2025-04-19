# MovieSeatBooking
In this project, I stepped into the shoes of a web UI designer and front-end developer for a cinemas and theater management company, helping to enable users to book and view their seats smoothly across different devices.

# MovieSeatBooking
In this project, I stepped into the shoes of a web UI designer and front-end developer for a cinemas and theater management company, helping to enable users to book and view their seats smoothly across different devices.

# Movie Seat Booking System 🎟️

A fully functional web application built using **Django**, **Bootstrap**, and **jQuery**, allowing users to select and book movie theater seats in real-time. Seats once booked are saved in the database and shown as unavailable (red) on reload.

---

## 🌐 Live Features

- 🌻 Interactive seat selection grid
- ✅ Real-time seat availability check
- 🔒 Prevents double booking of seats
- 📌 Responsive layout with Bootstrap
- 🎨 Visual feedback:  
  - 🟩 Green for available  
  - 🟧 Orange for selected  
  - 🔴 Red for booked  
- 🔍 Zoom In/Out feature for small screens

---

## 📁 Project Structure

```
theater_booking/
├── booking/
│   ├── migrations/
│   ├── templates/
│   │   └── booking/
│   │       └── seat_booking.html
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── theater_booking/
│   ├── settings.py
│   └── urls.py
└── manage.py
```

---

## ⚙️ Technologies Used

| Tool        | Purpose |
|-------------|---------|
| **Django**  | Backend framework, handles views, database, routing |
| **SQLite3** | Default database to store seat data |
| **Bootstrap** | UI components, responsive layout |
| **jQuery**  | DOM manipulation and real-time interactivity |
| **HTML/CSS/JS** | Frontend structure and styling |

---

## 🖥️ Setup Instructions

### 🔧 Prerequisites

- Python 3.8+
- pip
- Virtual environment (recommended)

### 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/ShashankGoutam/MovieSeatBooking.git
cd movie-seat-booking

# Create and activate virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Run the development server
python manage.py runserver
```

---

## 🧪 How It Works

- Seats are rendered from the database using Django templates.
- Users can click on available seats to select them.
- jQuery updates a hidden form field with selected seat IDs.
- On form submission, Django marks those seats as `booked=True`.
- Booked seats are shown in red when the page reloads.

---

## 👥 Contributors

- **Shashank Goutam** – Fullstack Development, UI Design, Django Integration  
- **Tanmay Vemuri** – jQuery, Booking Logic, Seat Model Logic  
- **Aditya Chitransh** – Styling, Zoom Feature, Documentation

---

## 🔗 Links

- [Django Docs](https://docs.djangoproject.com/en/5.2/)
- [Bootstrap Docs](https://getbootstrap.com/docs/5.3/)
- [jQuery Docs](https://api.jquery.com/)
