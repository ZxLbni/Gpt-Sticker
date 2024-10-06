# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8443, 80, 88, and 443 available to the world outside this container
EXPOSE 8443
EXPOSE 80
EXPOSE 88
EXPOSE 443

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Run bot.py when the container launches
CMD ["python", "bot.py"]
