
FROM node:16

#In container 
WORKDIR /usr/src/app

COPY fridge-runner/package*.json ./

RUN npm install

COPY fridge-runner/ ./

#FOR PROD:
#RUN npm run build

#FROM nginx:stable-alpine

#COPY --from=build /app/build /usr/share/nginx/html

#CMD ["nginx", "-g", "daemon off;"]

#FOR DEV:

EXPOSE 3000

CMD ["npm", "start"]




