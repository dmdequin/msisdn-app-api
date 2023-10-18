{* pass in environment variables to nginx at runtime *}

server {
    {* port server will listen on *}
    listen      ${LISTEN_PORT};

    {* map /static url to /vol/static in system *}
    location /static {
        alias /vol/static;
    }

    {* map the rest of the urls *}
    location / {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        {* uwsgi_pass              http://127.0.0.1:8000;*}
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    10M;
    }
}
