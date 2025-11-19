# Kuwait University Guide (KUGuide)

A web platform for Kuwait University students that centralizes study resources, FAQs, AI support, and career guidance into one place.

---

## 🎯 Project Goal

KUGuide is designed to reduce common KU student struggles by:

- Providing a **reliable platform** for students to share notes, tips, and resources (instead of messy WhatsApp chats).
- Centralizing **study materials** (lecture notes, slides, textbooks, practice questions).
- Answering **frequently asked administrative & academic questions** (withdrawal dates, registration, graduation, etc.) via FAQ + AI chatbot.
- Helping **current students and graduates** discover in-demand **skills and certifications** in the Kuwaiti job market through collaboration with **OSTA**.

---

## 👥 Target Users

- **Fresh Students**

  - Need basic guidance about systems, dates, and study resources.
  - Can access and share notes, books, and study materials.

- **Students by Major**

  - Need career-oriented help more than basic academic help.
  - Can explore **certifications and skills** related to their major that are required in the job market.

- **Graduates (through OSTA)**
  - Access **training**, **internships**, **career events**, and **job-related announcements**.

---

## 🧩 Main Features

- **Frequently Asked Questions (FAQ)**

  - Organized by categories such as:
    - General Questions
    - Career Guidance
    - Account Help
    - Details
    - Technical Help
  - If the FAQ doesn’t answer it, the user can pass the question to the **AI chatbot**.

- **AI Chatbot**

  - Uses an AI language model to answer questions instantly.
  - Supports **voice commands** to help users with disabilities.
  - Handles common admin/academic questions (e.g., withdrawal dates, system opening/closing, registration periods).

- **Career Guidance**

  - Shows **required skills** for different roles (e.g., Web Designer → HTML, CSS, Java, UI/UX principles).
  - Lists **certifications required in the market** per major.
  - Highlights **internship and training opportunities** via OSTA.

- **User Accounts & Profiles**

  - Users register with **name, university ID, and KU email**.
  - After login, users can:
    - Access chat rooms and resources
    - Explore careers
    - Upload/update profile picture
  - Major can be inferred from the **university ID** format.

- **Responsive Design**
  - Layout adapts to **desktop, tablet, and mobile**.
  - On desktop: full navbar always visible.
  - On mobile: **hamburger menu** for navigation.
  - Same color scheme and font across all pages for consistency.

---

## ✅ Requirements

### Functional Requirements

- Users can:
  - **Sign in** with KU email and password.
  - **Edit profile** (name, bio, picture).
- Chatbot:
  - Responds automatically to user questions.
  - Example: “How to show careers?” → returns a clear, step-by-step answer.
- Career page:
  - Recommends **job lists** based on user major (e.g., MIS → MIS-related jobs).

### Non-Functional Requirements

- User accounts must be **protected through authentication**.
- Website must work across **different devices** (responsive).
- Supports users with disabilities (font size, clear contrast, spacing).

### User Experience Requirements

- Navigation must be **simple and predictable**.
- All pages share a **consistent theme** (colors, typography).
- Error messages (e.g., invalid login) must **explain what went wrong and how to fix it**.

---

## 🏗️ Website Architecture & Navigation Flow

High-level structure:

- **Home Page**

  - Navigation bar.
  - Login / Signup.
  - Website introduction.
  - Live updates & announcements.
  - FAQ highlights.
  - **Navigation:** one-click access to all main pages.

- **FAQ Page**

  - Hub of common questions, grouped by topic (e.g., “Portal”).
  - **Navigation:** filter and search by subject.
  - Supports escalation to AI chatbot.

- **User Profile Page**

  - View: Name, ID, Major, Picture.
  - Edit: Bio, Picture.
  - Access saved resources.
  - **Navigation:** appears as a dropdown after user login.

- **Career Guidance Page**

  - Certifications & required skills for all **CBA majors**.
  - Internship and training opportunities.
  - **Navigation:** always available via navbar link.

- **Contact Page**

  - For feedback, technical support, and general inquiries.
  - **Navigation:** accessible from both footer and navbar.

- **Sign-In Page**

  - Login with **KU email + password**.
  - “Forgot Password” option.
  - **Flow:**
    - Credentials verified by backend.
    - If successful → redirect to **Profile Page**.
    - If failed → show error (“Invalid ID or Password. Please try again”).
    - User can reset password or go back to Home.

- **Responsive Navigation**
  - Full navbar on large screens.
  - Collapsible / hamburger menu on small screens.
  - Uses semantic HTML (`<header>`, `<nav>`, `<main>`, `<footer>`) for structure and accessibility.

---

## 🖼️ Wireframes & Mockups

Wireframes were prototyped using **Figma** and **Excalidraw** and include:

- **Home Page**

  - Navbar on top.
  - Greeting + website introduction.
  - Announcements scrollbar.
  - Quick access section acting as a “map” of key features.

- **FAQ Page**

  - List of FAQs under 5 main categories.
  - Integrated chatbot area where users can type questions.

- **Career Page**

  - Two main sections:
    - Skills required for **fresh KU students** (Word, PowerPoint, Excel, Teams).
    - Certifications required in the market per **CBA major**.

- **Contact Page**
  - Direct contact (phone, email).
  - Form with (Name, KU Email, Message) to reach IT team.

---

## 📱 Responsive Design & Accessibility

- Each page (Home, Career, Profile, FAQ, Contact) follows a **consistent structure**:
  - Header (KU logo + navbar)
  - Main content (page-specific blocks)
  - Footer (links and contact info)
- Uses:
  - **Media queries** and **flex layouts** to adapt to screen sizes.
  - Readable text sizes, clear color contrast, and spacing to support accessibility.
  - Proper spacing for buttons and inputs for mouse/touch use.

---

## 🧪 Interactivity & User Input Handling

Planned interactivity includes:

- **Form validation** on login, signup, and contact forms.
- **Clear error messages** (e.g., wrong username/password).
- **Dynamic FAQ interactions** (accordions, toggles, search/filter).
- **Chatbot input handling** with support for both text and voice commands.
- Pop-up messages, dropdown menus, and other UI enhancements to improve usability.

---

## 🧰 Technology Stack

- **HTML5** – structure and semantic layout.
- **CSS3** – styling and layout.
- **JavaScript** – interactivity and form handling.
- **Bootstrap 5** – responsive grid system, components (navbar, buttons, forms).
- **Design Tools**
  - Figma
  - Excalidraw

---

## 📚 Reference

- Connolly, R., & Hoar, R. (2021). _Fundamentals of Web Development_ (3rd ed.). Pearson Education.

---

## 👨‍💻 Team

- **Abdulrahman Mahmoud** – Target Users, Website Architecture & Navigation Flow
- **Abdullah Bukoubar** – Website Structure
- **Abdullah Alrashidi** – Interactivity & User Input Handling
- **Yousef Alfarhan** – Main Features, Responsive Design & Layout Planning
- **Aisha Alsubaie** – Concept / Problem, Technology Stack & Framework Specification

Section: **01A** – College of Business Administration, Department of ISOM.
