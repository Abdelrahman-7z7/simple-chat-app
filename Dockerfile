# Use an official Nginx image as the base image
FROM nginx:latest

# Copy the static files to the default Nginx HTML directory
COPY public/ /usr/share/nginx/html

# Expose port 8080
EXPOSE 8080

# Add a health check to periodically check the health of the app
# interval = 45s => means that the docker will check for the health of the app every 30 seconds
# timeout = 15s => waiting for the response for a 10s before pointing it out as a failure
# retries = 5 => before stating the health of the app it will go on a 3 trials
HEALTHCHECK --interval=45s --timeout=15s --retries=5 \
  CMD curl --fail http://localhost:8080 || exit 1


# Start Nginx when the container launches
CMD ["nginx", "-g", "daemon off;"]
