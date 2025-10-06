FROM nginx:alpine
COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf.template /etc/nginx/templates/default.conf.template
ENV API_HOST=backend API_PORT=8000
EXPOSE 80
