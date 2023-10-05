#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

folder1="/data/"
folder2="/data/web_static/"
folder3="/data/web_static/releases/"
folder4="/data/web_static/shared/"
folder5="/data/web_static/releases/test/"
file1="/data/web_static/releases/test/index.html"
slink="/data/web_static/current"
nginx_configs="/etc/nginx/sites-available/default"

if ! command -v nginx; then
        sudo apt-get update
        sudo apt-get install nginx -y
else
        echo "already installed"
fi

if [ ! -d "$folder1" ]; then
        sudo mkdir "$folder1"
fi

if [ ! -d "$folder2" ]; then
        sudo mkdir "$folder2"
fi

if [ ! -d "$folder3" ]; then
        sudo mkdir "$folder3"
fi

if [ ! -d "$folder4" ]; then
        sudo mkdir "$folder4"
fi

if [ ! -d "$folder5" ]; then
        sudo mkdir "$folder5"
fi

sudo touch "$file1"
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > "$file1"


if [ -L "$slink" ]; then
        sudo rm "$slink"
        echo "symbolic link removed"
        sudo ln -s "$folder5" "$slink"
        echo "Created symbolic link: $slink"
else
        sudo ln -s "$folder5" "$slink"
        echo "Created symbolic link: $slink"
fi

sudo chown -R ubuntu:ubuntu "$folder1"
sudo chown -R "$USER":"$USER" $nginx_configs
sudo sed -i '52i\       location /hbnb_static/ {\n              alias /data/web_static/current/;\n      }' "$nginx_configs"
sudo service nginx restart
