<div align="center">

# 📸 SnapAttend

### Making Attendance Faster Using AI

SnapAttend is an intelligent attendance management system that leverages facial recognition technology to streamline the attendance process. Built with Python and Streamlit, it provides a seamless experience for both teachers and students.

[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![Supabase](https://img.shields.io/badge/Supabase-Database-3ECF8E?style=for-the-badge&logo=supabase)](https://supabase.com/)
[![License](https://img.shields.io/badge/License-Open%20Source-yellow?style=for-the-badge)](LICENSE)

**[🌐 Live Demo](https://hamza-snapattend.streamlit.app)** &nbsp;|&nbsp; **[📋 Report Bug](https://github.com/upskill-hamza/SnapAttend/issues)** &nbsp;|&nbsp; **[✨ Request Feature](https://github.com/upskill-hamza/SnapAttend/issues)**

</div>

---

## 🎯 Features

<div align="center">

| Feature | Description |
|---|---|
| 🤖 **AI Facial Recognition** | Automatically recognize and verify student identities |
| 👥 **Dual Interface** | Separate dashboards for teachers and students |
| 📱 **QR Code Generation** | Generate QR codes for quick attendance verification |
| 🔐 **Secure Authentication** | Login system with bcrypt password encryption |
| 🎙️ **Audio Analysis** | Voice/audio recognition for enhanced verification |
| ☁️ **Cloud Database** | Supabase-powered cloud storage and data management |
| 🌐 **Multi-Platform** | Streamlit-based web app, accessible anywhere |

</div>

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology |
|---|---|
| **Frontend** | Streamlit |
| **Backend** | Python 3.8+ |
| **Face Recognition** | face_recognition, dlib, scikit-learn |
| **Audio Processing** | librosa, resemblyzer |
| **Database** | Supabase |
| **Security** | bcrypt |
| **Image Processing** | Pillow (PIL) |
| **QR Code** | segno |
| **Data Handling** | NumPy, Pandas |

</div>

---

## 📋 Prerequisites

- Python **3.8** or higher
- **pip** (Python package manager)
- **Git**

---

## 🚀 Installation

**1. Clone the repository**
```bash
git clone https://github.com/upskill-hamza/SnapAttend.git
cd SnapAttend
```

**2. Create a virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

---

## 🎮 Running the Application

```bash
streamlit run app.py
```

<div align="center">

The app will open in your browser at **http://localhost:8501**

</div>

---

## 📁 Project Structure

```
SnapAttend/
├── app.py                      # Main application entry point
├── requirements.txt            # Python dependencies
├── src/
│   └── screens/
│       ├── home_screen.py      # Landing page for login selection
│       ├── teacher_screen.py   # Teacher dashboard
│       └── student_screen.py   # Student dashboard
└── README.md
```

---

## 👥 Usage

<div align="center">

### 🧑‍🏫 For Teachers

</div>

1. Login with teacher credentials
2. Upload or capture student photos for facial recognition training
3. Generate attendance reports
4. Monitor class attendance in real-time
5. Generate and share QR codes for attendance marking

<div align="center">

### 🎓 For Students

</div>

1. Login with student credentials
2. Mark attendance using facial recognition
3. Scan QR codes to verify attendance
4. View personal attendance records

---

## 🔐 Security Features

<div align="center">

| Feature | Detail |
|---|---|
| 🔒 **Password Encryption** | Secured using bcrypt hashing |
| 🛡️ **Secure Authentication** | Session-based authentication system |
| ☁️ **Data Privacy** | Cloud storage managed securely via Supabase |

</div>

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

```bash
# 1. Fork the repository
# 2. Create your feature branch
git checkout -b feature/AmazingFeature

# 3. Commit your changes
git commit -m 'Add some AmazingFeature'

# 4. Push to the branch
git push origin feature/AmazingFeature

# 5. Open a Pull Request
```

---

## 📝 License

<div align="center">

This project is currently unlicensed. Feel free to use it for educational and personal projects.

</div>

---

## 💬 Support & Issues

<div align="center">

If you encounter any issues or have suggestions:

**[🐛 Open an Issue](https://github.com/upskill-hamza/SnapAttend/issues)** &nbsp;|&nbsp; **[🔍 Browse Existing Issues](https://github.com/upskill-hamza/SnapAttend/issues)**

</div>

---

## 🙏 Acknowledgments

<div align="center">

[Streamlit](https://streamlit.io/) &nbsp;•&nbsp; [face_recognition](https://github.com/ageitgey/face_recognition) &nbsp;•&nbsp; [Supabase](https://supabase.com/)

---

Made with ❤️ by **[Hamza](https://github.com/upskill-hamza)**

</div>
