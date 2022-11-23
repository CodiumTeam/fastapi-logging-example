FROM node:19-slim

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci
COPY . .

RUN npm run build

CMD ["npm", "run", "preview", "--", "--host=0.0.0.0"]