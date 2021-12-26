FROM python:3.10-alpine as base 

FROM base as builder
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories \
    && apk update \
    && apk add --no-cache gcc musl-dev libffi-dev openssl-dev g++ \
    && pip install -i https://pypi.tuna.tsinghua.edu.cn/simple poetry
WORKDIR /proj
COPY pyproject.toml poetry.lock ./
RUN python -m venv /env && . /env/bin/activate && poetry install --no-dev

FROM base
COPY --from=builder /env /env
WORKDIR /biz
COPY app app/
COPY bin/bootstrap.sh bin/
RUN mkdir data
RUN chmod +x bin/bootstrap.sh
ENV HOST="0.0.0.0" \
    PORT=80
EXPOSE ${PORT}
CMD ["./bin/bootstrap.sh"]
