# About website 
Cafe- is a restaurant website. It has 4 sub domains-menu,about,contactus,services.

#proceedure to start the website
1>Start a Ubuntu machine
2>Install Apache 
3>create an index.html file in /var/www/ folder
4> goto a browser and type localhost/ in the url


#To change domain name
1. Create a configuration file for the virtual host. 
▪ sudo nano /etc/apache2/sites-available/awesomeweb.conf

2.Add this in the file
<VirtualHost *:80>
 ServerName awesomeweb
 DocumentRoot /var/www/awesomeweb
 ErrorLog ${APACHE_LOG_DIR}/error.log
 CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

3.Enable the virtual host using cmd:
▪ sudo a2ensite awesomeweb.conf

4. Create DNS entry (Edit Hosts File):
-Open the hosts file in the editor:
▪ sudo nano /etc/hosts
- Add the following line:
▪ 127.0.0.1 awesomeweb

5. Create the website directory awesomeweb using cmd:
▪ sudo mkdir /var/www/awesomeweb
-Place your  files and folders in cafe directory  (HTML) in the /var/www/awesomeweb 
directory

6. Restart Apache2 
• sudo service apache2 restart

7. Open http://awesomeweb in web browser
• firefox http://awesomeweb









