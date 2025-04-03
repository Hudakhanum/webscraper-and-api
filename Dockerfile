# 1. Use an official Python image
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy all files and folders into the container
COPY . .

# 4. Install dependencies (ensure pytest is installed)
RUN pip install --no-cache-dir -r requirements.txt && pip install pytest

# 5. List the contents of the directory for debugging
RUN ls -R /app

# 6. Run pytest on the tests/test_black.py file
CMD ["pytest", "tests/"]



