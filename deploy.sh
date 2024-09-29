# #!/bin/bash


sudo apt-get update
sudo apt-get install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa




sudo apt-get -y install python3.11 python3.11-venv python3-pip nginx


python3.11 -m venv box_venv



# # Activate the virtual environment
source box_venv/bin/activate

# # Install all required packages listed in 'requirements.txt'
pip install -r requirements.txt


cp env .env
# # Install Gunicorn, the WSGI server, if it's not listed in requirements.txt

# # Make database migrations (prepares migration files)



# python3.11 manage.py add_product

sudo systemctl stop gunicorn 

sudo cp gunicorn.service /etc/systemd/system/gunicorn.service


sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn

sudo systemctl status gunicorn > gunicorn.log 2>&1



if [ -f /etc/nginx/sites-available/pixilar_config ]; then
    echo "File exists in sites-available."
    sudo rm /etc/nginx/sites-available/pixilar_config
    sudo rm /etc/nginx/sites-enabled/pixilar_config

fi


# Copy the new Nginx configuration to the available sites directory
sudo cp pixilar_config /etc/nginx/sites-available/

# Create a symbolic link in the sites-enabled directory
sudo ln -s /etc/nginx/sites-available/pixilar_config /etc/nginx/sites-enabled/pixilar_config

# Reload the Nginx configuration
sudo systemctl restart  nginx

sudo systemctl status nginx

# Check the logs for the Gunicorn service

echo "Deployment complete. Your Django application should be running!"
