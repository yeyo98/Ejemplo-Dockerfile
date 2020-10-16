FROM node:10 AS build-env
WORKDIR /app
COPY . .
RUN npm install --production

FROM gcr.io/distroless/nodejs:10
COPY --from=build-env /app /app
WORKDIR /app
EXPOSE 3000
CMD ["hello_express.js"]