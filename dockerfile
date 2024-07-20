FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    git
RUN git clone https://github.com/Croissant-Team-Cinnamon-Bootcamp-2024/homework-week-3.git
WORKDIR /app/homework-week-3
RUN git checkout feat/aggregate-api && pip3 install -r requirements.txt

EXPOSE 8000

# ENTRYPOINT ["fastapi", "run", "main.py"]
CMD ["fastapi", "run", "main.py"]
