# Use official Node.js image
FROM node:18-slim

# Set working directory
WORKDIR /app

# Copy files
COPY package.json package-lock.json ./
COPY index.js .

# Install dependencies
RUN npm install

# Expose port
EXPOSE 3000

# Run the Express app
CMD ["node", "index.js"]
