export TERM=xterm;
rm -rf botrepo;
git clone https://<token>:x-oauth-basic@github.com/NEGANTG/delpro.git botrepo;
cd botrepo;
bash start.sh;
