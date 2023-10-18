{* pass in environment variables to nginx at runtime *}

server {
    {* port server will listen on *}
    listen ${LISTEN_PORT};

    {* map /static url to /vol/static in system *}
    location /static {
        alias /vol/static;
    }

    {* map the rest of the urls *}
    location / {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    10M;
        {* proxy_pass           http://app:8000; *}
    }
}
