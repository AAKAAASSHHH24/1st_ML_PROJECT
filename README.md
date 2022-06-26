# 1st_ML_PROJECT


creating conda environment
..........

conda create -p venv python==3.7 -y


activate the environment
............

conda activate venv/

install requirements
.............

pip install -r requirements.txt


add files to git
.............
git add .


to check git status
...................
git status


to check all versions of maintained by git
..............
git log


to create version/comit all changes
...............
git commit -m 'message'



to send changes to main
.............
git push origin main


to check remote url
............
git remote -v



To Setup a CI/CD pipeline in heroku we need 3 info:
1. heroku_email = akashrksht@gmail.com
2. heroku_API_KEY =
56b1328f-a8eb-458c-95e7-4bb2673674b1
3. heroku_app_name = beginner-a



build docker image
......
docker build -t <image_name>:<tagname>

Note: Image name for docker must be lowercase


to list docker image
...........
docker images

to run docker image
.......
docker run -p 5000:5000 -e port5000 <imageid>



to check running container
...........
docker ps


to stop docker container
.........
docker stop <container_id>



alternate for requirements.txt
...............
python setup.py install


install ipynb kernel
..............
pip install ipykernel


install YAML
.............
pip install pyYAML