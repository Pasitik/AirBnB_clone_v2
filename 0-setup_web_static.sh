#!/usr/bin/env bash
#script that sets up your web servers for the deployment of web_static


sudo apt-get update -y
sudo apt-get install nginx -y

folder_name="/data"

if [ ! -d "$folder_name" ]; then
        sudo mkdir "$folder_name"
fi
sudo chown -R "$USER:$USER" "/data"

folder_name="/data/web_static/"

if [ ! -d "$folder_name" ]; then
        mkdir "$folder_name"
fi

folder_name="/data/web_static/releases"

if [ ! -d "$folder_name" ]; then
        mkdir "$folder_name"
fi

folder_name="/data/web_static/shared"

if [ ! -d "$folder_name" ]; then
        mkdir "$folder_name"
fi

folder_name="/data/web_static/releases/test/"

if [ ! -d "$folder_name" ]; then
        mkdir "$folder_name"
fi

echo "Hello World! updated" > "$folder_name"/index.html

if [ ! -d "/data/web_static/current" ]; then
        #mkdir "/data/web_satic/current"
        ln -s "/data/web_static/releases/test/" "/data/web_static/current"
else
        rm -r "/data/web_static/current"
        #mkdir "/data/web_satic/current"
        ln -s "/data/web_static/releases/test/" "/data/web_static/current"
fi

sudo chown -R $USER:ubuntu "/data"


# Get the hostname of the server
HOSTNAME=$(hostname)

# Define the Nginx configuration file path
NGINX_CONF_PATH="/etc/nginx/sites-available/default"

sudo chown -R $USER:$USER "/etc/nginx"
sudo chown -R $USER:$USER "/var/www"
sudo chown -R $USER:$USER "/usr/share/nginx/html"

REDIRECT="\n\tlocation /redirect_me {\n\t\treturn 301 http://dev-israel.tech;\n\t\tadd_header X-Served-By $HOSTNAME;\n\t}\n"
FILE="/etc/nginx/sites-available/default"

ERRORFILE="/usr/share/nginx/html/404error.html"
FOUR="Ceci n'est pas une page"
ERRORREDIRECT="\n\terror_page 404 /404error.html;\n\tlocation = /404error.html {\n\t\troot /usr/share/nginx/html;\n\t\tinternal;\n\t\tadd_header X-Served-By $HOSTNAME;\n\t}\n"


hbnb_static_file="/data/web_static/current"
hbnb_static_serve="\n\tlocation = /hbnb_static {\n\t\talias /data/web_static/current;\n\t\tadd_header X-Served-By $HOSTNAME;\n\t}\n"


echo "Helo World!" > "/var/www/html/index.nginx-debian.html"
sed -i "37i\ $hbnb_static_serve" "$FILE"
sed -i "37i\ $REDIRECT" "$FILE"
echo "$FOUR" > "$ERRORFILE"
sed -i "37i\ $ERRORREDIRECT" "$FILE"

#sudo sed -i "33i\ \n\t\tadd_header X-Served-By $HOSTNAME;\n\t" "$FILE"
hbnb_static_path="/var/www/html/hbnb_static"


sudo service nginx restart


