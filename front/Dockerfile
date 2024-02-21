# Étape de build
FROM node:18.16-alpine AS build
WORKDIR /usr/src/app
COPY package.json ./
RUN npm install
COPY . .
RUN npm run build

# Étape de serveur HTTP
FROM nginx:alpine
COPY --from=build /usr/src/app/dist/mon-app-angular /usr/share/nginx/html