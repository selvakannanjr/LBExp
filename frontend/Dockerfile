### STAGE 1: Build ###
FROM node:18.14-alpine AS build
WORKDIR /usr/src/app
COPY package.json package-lock.json ./
RUN npm install -g @angular/cli
RUN npm install
EXPOSE 4200
CMD ["ng","serve","--host","0.0.0.0"]
