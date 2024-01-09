FROM node
WORKDIR /frontend-server
COPY . .

EXPOSE 8080

RUN npm install
CMD npm run serve

