mkdir external
cd ./external

mkdir tsschecker
cd ./tsschecker

wget http://api.tihmstar.net/builds/tsschecker/tsschecker-latest.zip

unzip tsschecker-latest.zip
chmod +x tsschecker_linux
rm tsschecker-latest.zip

# Install libimobiledevice.

if ! type ideviceinfo  &> /dev/null ; 
then 
    sudo apt-get install libimobiledevice libimobiledevice-utils
fi


echo "Sucesfull installed dependencies!"