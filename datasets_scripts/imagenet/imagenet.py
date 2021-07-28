def download():
    """
    Provide developer with the instruction to download the dataset.
    """
    manual_download = True
    datasetName = "imagenet"
    instructions = """\
    1. Go to https://image-net.org/
    2. Create an account. 
    3. Request the access to the dataset. 
    """
    
    if manual_download:
        print("The {} dataset requires manual download due to login requirement. " \
                                "\n Please follow the instructions: {}".format(datasetName,instructions))

if __name__ == "__main__":
    download()
