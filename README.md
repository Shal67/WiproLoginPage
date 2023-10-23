# Login Page with Cached Frontend, Rate Limiting, and Load Balancing

## Overview

This project seamlessly integrates Django authentication with Azure Active Directory (Azure AD) services, enhancing security and user experience. Utilizing frontend technologies like HTML, JavaScript, and Django's `auth.contrib` module, it provides robust login functionality. Additionally, it incorporates frontend session management, Azure AD integration and advanced features like rate limiting and load balancing.

## Features

- **Django Authentication:** Utilizes `auth.contrib` for secure user authentication and session management. Functions are defined in `views.py` to handle authentication logic.
- **HTML and JavaScript Integration:** Frontend layout created using HTML. JavaScript used for interactive user experiences and frontend session storage.
- **URL Configuration:** Integrates frontend and backend by defining appropriate URLs in `urls.py`.
- **Frontend Sessions:** Cached frontend sessions provide a seamless user experience. User credentials stored in frontend session storage.
- **IndexedDB Storage:** Cached session user credentials stored in IndexedDB for local storage and offline access.
- **Local Credential Clearing:** User credentials cleared locally after successful login to enhance security.
- **Azure Active Directory Integration:**
  - Registered Django app with Azure Active Directory.
  - Created a user in Azure AD tenant.
  - Added Azure AD configurations to the Django project.
  - Integrated the `MsalMiddleware` class from the MS-identity-web library into the project's Middleware in the settings file.
  - Implemented Azure AD login form using OAuth code flow.
  - Added Single Sign-On (SSO) functionality to Django Runserver.
- **Additional Features:**
  - Implemented rate limiting to protect against brute-force attacks.
  - Added load balancing for optimized server performance and reliability.

## Prerequisites

- **Backend Server:** Ensure Django and required Python packages are installed.
- **Frontend Server:** Node.js and npm for running the frontend application.

## Installation and Usage

1. **Clone the Repository:**
   ```shell
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install Backend Dependencies:**
   ```shell
   pip install -r requirements.txt
   ```

3. **Run Backend Server:**
   ```shell
   python manage.py runserver
   ```

4. **Navigate to Frontend Directory:**
   ```shell
   cd frontend
   ```

5. **Install Frontend Dependencies:**
   ```shell
   npm install
   ```

6. **Run Frontend Server:**
   ```shell
   npm start
   ```

7. **Access the Application:**
   Open your web browser and navigate to `http://localhost:3000`.

8. **User Login:**
   - Users can log in using their Azure AD credentials.
   - SSO provides a seamless experience across the application.

## Security Measures

- **Rate Limiting:** Protects against brute-force attacks by limiting login attempts.
- **Load Balancing:** Optimizes server performance and ensures high availability.


