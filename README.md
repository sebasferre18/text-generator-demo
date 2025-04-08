# Text Generator Demo
This is a small demo focused on text generation using Google's FLAN-T5 small model for testing purposes.

## Requirements

You need [Docker](https://www.docker.com/) to deploy this demo.

The Docker container is an instance of a Python 3.9 image. Docker will install all the dependencies needed for you inside that container.

### Dependencies
- PyTorch
- Transformers
- Accelerate
- FastAPI
- Requests
- Uvicorn
- SentencePiece

## Deployment

1. Open the command line of your system.
2. Clone this project.
3. Go to the project's folder on the command line.
4. With Docker installed, build the container:

```
docker build -t text-generator-demo .
```

5. Finally, to deploy this demo with Docker:

```
docker run -it -p 127.0.0.1:7860:7860 text-generator-demo
```

And you're ready to go! Now you can go to /docs in the browser or send POST requests to /generate in order to generate text. The query param key for the text input is called "text".
