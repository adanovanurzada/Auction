COPY req.txt /app/
RUN pip install gunicorn
RUN pip install setuptools
RUN pip install --upgrade pip && \
    pip install -r req.txt

COPY nginx/nginx.conf /etc/nginx/conf.d/

COPY . /app/