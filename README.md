"# SIEMSa" 


for install django proyect and requirements in server 
1) create folder in server: mkdir Siemsa
2) clone repositorio: git clone url
3) install requirements pip install -r requirements.txt

instalar dependencias

sudo apt update && sudo apt install -y python3 python3-pip python3-venv build-essential libpq-dev

create virtual entorno

python3 -m venv venv
source venv/bin/activate

checkear las variables de entorno

instalar base de datos o ver si se puede usar la version que ya existe creando una nueva base de datos

aplicar migraciones de la base de datos, del proyecto para poder hacer la migracion de los datos


instalar gunicorn
pip install gunicorn

luego correr gunicorn tu_proyecto.wsgi:application --bind 0.0.0.0:8000

instalar supervisor

crear el archivo gunicorn_config.py

        bind = "0.0.0.0:8000"
        workers = 3
        accesslog = "/var/log/gunicorn/access.log"
        errorlog = "/var/log/gunicorn/error.log"
        loglevel = "info"

el directorio /var/log/gunicorn exista y tenga permisos:
    sudo mkdir -p /var/log/gunicorn
    sudo chown -R $USER:$USER /var/log/gunicorn

supervisor — Configuración en /etc/supervisor/conf.d/tu_app.conf

        [program:tu_app]
        directory=/ruta/a/tu/proyecto
        command=/ruta/a/tu/venv/bin/gunicorn tu_proyecto.wsgi:application -c /ruta/a/gunicorn_config.py
        autostart=true
        autorestart=true
        stderr_logfile=/var/log/gunicorn/error.log
        stdout_logfile=/var/log/gunicorn/access.log
        user=tu_usuario
        environment=PATH="/ruta/a/tu/venv/bin"

        
        
        /ruta/a/tu/proyecto → Ruta absoluta a tu carpeta Django (donde está manage.py)

        /ruta/a/tu/venv/bin → Ruta al binario de tu entorno virtual

        /ruta/a/gunicorn_config.py → Ruta al archivo de configuración gunicorn_config.py

        tu_usuario → Usuario con permisos para correr Gunicorn

    sudo supervisorctl reread
    sudo supervisorctl update
    sudo supervisorctl restart tu_app


Script final: siemsa

#!/bin/bash

# ✅ Validación: debe ejecutarse desde la raíz del proyecto Django
if [ ! -f manage.py ]; then
    echo "❌ Este comando debe ejecutarse desde la raíz del proyecto Django (donde está manage.py)"
    exit 1
fi

# 🔧 CONFIGURACIÓN
APP_NAME="tu_app"  # Nombre del programa en supervisor
PYTHON_PROC_KEY="gunicorn"  # Palabra clave del proceso Python (puede ser gunicorn o manage.py runserver)
SUPERVISOR_CMD=$(which supervisorctl)

# ✅ FUNCIONES

start_app() {
    echo "🟢 Iniciando $APP_NAME..."
    $SUPERVISOR_CMD start $APP_NAME
}

stop_app() {
    echo "🔴 Deteniendo $APP_NAME y procesos Python relacionados..."
    $SUPERVISOR_CMD stop $APP_NAME
    PIDS=$(pgrep -f "$PYTHON_PROC_KEY")
    if [ -n "$PIDS" ]; then
        echo "💀 Matando procesos: $PIDS"
        kill -9 $PIDS
    else
        echo "✅ No hay procesos Python activos con '$PYTHON_PROC_KEY'"
    fi
}

restart_app() {
    echo "🔁 Reiniciando $APP_NAME..."
    $SUPERVISOR_CMD restart $APP_NAME
}

status_app() {
    echo "📋 Estado de $APP_NAME:"
    $SUPERVISOR_CMD status $APP_NAME
}

# 🧭 INTERFAZ
case "$1" in
    start)
        start_app
        ;;
    stop)
        stop_app
        ;;
    restart)
        restart_app
        ;;
    status)
        status_app
        ;;
    *)
        echo "🔧 Uso: siemsa {start|stop|restart|status}"
        ;;
esac


Otorgar permisos al archivo 
chmod +x manage_server.sh


mv manage_server.sh siemsa
chmod +x siemsa
sudo mv siemsa /usr/local/bin/


como usarlo 
    siemsa start
    siemsa stop
    siemsa restart
    siemsa status


Script: siemsa-logs

#!/bin/bash

# ✅ Validación: ejecutarse desde la raíz del proyecto
if [ ! -f manage.py ]; then
    echo "❌ Este comando debe ejecutarse desde la raíz del proyecto Django (donde está manage.py)"
    exit 1
fi

# CONFIGURACIÓN
APP_NAME="tu_app"  # Nombre definido en supervisor
LOG_DIR="/var/log/supervisor"  # Ruta por defecto de logs de supervisor (ajustá si cambia)
GUNICORN_LOG="/var/log/gunicorn/gunicorn.log"
NGINX_LOG="/var/log/nginx/access.log"
NGINX_ERR="/var/log/nginx/error.log"

# FUNCIONES
show_supervisor_log() {
    LOG_FILE="$LOG_DIR/$APP_NAME-stderr---supervisor-*.log"
    echo "📄 Mostrando logs de Supervisor para $APP_NAME..."
    tail -n 100 -F $LOG_FILE
}

show_gunicorn_log() {
    echo "📄 Mostrando logs de Gunicorn..."
    tail -n 100 -F "$GUNICORN_LOG"
}

show_nginx_access() {
    echo "📄 Mostrando logs de acceso NGINX..."
    tail -n 100 -F "$NGINX_LOG"
}

show_nginx_error() {
    echo "📄 Mostrando logs de error NGINX..."
    tail -n 100 -F "$NGINX_ERR"
}

# INTERFAZ
case "$1" in
    supervisor)
        show_supervisor_log
        ;;
    gunicorn)
        show_gunicorn_log
        ;;
    nginx)
        show_nginx_access
        ;;
    nginx-error)
        show_nginx_error
        ;;
    *)
        echo "🔧 Uso: siemsa-logs {supervisor|gunicorn|nginx|nginx-error}"
        ;;
esac


darle los permisos
chmod +x siemsa-logs


sudo mv siemsa-logs /usr/local/bin/

como usarlo 
    siemsa-logs supervisor     # Logs supervisord de la app
    siemsa-logs gunicorn       # Logs gunicorn
    siemsa-logs nginx          # Logs de acceso NGINX
    siemsa-logs nginx-error    # Logs de error NGINX
        
