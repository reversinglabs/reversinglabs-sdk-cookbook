FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN apt update && \
    apt install -y wget unzip curl && \
    rm -rf /var/lib/apt/lists/*

RUN export latest=$(curl "https://api.github.com/repos/reversinglabs/reversinglabs-sdk-cookbook/releases/latest" | grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/') && \
    wget "https://github.com/reversinglabs/reversinglabs-sdk-cookbook/archive/refs/tags/$latest.zip" && \
    unzip "$latest.zip" && \
    rm "$latest.zip"

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]




