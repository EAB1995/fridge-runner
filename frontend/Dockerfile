
FROM node:16 AS build

WORKDIR /app

COPY fridge-runner/package*.json ./
RUN npm install

COPY fridge-runner/. .

RUN npm run build

FROM nginx:stable-alpine

COPY --from=build /app/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]



