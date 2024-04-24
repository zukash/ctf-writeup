FROM node:18-alpine

ENV NODE_ENV=production
WORKDIR /app
COPY ["package.json", "package-lock.json*", "./"]
RUN npm install --production

COPY index.js index.js
COPY public public
COPY views views
COPY flag.txt flag.txt

EXPOSE 3000
CMD ["node", "index.js", "server"]
