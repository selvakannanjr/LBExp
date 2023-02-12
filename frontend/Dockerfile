### STAGE 1: Build ###
FROM node:18.14-alpine AS build
WORKDIR /usr/src/app
COPY package.json package-lock.json ./
RUN npm install
COPY . .
RUN npm i && npm run ng build
### STAGE 2: Run ###
FROM nginx:alpine
WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
COPY --from=build /usr/src/app/dist/interview .
ENTRYPOINT [ "nginx","-g","daemon off;" ]