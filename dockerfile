FROM keymetrics/pm2:16-alpine
# 1. add helpful packages
RUN apk add --no-cache --update alpine-sdk git wget python3 python3-dev ca-certificates musl-dev libc-dev gcc bash nano linux-headers  && \
    python3 -m ensurepip && \
    pip install psycopg2 \
RUN docker-compose --version
# 2. create user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
# 3. copy requirements.txt file to temp folder and installs required packages
RUN mkdir -p /home/appuser/temp
ADD ./requirements.txt /home/appuser/temp/requirements.txt
RUN pip3 list
RUN pip3 install -r /home/appuser/temp/requirements.txt
# 4. copy project
RUN mkdir -p /home/appuser/project
COPY ./*.py /home/appuser/project/
COPY ./*.json /home/appuser/project/
# 5. grant permission
RUN chown appuser /home/appuser/project
# 6. setting enviroment
WORKDIR /home/appuser/project/
USER appuser
# 7. use pm2-logrotate
RUN pm2 install pm2-logrotate