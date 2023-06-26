FROM python:3

# Make a directory for our app
WORKDIR /var/www/app

# Copy all code files with dependencies
COPY . .

# install all dependencies
RUN pip3 install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy code, and project essentials
COPY app ./app

# Expose application port
EXPOSE 5000

CMD python3 app.py