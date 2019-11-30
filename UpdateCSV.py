import urllib.request
from zipfile import ZipFile
import UploadCSV
import os
import argparse
from cligui import cligui

def main():
    print('Beginning file download from Epicollect...')


    parser = argparse.ArgumentParser()

    #EXAMPLE USAGE:
    #python3 UpdateCSV.py -name my-project -sheetsurl https://docs.google.com/spreadsheets/d/1xyqWo7q6nlExkjVAvbrEI8yw0jNeGn3i9VWGUoZU3vw/edit#gid=0
    parser.add_argument("-name", "--projectname", dest = "name", default = "", help="Epicollect Project Name.  ex: asm-f19-phenology-trees")
    parser.add_argument("-sheetsurl", "--sheetsurl", dest = "sheetsURL", default = "", help="Google Sheets Website URL. ex: https://docs.google.com/spreadsheets/d/1xyqWo7q6nlExkjVAvjasdfkji9VWGUoZU3vw")

    args = parser.parse_args()
    print(args)

    if(args.name!='' and args.sheetsURL!=''):
        processArgs(args)
    else:
        cligui.CliGui(parser, processArgs)




def processArgs(args):
    if(args.name!=''):
        userInput = args.name
    else:
        userInput = input("Enter the Epicollect Project Name, as it appears in the Website URL. For example: asm-f19-phenology-trees\n")
        #url = 'https://five.epicollect.net/api/internal/download-entries/asm-f19-phenology-trees?filter_by=created_at&format=csv&map_index=0'

    url = 'https://five.epicollect.net/api/internal/download-entries/' + str(userInput) + '?filter_by=created_at&format=csv&map_index=0'


    urllib.request.urlretrieve(url, 'csv.zip')

    print('Beginning file download from Epicollect...')


    zip = ZipFile('csv.zip')
    zipName = zip.namelist()[0]
    zip.extractall()

    print('Unzipped file to: ' + zipName)
    UploadCSV.main(zipName, args.sheetsURL)



if __name__ == '__main__':
    main()
