#!/bin/bash


function no_env {
    echo ""
    echo "WG_SERVER_ADDR or WG_SERVER_KEY not set"; 
    echo ""
    echo "run source ./wg_env or set each variable like so:";
    echo ""
    echo "export WG_SERVER_ADDR=<WG server hostname or IP>";
    echo "export WG_SERVER_KEY=<WG server public key>";
    echo "export WG_DNS=<DNS server IP> (optional, default: 8.8.8.8)";
    echo ""

    exit 1;
}

function no_wireguard {
    echo "Error"
    echo "Could not find wireguard. 
You must install wireguard first: https://www.wireguard.com/install/"
    echo ""

    exit 1;
}

function no_qrencode {
    echo "Error"
    echo "Could not find qrencode."
    echo ""

    exit 1;
}

function file_exists {
    echo "Error:"
    echo "wg0.conf exists.  Move or delete it.  There's no force option to 
overwrite because you risk losing your keys.  You moving the 
file is your confirmation that you would like to generate a new config."
    echo ""


    exit 1;
}

# Pre-reqs
[[ -z "${WG_SERVER_ADDR}" ]] || [[ -z "${WG_SERVER_KEY}" ]] && no_env
[[ -x "$(which wg)" ]] || no_wireguard
[[ -x "$(which qrencode)" ]] || no_qrencode
[[ -e "wg0.conf" ]] && file_exists

# Optional DNS
[[ -z "${WG_DNS}" ]] && WG_DNS=8.8.8.8

WG_CLIENT_PRIVATE_KEY=$(wg genkey)
WG_CLIENT_PUB_KEY=$(echo $WG_CLIENT_PRIVATE_KEY | wg pubkey)

read -e -p "Enter the tunnel IP for this new client:" -i "10.0.0.2/8" WG_CLIENT_IP

echo ""

cat << EOF > wg0.conf
[Interface]
PrivateKey = $WG_CLIENT_PRIVATE_KEY
Address = $WG_CLIENT_IP
DNS = $WG_DNS

[Peer]
PublicKey = $WG_SERVER_KEY
AllowedIPs = 0.0.0.0/0
Endpoint = $WG_SERVER_ADDR
PersistentKeepalive = 30
EOF

echo 'File "wg0.conf" generated.  Give this information to the server administrator:';
echo ""

echo "client public key: $WG_CLIENT_PUB_KEY"
echo "client tunnel IP: $WG_CLIENT_IP"
echo ""


qrencode -t ANSI -r wg0.conf
