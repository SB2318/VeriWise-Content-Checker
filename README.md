# 🔍 VeriWise-Content-Checker

**VeriWise-Content-Checker** is an intelligent, modular Python API system designed to help you validate and verify content efficiently across multiple aspects:

- ✅ **Plagiarism Detection:** Detect content similarity using TF-IDF & cosine similarity algorithms.
- ✅ **Grammar Checking:** Identify grammar and spelling issues using LanguageTool.
- ✅ **Grammar Suggestion:** Provide detailed grammar improvement suggestions.
- ✅ **Copyright and Medical Content Verification:** Extract text from images using Easyocr and OpenCV to cross-check with a database of copyrighted medical content providers.

---

## 📸 Screenshot Examples

### Plagiarism Detection:
![Screenshot 2025-05-21 002104](https://github.com/user-attachments/assets/1d037f72-d068-4586-b8f2-d08b25296ef3)

### Grammar Suggestion:

![WhatsApp Image 2025-05-21 at 12 20 51 AM](https://github.com/user-attachments/assets/dd412028-3ace-4eb9-9321-c4e3d0691c30)

---

## 🛠️ Requirements

Make sure you have the following Python packages installed:

- fastapi
- gunicorn

- easyocr
- opencv-python
- numpy
- requests
- Pillow
- difflib

- beautifulsoup4
- language_tool_python

- scikit-learn
- pocketbase  # Datasource for plagiarism detection
- PyMuPDF


You can install all dependencies using:

```
pip install -r requirements.txt

```

## 🚀 How to Run

1. Clone the repository

```
git clone https://github.com/SB2318/VeriWise-Content-Checker.git
cd VeriWise-Content-Checker

```

2. Install the dependencies

```
pip install -r requirements.txt

```

3. Run the application

```
uvicorn main:app --reload

or

python run.py

```
4. Open your web browser and navigate to `http://127.0.0.1:5000`

## ⚙️ Features Overview

- **Plagiarism Detection:** Submit text to check for similarity against existing content.
- **Grammar Check:** Submit text to get a grammar correctness score (predict score).
- **Grammar Suggestion:** Get detailed suggestions to improve grammar and spelling errors.
- **Copyright Checker:** Upload images or text to verify against copyrighted medical content provider data.

## 🙌 Contribution & Feedback

Feel free to open issues or pull requests to improve the system. For feedback or any queries, you can contact the maintainer, via GitHub or email.


