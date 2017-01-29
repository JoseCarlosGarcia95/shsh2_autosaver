import os, urllib2, json

apiURL = "https://api.ineal.me/tss/all"

print "Auto detecting your device..."

def get_device_info(val):
    """
        Get device information from ideviceinfo tool.
    """
    idevice_bashout = os.popen("ideviceinfo | grep " + val).read()
    idevice_bashout = idevice_bashout.replace("\n", "")
    return idevice_bashout.split(": ")[1]

def wait_until_connect():
    """
        Wait until user connect a device.
    """
    while os.popen("ideviceinfo").read() == "No device found, is it plugged in?\n":
        pass

def download_tssstatus_information(device):
    """
        Download information from tssstatus API
    """
    response = urllib2.urlopen(apiURL).read()
    data = json.loads(response)

    return data[device]

def main():
    """
        The main function!
    """
    wait_until_connect()

    productType = get_device_info("ProductType")
    uniqueChipID = get_device_info("UniqueChipID")
    deviceName = get_device_info("DeviceName")

    print "Product type: ", productType
    print "ECID: ", uniqueChipID

    tssJSON = download_tssstatus_information(productType)

    for firmware in tssJSON["firmwares"]:
        version = firmware["version"]
        print version + " is being signed!"

        os.system("./external/tsschecker/tsschecker_linux -d " + productType + " -e " + uniqueChipID + " -i " + version + " -s")

    if not os.path.exists("shsh2"):
        os.makedirs("shsh2")

    if not os.path.exists("shsh2/" + deviceName):
        os.makedirs("shsh2/" + deviceName)

    for filesondir in os.listdir("."):
        if filesondir.startswith(str(uniqueChipID)):
            os.rename(filesondir, "shsh2/" + deviceName + "/" + filesondir)


if __name__ == '__main__':
    main()
    