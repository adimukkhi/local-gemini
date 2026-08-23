# Stateful Gemini AI Chat Client

A minimalist, responsive, local dark-themed AI chat interface powered by Google's official **Gemini 3.5 Flash Lite** model and built using **Flask**.

This web application implements a robust server-side state tracking architecture to maintain conversation context across multiple turns seamlessly, bypassing standard stateless constraints while avoiding client-side layout leakage.

## 🚀 Features

- **Multi-Turn Contextual Tracking:** Maintains an unbroken conversation history stream, allowing Gemini to remember and refer to past messages.
- **Disk-Based State Persistence:** Uses `Flask-Session` with filesystem storage to handle context data seamlessly, entirely avoiding standard 4KB browser cookie constraints.
- **Data Pipeline Isolation:** Keeps API payloads completely pure by separating raw text conversation logs from front-end Markdown/HTML layout conversions.
- **Auto-Cleaning Lifecycle:** Integrated structural hooks clear server-side session cache directories on every native application execution restart.
- **Clean Responsive Dark UI:** Minimalist pill-shaped input elements and stylized visual layout containers.

## 🛠️ Tech Stack

- **Backend:** Python 3, Flask
- **AI Core:** Google GenAI SDK (`gemini-3.5-flash-lite`)
- **Data Layer:** Flask-Session (Filesystem)
- **Formatting:** Python-Markdown Engine
- **Frontend:** HTML5, CSS3, Jinja Templates

## 📂 Project Directory Structure

```text
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── static/
│   └── styles.css
└── templates/
    └── index.html
```

## ⚙️ Installation & Local Setup

### 1. Clone the Repository
```bash
git clone https://github.com
cd YOUR_REPOSITORY_NAME
```

### 2. Install Dependencies
Ensure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a `.env` file in the root directory and add your Google Gemini API Key:
```text
GEMINI_API_KEY=your_actual_api_key_here
```

### 4. Run the Application
```bash
python app.py
```
Open your browser and navigate to `http://127.0.0`.

## 🔄 Route Lifecycles

- **`GET /`** : Renders the home screen interface and dynamically builds historical text components.
- **`POST /`** : Intercepts user prompt strings, maps structural type validations (`types.Content`), streams payloads to Google servers, and logs content blocks.
- **`GET /clear`** : Wipes the internal session storage file data, resets chat streams, and directs the browser back to a fresh home state.
