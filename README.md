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
        




select * from "Canons" c 
inner join "Expedients" e 
on c."ExpedientId" = e."Id"
where e."Expediente" in (5517,
'6167',
'6172',
'6173',
'6174',
'6175',
'6176',
'6177',
'6178',
'6179',
'13526',
'18533',
'18860',
'18925',
'19767',
'21001',
'21002',
'21383',
'22891',
'48',
'50',
'53',
'54',
'57',
'60',
'62',
'63',
'65',
'67',
'68',
'70',
'84',
'86',
'203',
'204',
'206',
'266',
'1104',
'1105',
'1111',
'1112',
'3280',
'3572',
'4201',
'4202',
'4203',
'4302',
'4303',
'4304',
'4411',
'4412',
'4413',
'4415',
'4416',
'4417',
'4418',
'4419',
'4420',
'4421',
'4422',
'4423',
'4424',
'4669',
'4670',
'4671',
'4672',
'4673',
'4736',
'4737',
'5498',
'5515',
'5516',
'5517',
'5518',
'5519',
'5572',
'5574',
'6165',
'6166',
'6167',
'6168',
'6169',
'6170',
'6171',
'6172',
'6173',
'6174',
'6175',
'6176',
'6177',
'6178',
'6179',
'7111',
'7112',
'7328',
'7329',
'7330',
'7331',
'7333',
'8038',
'8040',
'8170',
'8508',
'8592',
'8905',
'8908',
'8936',
'8937',
'9328',
'9335',
'9337',
'10154',
'10245',
'11507',
'11508',
'11576',
'11577',
'11578',
'11579',
'11580',
'11873',
'12032',
'12036',
'12099',
'12438',
'12509',
'12790',
'13482',
'13486',
'13487',
'13512',
'13514',
'13515',
'13516',
'13518',
'13522',
'13523',
'13526',
'13527',
'13528',
'13555',
'13699',
'14329',
'14589',
'14728',
'14729',
'14730',
'14731',
'14732',
'14733',
'14734',
'15912',
'15913',
'15914',
'15988',
'15989',
'15990',
'15992',
'16095',
'16096',
'16097',
'16098',
'16102',
'17321',
'17514',
'17538',
'17580',
'17650',
'17681',
'17710',
'17734',
'17744',
'17816',
'17858',
'17908',
'17958',
'17970',
'17979',
'17980',
'17981',
'17982',
'18183',
'18199',
'18286',
'18360',
'18481',
'18533',
'18808',
'18833',
'18834',
'18838',
'18839',
'18840',
'18841',
'18842',
'18843',
'18844',
'18845',
'18855',
'18856',
'18857',
'18858',
'18859',
'18860',
'18861',
'18924',
'18925',
'19005',
'19006',
'19099',
'19206',
'19189',
'19668',
'19391',
'19743',
'19742',
'19745',
'19744',
'19776',
'19767',
'19983',
'19891',
'20422',
'20414',
'20925',
'20423',
'21001',
'20926',
'21383',
'21002',
'21692',
'21478',
'21694',
'21693',
'22734',
'22076',
'22891',
'22735',
'22891',
'22891',
'22891',
'22891',
)






(19767,
21478,
5517,
6167,
6172,
6173,
6174,
6175,
6176,
6177,
6178,
6179,
13526,
18533,
18860,
18925,
21001,
21002,
21383,
22891,
48,
50,
53,
54,
57,
60,
62,
63,
65,
67,
68,
70,
84,
86,
203,
204,
206,
266,
1104,
1105,
1111,
1112,
3280,
3572,
4201,
4202,
4203,
4302,
4303,
4304,
4411,
4412,
4413,
4415,
4416,
4417,
4418,
4419,
4420,
4421,
4422,
4423,
4424,
4669,
4670,
4671,
4672,
4673,
4736,
4737,
5498,
5515,
5516,
5518,
5519,
5572,
5574,
6165,
6166,
6168,
6169,
6170,
6171,
7111,
7112,
7328,
7329,
7330,
7331,
7333,
8038,
8040,
8170,
8508,
8592,
8905,
8908,
8936,
8937,
9328,
9335,
9337,
10154,
10245,
11507,
11508,
11576,
11577,
11578,
11579,
11580,
11873,
12032,
12036,
12099,
12438,
12509,
12790,
13482,
13486,
13487,
13512,
13514,
13515,
13516,
13518,
13522,
13523,
13527,
13528,
13555,
13699,
14329,
14589,
14728,
14729,
14730,
14731,
14732,
14733,
14734,
15912,
15913,
15914,
15988,
15989,
15990,
15992,
16095,
16096,
16097,
16098,
16102,
17321,
17514,
17538,
17580,
17650,
17681,
17710,
17734,
17744,
17816,
17858,
17908,
17958,
17970,
17979,
17980,
17981,
17982,
18183,
18199,
18286,
18360,
18481,
18808,
18833,
18834,
18838,
18839,
18840,
18841,
18842,
18843,
18844,
18845,
18855,
18856,
18857,
18858,
18859,
18861,
18924,
19005,
19006,
19099,
19189,
19206,
19391,
19668,
19742,
19743,
19744,
19745,
19776,
19891,
19983,
20414,
20422,
20423,
20925,
20926,
21692,
21693,
21694,
22076,
22734,
22735)





(1434,
7578,
7579,
7580,
7581,
7582,
7583,
7584,
14460,
14461,
15478,
15727,
15834,
15948,
9078,
12682,
15949,
17642,
17879,
18034,
18048,
18049,
18646,
18685,
18794,
18832,
18851,
18959,
18960,
18961,
19249,
19666,
19672,
19693,
19694,
19715,
19716,
19799,
19991,
19999,
20688,
20821,
21033,
21121,
21122,
21202,
21307,
21450,
21498,
21956,
21983,
21984,
21985,
21986,
21987,
21988,
21989,
21990,
21991,
22254,
22255,
22286,
22287,
22288,
22289,
22421,
22422,
22779,
22780,
22801,
22861,
22869,
22870,
22871,
22872,
22873,
22874,
22875,
23009,
23010,
23031,
64228)





(19632,
19644,
19822,
19823,
19824,
19961,
20347,
22601,
1236,
1237,
1238,
1266,
3843,
6377,
6399,
6400,
7540,
7871,
13127,
14563,
16573,
17455,
17662,
17798,
17897,
17918,
18503,
19111,
19117,
19428,
19476,
19481,
19521,
19522,
19523,
19524,
19525,
19526,
19527,
19528,
19529,
19560,
19597,
19631,
19633,
19663,
19970,
20020,
20021,
20022,
20046,
20111,
20113,
20160,
20161,
20260,
20261,
22267,
22268,
23196,
23198,
23199,
23200,
23203,
23204,
23205,
23206,
23208,
23539,
62066)