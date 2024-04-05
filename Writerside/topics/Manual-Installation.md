# Manual Installation

This installation guide assumes that you have installed the latest version of Ubuntu or other Debian-based Linux distributions on the target server.

**Installing web server**
<code-block lang="shell">sudo apt update</code-block>
<code-block lang="shell">sudo apt install apache2 -y</code-block>

**Downloading files on server**

<p>To install the production version (stable and secure | recommended), visit [https://github.com/kioydiolabs/Kioydioshort/releases/tag/production-release](https://github.com/kioydiolabs/Kioydioshort/releases/tag/production-release).
Then, search for the latest release with the "production-release tag". The version name will also end in "-prod".</p>
<img src="Latest-Release-GitHub.png" height="370"></img>

Then, right click on the file "api.py" and select _copy link address_.

<img src="CopyLink.png" height="150"></img>

Now, on your server terminal again, navigate to the directory `/etc/` with the command
<code-block lang="shell">cd /etc/</code-block>
Then, create a directory called kioydioshort with the command
<code-block lang="shell">sudo mkdir kioydioshort</code-block>
Now, download the file with the command wget and the link you copied earlier.
<code-block lang="shell">wget [link-you-copied-here-without-the-brackets]</code-block>
Install the required Python modules with the command
<code-block lang="shell">sudo pip install Flask</code-block>
At this point, the API should be ready to test. To start the backend API use the command
<code-block lang="shell">python3 api.py</code-block>
Then, open a browser window, and navigate to the IP adress of the server, on port 5000, on endpoint /create/ with the URL attribute set as the target URL which is the URL to be shortened.
The complete endpoint should look like this : <code-block lang="http">http://[IP-Address]:5000/create/?url=[URL-to-shorten]</code-block>
The API should return a shortened URL in plain text. If the URL works, the API is working well.

**Set up API as a service**

To automatically run the API file as a service on your server, do the following :

Navigate to the directory `/etc/systemd/system/`
<code-block lang="shell">cd /etc/systemd/system</code-block>

Download the `kioydioshort.service` file from the GitHub release by right-clicking the asset and copying the link on GitHub the same way as downloading the API script.
<code-block lang="shell">wget [kioydioshort.service-file-link-from-github]</code-block>

The file `kioydioshort.service` creates a service that will autostart the API every time the server is rebooted. To enable the service run
<code-block lang="shell">sudo systemctl enable kioydioshort</code-block>

Finally, to start the service right now, use
<code-block lang="shell">sudo systemctl start kioydioshort</code-block>

**Installing the frontend GUI**

First, change your directory to `/var/www/html`
<code-block lang="shell">cd /var/www/html</code-block>

Delete the default index.html file
<code-block lang="shell">sudo rm index.html</code-block>

Then, use wget to download the frontend.zip file the same way we did with api.py and kioydioshort.service, by copying the link from the GitHub release asssets.
<code-block lang="shell">wget [frontend.zip-file-link-from-github]</code-block>

Then, install unzip using the command
<code-block lang="shell">sudo apt install unzip</code-block>

Use unzip to extract the contents of the archive
<code-block lang="shell">unzip frontend.zip</code-block>

Finally, delete the frontend.zip file
<code-block lang="shell">sudo rm frontend.zip</code-block>

Now visit your server's IP address and make sure the frontend is working.

**Editing the shortened URL**

To change the IP address or use a domain (assuming that you have already mapped an A record on your domain to the server or used a proxy such as Cloudflare Tunnels), do the following

First, go to the API directory
<code-block lang="shell">cd /etc/kioydioshort</code-block>

Then, use nano to edit the file
<code-block lang="shell">sudo nano api.py</code-block>

Navigate to line 37 with the keyboard arrows. Then change the 127.0.0.1 IP address which means localhost to the actual private IP address of the server, or a domain, again assuming that the domain has already been mapped to the server.

![edit_ip_address.png](edit_ip_address.png)

Finally, exit nano by pressing <shortcut>Ctrl + X</shortcut> then <shortcut>Y</shortcut> and finally <shortcut>Enter</shortcut>.

Now, restart the API service by using
<code-block lang="shell">sudo systemctl restart kioydioshort</code-block>

Your URL shortener should now function as needed!
Your frontpage should be accessible at
<code-block lang="http">http://[IP-Addr-Of-Server_or_Domain]/</code-block>




[//]: # (You can make the string that goes at the end of the shortened URL longer or shorter, by editing the api.py file, and changing the default value of 6 inside the brackets on line 18.)
