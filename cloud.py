import os
import dropbox
from dropbox.files import WriteMode
#
class TransferData:
    def __init__ (self,access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
          for filename in files:
                # construct the full local path
               local_path = os.path.join(root, filename)
               relative_path = os.path.relpath(local_path, file_from)
               dropbox_path = os.path.join (file_to,relative_path)
               with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))


def main():
    access_token='sl.BDcFpqDwnGpP02WJSxjqI9EUZl5MmP1SaRSZ_Elsc__jObi2i98fOcPSZI0IIa3KFgZDS-GW7T0TnzyHxABbiQArBaP6MNTKKuk05OS3sVYaR09lHoYbzZL0ANOBBBXRDenJKskhcwD_'
    #creating object for class
    pd = TransferData(access_token)

    file_from = input("Enter the file path to transfer : ")
    file_2 = input("enter the  path to upload to dropbox : ")

    #function defined in the class "TransferData" is called
    pd.upload_file(file_from,file_2)
    print ("files moved")
main()