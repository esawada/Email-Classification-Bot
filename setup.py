from setuptools import setup, find_packages

setup(
    name='email_classification_bot',
    version='0.1.0',
    author='esawada',
    description='A cloud-based email classification bot with QR code and keyword detection.',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'imapclient',
        'email-validator',
        'beautifulsoup4',
        'python-dotenv',
        'sqlalchemy',
        'psycopg2-binary',  
        'pyzbar',
        'opencv-python',
        'pdf2image',
        'Pillow',
        'PyMuPDF',
        'schedule',
        'loguru',
        'pytest',
        "mysql-connector-python",
        'flask',           # Optional: for dashboard
        'spacy',           # Optional: for advanced NLP
        'gunicorn',        # Optional: if deploying Flask
    ],
    entry_points={
        'console_scripts': [
            'email-bot=email_bot.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
