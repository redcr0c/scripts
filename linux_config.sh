#!/bin/bash

# Funktionen
function header() {
    clear
    echo "#####################################"
    echo "-----------------Menu----------------"
    echo "#####################################"
    echo "Enter 1 Installation \"Update & Upgrade\""
    echo "Enter 2 Installation \"Net-Tools\""
    echo "Enter 3 Installation \"SSH\""
    echo "Enter 4 Installation \"Apache2\""
    echo "Enter 5 Installation \"PHP-Module\""
    echo "Enter 6 Installation \"Maria-DB\""
    echo "Enter 7 Installation \"PHPmyAdmin\""
    echo "Enter 8 Installation \"Composer\""
    echo "Enter 9 Installation \"Gastzugang\""
    echo "Enter q \"exit\""
    echo -e "\n"
}

function install_updates() {
    echo "Update & Upgrade wird durchgeführt..."
    sudo apt update && sudo apt upgrade -y
    echo "Update & Upgrade abgeschlossen!"
    sleep 2
}

function install_net_tools() {
    echo "Net-Tools wird installiert..."
    sudo apt install -y net-tools
    echo "Net-Tools Installation abgeschlossen!"
    sleep 2
}

function install_ssh() {
    echo "SSH wird installiert und konfiguriert..."
    sudo apt install -y openssh-server
    sudo sed -i 's/#UseDNS yes/UseDNS no/' /etc/ssh/sshd_config
    sudo sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
    echo 'SSHD_OPTS="-u0"' | sudo tee -a /etc/default/ssh
    sudo systemctl restart ssh
    echo "SSH Installation und Konfiguration abgeschlossen!"
    sleep 2
}

function install_apache() {
    echo "Apache2 wird installiert..."
    sudo apt install -y apache2
    sudo systemctl enable apache2
    sudo systemctl start apache2
    
    # PHP 8.3 Repository hinzufügen
    sudo curl -sSL https://packages.sury.org/php/README.txt | sudo bash -x
    sudo apt update
    
    # PHP 8.3 installieren
    sudo apt install -y php8.3 php8.3-cli php8.3-common php8.3-curl php8.3-mbstring php8.3-xml php8.3-zip php8.3-mysql php8.3-gd php8.3-fpm
    
    # PHP Info Datei erstellen
    echo "<?php phpinfo(); ?>" | sudo tee /var/www/html/phpinfo.php
    
    # VirtualHost erstellen
    echo '<VirtualHost *:80>
    ServerName servername
    ServerAlias *.servername
    DocumentRoot "/vagrant/public"
    ServerAdmin admin@servername
    DirectoryIndex index.php index.html index.htm
    <Directory "/vagrant/public">
        Options +Indexes +FollowSymLinks +MultiViews
        AllowOverride All
        Require all granted
    </Directory>
</VirtualHost>' | sudo tee /etc/apache2/sites-available/example.conf
    
    sudo a2ensite example.conf
    sudo a2dissite 000-default.conf
    sudo systemctl restart apache2
    
    echo "Apache2 mit PHP 8.3 Installation abgeschlossen!"
    sleep 2
}

function php_modules() {
    while true; do
        clear
        echo "PHP Module Management"
        echo "1. Install PHP Module"
        echo "2. Remove PHP Module"
        echo "3. Back to main menu"
        read -p "Enter your choice: " php_choice
        
        case $php_choice in
            1)
                read -p "Enter module name to install (e.g., php8.3-json): " module
                sudo apt install -y $module
                ;;
            2)
                read -p "Enter module name to remove (e.g., php8.3-json): " module
                sudo apt remove -y $module
                ;;
            3)
                break
                ;;
            *)
                echo "Invalid option!"
                sleep 1
                ;;
        esac
    done
}

function install_mariadb() {
    echo "MariaDB wird installiert..."
    sudo apt install -y mariadb-server
    sudo mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED BY 'root';"
    sudo mysql -e "CREATE USER 'root'@'%' IDENTIFIED BY 'root';"
    sudo mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;"
    sudo mysql -e "FLUSH PRIVILEGES;"
    echo "MariaDB Installation abgeschlossen!"
    sleep 2
}

function install_phpmyadmin() {
    echo "phpMyAdmin wird installiert..."
    sudo apt install -y phpmyadmin
    sudo ln -s /usr/share/phpmyadmin /var/www/html/phpmyadmin
    
    # Blowfish Secret setzen
    sudo sed -i "s/\$cfg\['blowfish_secret'\] = '';/\$cfg\['blowfish_secret'\] = '$(openssl rand -base64 32)';/" /etc/phpmyadmin/config.inc.php
    
    # Datenbanken verstecken
    sudo sed -i "/\$cfg\['Servers'\]\[\$i\]\['hide_db'\] = '';/a \$cfg\['Servers'\]\[\$i\]\['hide_db'\] = 'mysql|information_schema|performance_schema|phpmyadmin|sys';" /etc/phpmyadmin/config.inc.php
    
    # Berechtigungen setzen
    sudo chown -R www-data:www-data /usr/share/phpmyadmin
    sudo chmod -R 755 /usr/share/phpmyadmin
    
    echo "phpMyAdmin Installation abgeschlossen!"
    sleep 2
}

function install_composer() {
    echo "Composer wird installiert..."
    php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
    php composer-setup.php
    php -r "unlink('composer-setup.php');"
    sudo mv composer.phar /usr/local/bin/composer
    echo "Composer Installation abgeschlossen!"
    sleep 2
}

function install_guest() {
    echo "Gastzugang wird eingerichtet..."
    # sudoers Eintrag für vagrant
    echo "vagrant ALL=(ALL) NOPASSWD:ALL" | sudo tee -a /etc/sudoers
    
    # Verzeichnisberechtigungen
    sudo chown -R vagrant:vagrant /vagrant
    sudo chmod -R 0777 /vagrant
    
    # VirtualBox Guest Additions
    sudo apt install -y linux-headers-$(uname -r) build-essential dkms
    sudo mount /dev/cdrom /mnt
    sudo /mnt/VBoxLinuxAdditions.run
    sudo systemctl restart systemd-modules-load
    echo "Gastzugang eingerichtet! Bitte System neustarten."
    sleep 2
}

# Hauptmenü
while true; do
    header
    read -p "Enter your choice: " choice
    
    case $choice in
        1) install_updates ;;
        2) install_net_tools ;;
        3) install_ssh ;;
        4) install_apache ;;
        5) php_modules ;;
        6) install_mariadb ;;
        7) install_phpmyadmin ;;
        8) install_composer ;;
        9) install_guest ;;
        q|Q) echo "Skript wird beendet..."; exit 0 ;;
        *) echo "Ungültige Auswahl!"; sleep 1 ;;
    esac
done
