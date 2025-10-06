# Systemd deployment

Copy repo to /opt/pms, pmste a .env, then:
sudo cp docker-compose@pups.service /etc/systemd/system/
sudo systemctl daemon-reloadpms
sudo systemctl enable --now docker-compose@pups
