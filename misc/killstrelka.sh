#/bin/sh

docker container kill strelka_frontend_1 strelka_customBE strelka_manager_1 strelka_coordinator_1 strelka_gatekeeper_1 clamav
docker container prune -f
docker volume prune -f
