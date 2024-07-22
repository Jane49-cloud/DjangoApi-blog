echo "building project packages..."
python3 -m pip install -r requirements.txt

echo "migrating database..."

python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput



echo "collecting static files..."
python3 manage.py collectstatic --noinput --clear
 echo "BUILD END"