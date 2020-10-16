FROM python:3 as build

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

FROM gcr.io/distroless/python3
COPY --from=build /app .

EXPOSE 4000

CMD ["python", "app.py"]