# Use the official Node.js image as the base image
FROM node:20.2.0-slim

# Set the working directory in the container
WORKDIR /frontend

# Copy the frontend source code into the container
COPY . .

# Install dependencies
RUN npm install

# Expose the port on which the React app is running
EXPOSE 5173

# Command to launch the React app
CMD ["npm", "run", "dev"]
