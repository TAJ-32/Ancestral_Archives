# Step 1: Build the React app
FROM node:20 AS builder

WORKDIR /app
COPY frontend/package*.json ./
RUN npm install

COPY frontend ./
RUN npm run build  # This generates the `dist/` folder

# Step 2: Use Nginx to serve the built files
FROM nginx:alpine

# Copy the built React app to the Nginx directory
COPY --from=builder /app/dist /usr/share/nginx/html

# Copy the custom nginx.conf from the nginx folder
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf
