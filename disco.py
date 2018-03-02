server {

    listen 80;
    server_name not.configured.example.com;
    charset utf-8;

    location /static {
        alias /data/web/mydjango/static;
    }

    location / {
        proxy_pass http://web:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

}
