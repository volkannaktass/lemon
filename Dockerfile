
FROM public.ecr.aws/lambda/python:3.9

ENV TZ=UTC
ENV PYTHONUNBUFFERED=1
COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . ${LAMBDA_TASK_ROOT}

WORKDIR ${LAMBDA_TASK_ROOT}/src/
#RUN pip3 freeze > requirements.txt



CMD ["handler.hello"]
