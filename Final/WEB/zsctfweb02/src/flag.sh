#!/bin/sh
sed -i "s/flag{testflag}/$GZCTF_FLAG/" /var/www/html/zsctfflag.php

export GZCTF_FLAG=""
