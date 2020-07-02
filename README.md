# Sports-App
Sporty


Run with uvicorn app.main:app --reload

Build Image

docker build -t sports .

Run

docker run --rm --network=host --name sports0 -p 8001 sports


